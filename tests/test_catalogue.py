import json
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PageText(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.hidden = False
        self.parts = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = False

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


class CatalogueRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = {
            p["id"]: p
            for p in json.loads((ROOT / "build/problems_source.json").read_text())
            if p.get("enabled", True)
        }
        cls.home = (ROOT / "index.html").read_text()

    def test_source_and_api_status_match(self):
        for pid, record in self.source.items():
            with self.subTest(problem=pid):
                api = json.loads((ROOT / f"api/problems/{pid}.json").read_text())
                for field in ("status", "progress", "known_results", "open_problem"):
                    if field in record:
                        self.assertEqual(record[field], api.get(field))
                self.assertTrue(api.get("open_problem"))

    def test_status_specific_headings_and_copy(self):
        for pid, record in self.source.items():
            with self.subTest(problem=pid):
                page = (ROOT / f"problems/{pid}.html").read_text()
                expected = {
                    "resolved": "Resolution",
                    "solution claimed": "Claimed Resolution",
                }.get(record["status"], "Open Problem")
                self.assertIn(f"<h2>{expected}</h2>", page)
                self.assertIn(f"STATUS: {record['status']}", page)
                if record["status"] in ("resolved", "solution claimed"):
                    self.assertNotIn("<h2>Open Problem</h2>", page)

    def test_restored_design_and_number_order(self):
        for marker in ("EB+Garamond", "Figtree", "--bg:#ffffeb", "--pink:#f0d7ff", "pageSize=5"):
            self.assertIn(marker, self.home)
        self.assertIn("selectedTags.some", self.home)
        self.assertIn("return a.number-b.number", self.home)
        self.assertNotIn('id="sortselect"', self.home)

    def test_no_suitability_framing_in_visible_pages(self):
        for path in [ROOT / "index.html", ROOT / "agents.html", *sorted((ROOT / "problems").glob("*.html"))]:
            with self.subTest(page=path.name):
                visible = " ".join(PageText(path.read_text()).parts)
                for term in ("Counterexample suitability", "AlphaEvolve", "Notes for AI Solvers"):
                    self.assertNotIn(term, visible)

    def test_matroid_citations_and_computational_model(self):
        record = self.source["matroid-secretary-conjecture"]
        self.assertNotEqual(record["status"], "open")
        for text in ("2609.14555v2", "Theorem 3.1", "2611.08869v1", "real-RAM", "bit-complexity"):
            self.assertIn(text, record["known_results"])

    def test_withdrawn_claim_not_counted_as_resolution(self):
        record = self.source["uniform-decision-tree-constant-approximation"]
        self.assertEqual(record["status"], "open")
        self.assertEqual(record["progress"]["state"], "partial")
        self.assertIn("withdraw", record["known_results"])
        links = {ref["url"] for ref in record["progress"]["links"]}
        self.assertIn("https://arxiv.org/abs/2604.12036v2", links)
        self.assertIn("https://arxiv.org/abs/2604.12036v4", links)
        self.assertNotIn("https://arxiv.org/abs/2604.12036v1", links)

    def test_machine_readable_interface_preserved(self):
        for path in ("api/problems.json", "api/solutions.json", "api/schema/problem.schema.json", "api/schema/solution.schema.json", "llms.txt"):
            self.assertTrue((ROOT / path).is_file())
        self.assertIn("counterexample_suitability", self.source["matroid-secretary-conjecture"])

    def test_partial_progress_has_results_citations_and_residual_question(self):
        cases = {
            "free-order-prophet-inequality": ("2610.34892v1", "0.74500001", "Theorem 6.1"),
            "bin-packing-additive-integrality-gap": ("2611.09447v1", "log^*", "Theorem 1.3"),
            "online-matching-general-vertex-arrivals": ("2602.18049v1", "0.526", "Theorem 1.1"),
        }
        for pid, (paper, result, theorem) in cases.items():
            with self.subTest(problem=pid):
                record = self.source[pid]
                self.assertEqual(record["status"], "partially resolved")
                self.assertEqual(record["progress"]["state"], "partial")
                self.assertTrue(record["open_problem"])
                for marker in (paper, result, theorem):
                    self.assertIn(marker, record["known_results"])
                url = f"https://arxiv.org/abs/{paper}"
                for refs in (record["progress"]["links"], record["literature"]["reviewed"], record["additional_refs"]):
                    self.assertIn(url, {r["url"] for r in refs})
                page = (ROOT / f"problems/{pid}.html").read_text()
                self.assertIn(url, page)
                self.assertIn("Remaining open problem.", page)

    def test_samuels_summary_matches_reported_full_resolution(self):
        record = self.source["samuels-conjecture-independent-nonnegative-sums"]
        self.assertEqual(record["status"], "solution claimed")
        self.assertIn("infimum", record["open_problem"])
        self.assertIn("general resolution", record["open_problem"])
        self.assertNotIn("sharp upper bound", record["open_problem"])
        self.assertIn("not independently certified", record["open_problem"])


if __name__ == "__main__":
    unittest.main()
