# rolldet

[![Build](https://github.com/ionite34/rolldet/actions/workflows/build.yml/badge.svg)](https://github.com/ionite34/rolldet/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/ionite34/rolldet/branch/main/graph/badge.svg)](https://codecov.io/gh/ionite34/rolldet)
[![DeepSource](https://deepsource.io/gh/ionite34/rolldet.svg/?label=active+issues&show_trend=true&token=LlLrug9IbkUDtPWcwjOHko8k)](https://deepsource.io/gh/ionite34/rolldet/?ref=repository-badge)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ionite34/rolldet/main.svg)](https://results.pre-commit.ci/latest/github/ionite34/rolldet/main)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Frolldet.svg?type=shield)](https://app.fossa.com/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Frolldet?ref=badge_shield)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rolldet)](https://pypi.org/project/rolldet/)
[![PyPI version](https://badge.fury.io/py/rolldet.svg)](https://pypi.org/project/rolldet/)

## Advanced Rickroll Detection

- ### 🚀 Built as an asynchronous API
- ### 🔄 Resolves any short URLs
- ### 🔍 Uses copyright signature frameworks where possible
- ### 🎯 High accuracy and low rate of false positives

## Currently supports

| Site    | Method                   |
|---------|--------------------------|
| YouTube | [Content ID][content_id] |

> YouTube and Content ID are respective trademarks of Google LLC.


## Getting started
```python
from rolldet import Detector

async def main():
    det = Detector()

    result = await det.find("https://youtu.be/6-HUgzYPm9g")

    print(result)

    if result.is_roll:
        print("Rickroll detected!")
```
- `Detector.find` is a coroutine that returns a `DetectionResult`
- The above example result would have the following attribute values
```python
url -> "https://youtu.be/6-HUgzYPm9g"
redirect_url -> "https://www.youtube.com/watch?v=6-HUgzYPm9g"
is_roll -> True
error -> None
song -> "Never Gonna Give You Up"
artist -> "Rick Astley"
```

- You can easily convert these results to `dict` or `json` strings
- Note the `json` conversion will not have `None` value keys

```python
result.as_dict() ->
{'url': URL('https://youtu.be/6-HUgzYPm9g'), 'redirect_url': URL('https://www.youtube.com/watch?v=Uj1ykZWtPYI'), 'is_roll': True, 'error': None, 'song': 'Never Gonna Give You Up', 'artist': 'Rick Astley'}

result.json() ->
{"url": "https://youtu.be/6-HUgzYPm9g", "redirect_url": "https://www.youtube.com/watch?v=Uj1ykZWtPYI", "is_roll": true, "song": "Never Gonna Give You Up", "artist": "Rick Astley"}
```

## License
The code in this template is released under the [MIT License](LICENSE).

[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Frolldet.svg?type=large)](https://app.fossa.com/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Frolldet?ref=badge_large)

[content_id]: https://wikipedia.org/wiki/Content_ID_(system)
