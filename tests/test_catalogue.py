import json
import unittest
from fractions import Fraction
from html.parser import HTMLParser
from itertools import permutations, product
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

    def test_deep_sweep_is_merged_and_citations_are_rendered(self):
        audit = json.loads((ROOT / "research/status-audit-deep-sweep-2026-11-09.json").read_text())
        changed = audit["changed_problem_ids"]
        self.assertEqual(len(changed), len(set(changed)))
        self.assertEqual(len(changed), audit["coverage_counts"]["changed_entries"])
        for pid in changed:
            with self.subTest(problem=pid):
                enrichment = json.loads((ROOT / f"research/enrichment/{pid}.json").read_text())
                source = self.source[pid]
                api = json.loads((ROOT / f"api/problems/{pid}.json").read_text())
                page = (ROOT / f"problems/{pid}.html").read_text()
                for field in ("status", "full_statement", "known_results", "open_problem", "progress", "literature"):
                    if field in enrichment:
                        self.assertEqual(enrichment[field], source[field])
                        self.assertEqual(source[field], api[field])
                for ref in enrichment.get("additional_refs", []):
                    self.assertTrue(ref.get("authors"))
                    self.assertTrue(ref.get("title"))
                    self.assertIn(ref["url"], page)
                for field in ("known_results", "full_statement", "open_problem"):
                    self.assertNotIn("**", source[field])
                    self.assertNotRegex(source[field], r"\]\(https?://")

    def test_claimed_resolutions_keep_their_scope(self):
        for pid in ("precedence-unit-jobs-three-machines-complexity", "fpp-bigeodesics-nonexistence"):
            record = self.source[pid]
            self.assertEqual(record["status"], "solution claimed")
            self.assertEqual(record["progress"]["state"], "solution-claimed")
            self.assertIn("independent", record["known_results"])
        fpp = self.source["fpp-bigeodesics-nonexistence"]
        self.assertIn(r"\min(X_1,X_2,X_3,X_4)^2", fpp["full_statement"])
        self.assertIn("without that moment condition is not settled", fpp["open_problem"])
        schedule = self.source["precedence-unit-jobs-three-machines-complexity"]
        self.assertIn("150020", schedule["known_results"])

    def test_updated_guarantees_retain_assumptions(self):
        matching = self.source["edge-weighted-matching-free-disposal"]
        self.assertIn("0.556195", matching["known_results"])
        self.assertIn("oblivious", matching["full_statement"])
        self.assertNotIn("adaptive adversary", matching["full_statement"])
        subsidy = self.source["subsidy-envy-freeness-monotone"]
        self.assertIn(r"v_i(\emptyset)=0", subsidy["full_statement"])
        self.assertIn("(n-1)^{3/2}", subsidy["known_results"])
        self.assertIn("existential", subsidy["known_results"])
        inventory = self.source["dual-sourcing-inventory-optimal-policy-structure"]
        for text in ("2207.12182v2", "Assumption 6.2", "finite variance alone"):
            self.assertIn(text, inventory["known_results"])
        self.assertIn("average-cost", inventory["full_statement"])

    def test_fairness_variants_are_not_conflated(self):
        goods = self.source["efx-existence-goods"]
        self.assertIn("EFX0", goods["full_statement"])
        self.assertIn("at most nine goods", goods["known_results"])
        chores = self.source["efx-chores"]
        self.assertIn("including $c_i(g)=0$", chores["full_statement"])
        self.assertIn("at most eight chores", chores["known_results"])
        self.assertIn("multiplicative 2-EFX", chores["known_results"])
        self.assertIn("not a bi-valued existence theorem for all", chores["known_results"])

    def test_existence_computability_and_value_remain_distinct(self):
        sat = self.source["random-ksat-satisfiability-threshold"]
        self.assertEqual(sat["status"], "partially resolved")
        for text in ("Carenini", "computability", "variational"):
            self.assertIn(text, sat["known_results"] + sat["open_problem"])
        self.assertIn("no efficiency bound", sat["known_results"])
        mean_payoff = self.source["mean-payoff-games-polynomial-time"]
        self.assertEqual(mean_payoff["status"], "partially resolved")
        self.assertIn("quasipolynomial", mean_payoff["known_results"])
        self.assertIn("binary", mean_payoff["open_problem"])

    def test_conditional_and_local_bounds_keep_their_qualifiers(self):
        graphs = self.source["correlated-random-graph-matching-efficient-threshold"]
        for text in ("Conjecture 2.2", "Theorem 3.3", "not an unconditional", "depth-local"):
            self.assertIn(text, graphs["known_results"])
        restricted = self.source["restricted-assignment-makespan"]
        self.assertIn("Conjecture 10", restricted["known_results"])
        self.assertIn("conditional", restricted["known_results"])
        self.assertEqual(restricted["status"], "open")

    def test_exact_matching_affine_slice_counterexample(self):
        # Every doubly stochastic 2x2 matrix has diagonal x and off-diagonal 1-x.
        red_counts = [sum(i == j for i, j in enumerate(p)) for p in permutations(range(2))]
        self.assertEqual(sorted(red_counts), [0, 2])
        self.assertNotIn(1, red_counts)
        x = Fraction(1, 2)  # The exact-one-red hyperplane forces 2*x = 1.
        sliced_vertex = ((x, 1 - x), (1 - x, x))
        self.assertTrue(all(sum(row) == 1 for row in sliced_vertex))
        self.assertTrue(all(sum(col) == 1 for col in zip(*sliced_vertex)))
        self.assertEqual(sum(sliced_vertex[i][i] for i in range(2)), 1)
        self.assertTrue(all(value.denominator == 2 for row in sliced_vertex for value in row))
        record = self.source["exact-matching-derandomization"]
        self.assertEqual(record["status"], "open")
        for text in ("2.7(iii)", "eight structural hypotheses", "not the main algorithmic conclusion"):
            self.assertIn(text, record["known_results"])

    def test_graph_balancing_six_edge_witness(self):
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 2), (1, 3, 2)]
        makespans = []
        for orientation in product((0, 1), repeat=len(edges)):
            loads = [0] * 4
            for side, edge in zip(orientation, edges):
                loads[edge[side]] += edge[2]
            makespans.append(max(loads))
        self.assertEqual(min(makespans), 3)
        # Each vertex mixes its heavy edge and its two light edges equally.
        coverage = [Fraction(0)] * len(edges)
        for vertex in range(4):
            for weight in (1, 2):
                configuration = [i for i, (u, v, w) in enumerate(edges) if vertex in (u, v) and w == weight]
                self.assertEqual(sum(edges[i][2] for i in configuration), 2)
                for i in configuration:
                    coverage[i] += Fraction(1, 2)
        self.assertEqual(coverage, [1] * len(edges))
        self.assertEqual(Fraction(sum(w for _, _, w in edges), 4), 2)


if __name__ == "__main__":
    unittest.main()
