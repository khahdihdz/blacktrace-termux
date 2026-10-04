import json
import py_compile
from pathlib import Path

def test_cases_are_valid():
    data = json.loads(Path("data/cases.json").read_text(encoding="utf-8"))
    assert len(data) >= 5
    ids = [c["id"] for c in data]
    assert len(ids) == len(set(ids))
    for case in data:
        assert case["flag"].startswith("BLACKTRACE{")
        assert case["clues"]

def test_i18n_is_bilingual_and_complete():
    ui = json.loads(Path("data/i18n.json").read_text(encoding="utf-8"))
    assert set(ui) == {"vi", "en", "cases"}
    assert ui["vi"].keys() == ui["en"].keys()
    assert set(ui["cases"]) >= {"1","2","3","4","5"}
    for case in ui["cases"].values():
        assert case["title"]
        assert case["objective"]

def test_python_compiles():
    py_compile.compile("blacktrace.py", doraise=True)
