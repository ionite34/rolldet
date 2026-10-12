from __future__ import annotations

from typing import AsyncGenerator, Iterable

import pytest
import pytest_asyncio

from rolldet.detector import Detector


@pytest_asyncio.fixture
async def detector() -> AsyncGenerator[Detector]:
    yield Detector()


# noinspection PyShadowingNames
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "urls, expected",
    [
        (
            [
                "https://www.youtube.com/watch?v=Uj1ykZWtPYI",
            ],
            {
                "is_roll": True,
                "song": "Never Gonna Give You Up",
                "artist": "Rick Astley",
            },
        ),
        (
            [
                "https://youtu.be/dQw4w9WgXcQ",
            ],
            {
                "is_roll": True,
                "song": 'Never Gonna Give You Up (7" Mix)',
                "artist": "Rick Astley",
            },
        ),
        (
            [  # Rick Roll in title but not rickroll
                "https://www.youtube.com/watch?v=PUew7VIUfnA",
            ],
            {
                "is_roll": False,
            },
        ),
        (
            [  # Expect 404
                "https://www.google.com/404",
            ],
            {
                "is_roll": False,
                "error": "404",
            },
        ),
        (
            [  # Expect no domain
                "https://unknown.example.org/",
            ],
            {
                "is_roll": False,
                "error": "Could not connect to host",
            },
        ),
        (
            [  # Expect no data, since short
                "https://www.youtube.com/shorts/96GnOB1iZQI",
                # No video at URL
                "https://www.youtube.com/watch?v=vAV0Q-pq_L",
            ],
            {
                "is_roll": False,
                "error": "Could not find YouTube data",
            },
        ),
    ],
)
async def test_detector_results(
    detector: Detector, urls: Iterable[str], expected: dict
) -> None:
    for url in urls:
        result = await detector.find(url)
        _dict = result.as_dict()
        for key, value in expected.items():
            assert _dict[key] == value


# noinspection PyShadowingNames
@pytest.mark.asyncio
async def test_detector_invalid(detector: Detector) -> None:
    """Test invalid URL with json result."""
    result = await detector.find("https://example.org")
    # Result should be falsy
    assert not result
    # Convert to json
    _json = result.json()
    assert (
        _json == '{"url": "https://example.org", '
        '"is_roll": false, '
        '"error": "Unsupported Link Type"}'
    )


@pytest.mark.parametrize(
    "text, expected",
    [
        ("var ytInitialData = {};<", {}),  # Normal empty data
        ("example", None),  # No regex match
        ("var ytInitialData = A;<", None),  # JSONDecodeError case
        ("var ytInitialData =;<", None),  # No data case
    ],
)
def test_parse_youtube(text: str, expected: str | None) -> None:
    assert Detector._parse_youtube(text) == expected
