# Target for analysis
from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from functools import cached_property

from httpx import URL

RE_YOUTUBE = re.compile(
    r"^((?:https?:)?//)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))"
    r"(/(?:[\w\-]+\?v=|embed/|v/)?)([\w\-]+)(\S+)?$"
)


class TargetType(Enum):
    """Enum for target link types."""

    unknown = 0
    youtube = 1


@dataclass
class Target:
    """Target URL for analysis."""

    url: URL

    @cached_property
    def link_type(self) -> TargetType:
        """Parse link and determine link_type"""
        if self.url.host == "www.youtube.com":
            return TargetType.youtube
        if RE_YOUTUBE.findall(str(self.url)):
            return TargetType.youtube
        return TargetType.unknown
