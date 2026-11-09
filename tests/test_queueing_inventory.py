import json
import unittest
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "research/status-audit-queueing-inventory-2026-11-09.json"


class QueueingInventoryRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = {
            p["id"]: p
            for p in json.loads((ROOT / "build/problems_source.json").read_text())
        }

    def test_pass_is_merged_and_rendered(self):
        audit = json.loads(AUDIT.read_text())
        ids = audit["changed_problem_ids"] + audit["new_problem_ids"]
        self.assertEqual(len(ids), len(set(ids)))
        for pid in ids:
            with self.subTest(problem=pid):
                folder = "new" if pid in audit["new_problem_ids"] else "enrichment"
                staged = json.loads((ROOT / f"research/{folder}/{pid}.json").read_text())
                source = self.records[pid]
                api = json.loads((ROOT / f"api/problems/{pid}.json").read_text())
                page = (ROOT / f"problems/{pid}.html").read_text()
                for field in ("status", "full_statement", "known_results", "open_problem", "progress", "literature"):
                    if field in staged:
                        self.assertEqual(staged[field], source[field])
                        self.assertEqual(source[field], api[field])
                self.assertNotEqual(source["short_statement"], source["open_problem"])
                self.assertIn("Remaining open problem.", source["known_results"])
                for ref in staged.get("additional_refs", []):
                    self.assertTrue(ref.get("authors"))
                    self.assertIn(ref["url"], page)

    def test_queueing_results_retain_assumptions(self):
        multi = self.records["multi-server-job-queue-stability-region"]
        for marker in ("2601.20653v1", "Theorems 4.2 and 5.1", "not a certified error bound"):
            self.assertIn(marker, multi["known_results"])
        self.assertIn("critical", multi["agent_guidance"]["verification_notes"])
        mgk = self.records["mgk-queue-exact-stationary-performance"]
        for marker in ("2510.11015v3", "Assumption 3", "non-lattice", "Jobs in service are excluded"):
            self.assertIn(marker, mgk["known_results"])
        switch = self.records["input-queued-switch-maxweight-heavy-traffic-distribution"]
        for marker in ("symmetric variances", "conditional", "not the full joint"):
            self.assertIn(marker, switch["known_results"])
        bar = self.records["sbp-queueing-network-bar-tight-matrix-condition"]
        self.assertIn("uniform integrability", bar["open_problem"])
        self.assertIn("does not refute", bar["known_results"])

    def test_inventory_limits_are_not_conflated(self):
        lost = self.records["lost-sales-inventory-positive-lead-time-optimal-policy"]
        for marker in ("Assumption 1", "Theorem 2(b)", "regularly varying", "fixed-$L$"):
            self.assertIn(marker, lost["known_results"])
        perishable = self.records["perishable-inventory-optimal-policy"]
        self.assertIn("zero replenishment lead time", perishable["full_statement"])
        self.assertIn("full theorem assumptions were not accessible", perishable["known_results"])
        self.assertIn("10.1287/mnsc.2023.03801", json.dumps(perishable["additional_refs"]))
        self.assertNotIn("Recent work on asymptotic optimality", json.dumps(perishable))
        capacity = self.records["stochastic-inventory-capacity-constraints-policy-structure"]
        self.assertIn("zero terminal cost", capacity["full_statement"])
        self.assertIn("not a stationary infinite-horizon", capacity["known_results"])

    def test_matching_resolution_is_scoped(self):
        record = self.records["dynamic-spatial-matching-greedy"]
        self.assertEqual(record["status"], "partially resolved")
        for marker in ("2210.03166v3", "constant-competitive", "not a theorem for ordinary greedy"):
            self.assertIn(marker, record["known_results"])
        self.assertIn("Demand does not wait", record["full_statement"])
        self.assertIn("dimension at least two", record["open_problem"])

    def test_new_routing_problem_keeps_the_slack_benchmark(self):
        record = self.records["skill-based-queue-routing-logarithmic-regret"]
        for marker in ("Bernoulli", "consistency condition", "not the zero-slack value"):
            self.assertIn(marker, record["full_statement"])
        for marker in ("editorial inference", "admissible confusing", "2\\beta"):
            self.assertIn(marker, record["known_results"])

    def test_rossi_chen_tarim_counterexample_exactly(self):
        # Example 3, Tables 2-3: integer probabilities over 1000 avoid rounding.
        demands = (
            ((34, 18), (159, 888), (281, 46), (286, 48)),
            ((14, 28), (223, 271), (225, 170), (232, 531)),
            ((5, 41), (64, 27), (115, 889), (171, 43)),
            ((35, 69), (48, 8), (145, 19), (210, 904)),
        )
        for distribution in demands:
            self.assertEqual(sum(prob for _, prob in distribution), 1000)

        @lru_cache(maxsize=None)
        def bellman(t, x):
            if t == 4:
                return 0, (0,)
            scale = 1000 ** (4 - t)
            costs = []
            for q in range(42):
                value = (250 if q else 0) * scale
                for demand, prob in demands[t]:
                    y = x + q - demand
                    stage = max(y, 0) + 26 * max(-y, 0)
                    future, _ = bellman(t + 1, y)
                    value += prob * (stage * (scale // 1000) + future)
                costs.append(value)
            optimum = min(costs)
            return optimum, tuple(q for q, cost in enumerate(costs) if cost == optimum)

        # All reachable states are recursively evaluated; there is no truncation.
        for inventory, order in ((601, 33), (602, 0), (615, 0), (616, 41), (617, 41), (618, 41), (619, 0)):
            with self.subTest(inventory=inventory):
                self.assertEqual(bellman(0, inventory)[1], (order,))


if __name__ == "__main__":
    unittest.main()
