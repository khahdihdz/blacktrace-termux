import json
from pathlib import Path

def test_cases_are_valid():
    data = json.loads(Path("data/cases.json").read_text(encoding="utf-8"))
    assert len(data) >= 5
    ids = [c["id"] for c in data]
    assert len(ids) == len(set(ids))
    for case in data:
        assert case["flag"].startswith("BLACKTRACE{")
        assert case["clues"]
