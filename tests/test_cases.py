import json
import py_compile
import unittest
from pathlib import Path

class BlacktraceTests(unittest.TestCase):
    def test_cases_are_valid(self):
        data = json.loads(Path("data/cases.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data), 5)
        ids = [c["id"] for c in data]
        self.assertEqual(len(ids), len(set(ids)))
        for case in data:
            self.assertTrue(case["flag"].startswith("BLACKTRACE{"))
            self.assertTrue(case["clues"])

    def test_i18n_is_bilingual_and_complete(self):
        ui = json.loads(Path("data/i18n.json").read_text(encoding="utf-8"))
        self.assertEqual(set(ui), {"vi", "en", "cases"})
        self.assertEqual(set(ui["vi"]), set(ui["en"]))
        self.assertGreaterEqual(set(ui["cases"]), {"1", "2", "3", "4", "5"})
        for case in ui["cases"].values():
            self.assertTrue(case["title"])
            self.assertTrue(case["objective"])

    def test_python_compiles(self):
        py_compile.compile("blacktrace.py", doraise=True)

if __name__ == "__main__":
    unittest.main()
