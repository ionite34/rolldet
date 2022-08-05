from __future__ import annotations

import json
from dataclasses import asdict, dataclass

from httpx import URL


@dataclass
class DetectResult:
    """Dataclass for Detection results."""

    url: URL
    redirect_url: URL | None = None
    is_roll: bool = False
    error: str | None = None
    song: str | None = None
    artist: str | None = None

    def __bool__(self) -> bool:
        """Return whether the result is a roll."""
        return self.is_roll

    def with_error(self, error: str) -> DetectResult:
        """Return a new result with an error."""
        return DetectResult(self.url, self.redirect_url, self.is_roll, error)

    def as_dict(self) -> dict:
        """Return a dictionary representation of the result."""
        return asdict(self)

    def json(self) -> str:
        """Return a JSON representation of the result."""
        _dict = self.as_dict()
        result = {}
        for key, val in _dict.items():
            if val is None:
                continue
            # Cast to str
            if not isinstance(val, (bool, str)):
                val = str(val)
            # Add to result
            result[key] = val
        return json.dumps(result)
