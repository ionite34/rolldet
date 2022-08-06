from __future__ import annotations

import json
import re
from typing import Any

from httpx import URL, AsyncClient, ConnectError

from rolldet.result import DetectResult
from rolldet.target import Target, TargetType

RE_YT_DATA = re.compile(r"(?<=var ytInitialData =)[^\n]*")

# Path for a list of dicts
INFO_PATH = (
    "engagementPanels/1/engagementPanelSectionListRenderer/content"
    "/structuredDescriptionContentRenderer/items/1"
    "/videoDescriptionMusicSectionRenderer/carouselLockups/0/"
    "carouselLockupRenderer/infoRows"
)


class Detector:
    """Analyze links for rick-roll detection"""

    def __init__(self) -> None:
        self.client = AsyncClient()

    @staticmethod
    def _determine_result(song: str, artist: str) -> bool:
        """Determine from song and artist if this is a valid match"""
        song = song.lower()
        artist = artist.lower()
        return "rick astley" in artist and "never gonna give you up" in song

    @staticmethod
    def _get_song_info(info_rows: list) -> dict:
        """Get song info from infoRows list"""
        result = {}
        for row in info_rows:
            info = row.get("infoRowRenderer", {})
            title = info.get("title", {}).get("simpleText")
            metadata = info.get("defaultMetadata")

            # 2 types of metadata, list of runs or direct dict
            # Try to get `simpleText` first
            entry = None
            if "simpleText" in metadata:
                entry = metadata["simpleText"]
            elif "runs" in metadata:
                runs = metadata["runs"]
                run = runs[0] if runs else None
                entry = run["text"] if run else None

            if title == "SONG":
                result["song"] = entry
            elif title == "ARTIST":
                result["artist"] = entry

            # Exit if both found
            if len(result) == 2:
                break

        return result

    @staticmethod
    def _get_path(dict_: dict, path: str) -> Any | None:
        """Attempt to get a nested path inside a json dict"""
        data: Any = dict_
        for part in path.split("/"):
            if isinstance(data, dict):
                data = data.get(part)

            elif isinstance(data, list):
                try:
                    data = data[int(part)]
                except (IndexError, ValueError):
                    data = None

            if data is None:
                return None

        return data

    @staticmethod
    def _parse_youtube(response_text: str) -> dict | None:
        """Parse YouTube web response to ytInitialData dict"""
        match = RE_YT_DATA.search(response_text)

        if not match or not match.group():
            return None

        result = match.group().split(";<")
        parsable = result[0].strip() if result else None

        if parsable:
            try:
                return json.loads(parsable)
            except json.JSONDecodeError:
                pass

        return None  # If none found

    async def find(self, url: str) -> DetectResult:
        """
        Find if a URL is a rick-roll.

        Args:
            url: URL to check
        """
        result = DetectResult(URL(url))
        target = Target(URL(url))

        try:
            response = await self.client.get(target.url, follow_redirects=True)
        except ConnectError:
            return result.with_error("Could not connect to host")

        if response.status_code == 404:
            return result.with_error("404")

        # Check if redirected
        if response.has_redirect_location or URL(url) != response.url:
            # Set result in case of redirect
            target.url = response.url
            result.redirect_url = response.url

        # Parse to see if this is a YouTube video
        if target.link_type == TargetType.youtube:
            # Parse to dict
            data = self._parse_youtube(response.text)
            if not data:
                return result.with_error("Could not parse YouTube data")

            # Find inner list for music data
            data = self._get_path(data, INFO_PATH)
            if not data or not isinstance(data, list):
                return result.with_error("Could not find YouTube data")

            # Get song info from data list
            song_info = self._get_song_info(data)
            if not song_info:
                return result.with_error("Could not find song info")

            # Set result
            result.song = song_info["song"]
            result.artist = song_info["artist"]

            # Check if this is a roll
            result.is_roll = self._determine_result(
                song_info["song"], song_info["artist"]
            )

            return result

        # If none found
        return result.with_error("Unsupported Link Type")
