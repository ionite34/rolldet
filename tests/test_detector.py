from typing import AsyncGenerator, Iterable

import pytest
import pytest_asyncio

from rolldet.detector import Detector


@pytest_asyncio.fixture
async def detector() -> AsyncGenerator[Detector, None]:
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
