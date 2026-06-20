import json, datetime, re
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent

SRC = [
  ("mig_online_market.json", None),
  ("mig_stoch_approx_notes.json", None),
  ("new_om_or_ms.json", None),
]
REQ = ["id","title","collection","area","status","short_statement","full_statement","source"]

OPEN_OVERRIDES = {
  "online-makespan-scheduling-gap": "Determine the exact asymptotic deterministic competitive ratio for online makespan scheduling on identical machines.",
  "randomized-list-update": "Determine the optimal randomized competitive ratio for the list update problem against an oblivious adversary.",
  "prophet-secretary-tight-ratio": "Determine the exact prophet-secretary constant for independent non-identical rewards arriving in uniformly random order.",
  "online-bipartite-matching-random-order": "Determine the optimal competitive ratio for online bipartite matching under uniformly random arrivals, and the exact ratio of RANKING in this model.",
  "lost-sales-inventory-positive-lead-time-optimal-policy": "Characterize the exact optimal policy for periodic-review lost-sales inventory with positive deterministic lead time, or prove sharp non-asymptotic guarantees for a simple policy class.",
  "dual-sourcing-inventory-optimal-policy-structure": "Characterize the exact optimal policy for dual sourcing when the regular and expedited lead times differ by at least two periods.",
  "optimal-policy-one-warehouse-multi-retailer": "Characterize the optimal replenishment-and-allocation policy for one-warehouse multi-retailer inventory under the true nonnegative-allocation constraints.",
  "closed-form-optimal-policy-general-assembly-systems": "Find a closed-form or polynomial-time characterization of the dynamic base-stock levels for general assembly systems, and understand what survives with positive fixed ordering costs.",
  "weber-weiss-whittle-index-asymptotic-optimality": "Give checkable conditions under which Whittle's index policy is asymptotically optimal, and characterize when its optimality gap is $O(\\sqrt N)$, $O(1)$, or exponentially small.",
  "bayesian-mab-switching-costs-optimal-policy": "Characterize the optimal policy for discounted Bayesian multi-armed bandits with positive switching costs, or give a tractable policy with provable optimality-gap guarantees.",
  "stochastic-bandits-switching-cost-regret": "Determine the exact gap-dependent regret and the tight minimax dependence for stochastic bandits with general switching-cost matrices.",
  "cmu-theta-rule-exact-optimality-abandonment": "Characterize when a static priority or index rule, such as $c\\mu/\\theta$, is exactly optimal for multiclass queues with abandonment.",
  "optimal-routing-heterogeneous-parallel-servers": "Determine the exact optimal dispatching policy for heterogeneous parallel-server queues, especially beyond asymptotic or heuristic speed-aware rules.",
  "nrm-relaxation-gap-degenerate-and-choice": "Find a tractable policy with $O(1)$ regret for general choice-based network revenue management, including degenerate CDLP instances, or prove such regret is impossible.",
  "stochastic-scheduling-optimal-policy-release-precedence": "Characterize the optimal non-anticipative policy for stochastic scheduling with release dates or precedence constraints, or determine the precise complexity of computing it.",
  "metric-tsp-four-thirds-integrality-gap": "Determine the exact integrality gap of the subtour-elimination (Held-Karp) LP for metric TSP; in particular, prove or refute the $4/3$ conjecture.",
  "atsp-held-karp-integrality-gap": "Determine the exact integrality gap of the Held-Karp LP for asymmetric metric TSP, closing the gap between the lower bound $2$ and the upper bound $22$.",
  "steiner-tree-bidirected-cut-integrality-gap": "Determine the exact integrality gap of the bidirected-cut relaxation for Steiner tree.",
  "steiner-tree-approximation-ratio-gap": "Determine the optimal polynomial-time approximation ratio for graph Steiner tree and the exact integrality gap of the hypergraphic LP.",
  "santa-claus-config-lp-integrality-gap": "Determine the exact integrality gap of the configuration LP for restricted Santa Claus / restricted max-min fair allocation.",
  "beck-fiala-conjecture": "Prove or refute the Beck-Fiala conjecture that every degree-$t$ set system has discrepancy $O(\\sqrt t)$.",
  "komlos-conjecture": "Prove or refute the Komlos conjecture that unit Euclidean norm vectors can always be signed to have $O(1)$ discrepancy in every coordinate.",
  "matrix-spencer-conjecture": "Prove or refute the full-rank Matrix Spencer conjecture: can $n$ bounded symmetric matrices always be signed to have spectral norm $O(\\sqrt n)$?",
  "metric-facility-location-gap": "Determine the exact polynomial-time approximability threshold for metric uncapacitated facility location between the $1.463$ hardness and the $1.488$ algorithm.",
  "online-knapsack-unit-density-tight-guarantee": "Determine the tight competitive ratio for unit-density online stochastic knapsack; in particular, prove or refute the conjectured value $(1-e^{-2})/2$.",
  "throughput-scheduling-release-pmax": "Determine whether $1|r_j,p_j\\le c|\\sum U_j$ is polynomial-time solvable for each fixed processing-time bound $c$, and settle the weighted constant-$c$ case.",
  "job-shop-makespan-fpt-as-machines": "Determine whether job-shop makespan admits an FPT approximation scheme parameterized only by the number of machines and $\\epsilon$, without dependence on maximum operations per job.",
  "open-shop-setup-times-fpt-batches": "Determine whether batch/open-shop scheduling with setup times is fixed-parameter tractable in the number of batches alone.",
}


def clean_text(value):
    value = re.sub(r"\\$\\$", " ", str(value or ""))
    value = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def sentences(value):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", value) if s.strip()]


def derive_open_problem(p):
    if p.get("open_problem"):
        return p["open_problem"]
    if p.get("id") in OPEN_OVERRIDES:
        return OPEN_OVERRIDES[p["id"]]
    full = clean_text(p.get("full_statement", ""))
    for label in ("Open Problem:", "Open:", "Question:"):
        idx = full.find(label)
        if idx >= 0:
            tail = full[idx + len(label):].strip()
            return " ".join(sentences(tail)[:2]).strip()
    ss = sentences(full)
    for sent in ss:
        if sent.startswith("Determine "):
            return sent
    for sent in ss[::-1]:
        low = sent.lower()
        if "determine" in low or "whether" in low or "open" in low or "conjecture" in low:
            if len(sent) > 35:
                return sent
    for sent in ss[::-1]:
        if "?" in sent and len(sent) > 35:
            return sent
    return "Resolve the open question stated in the model above."

problems, seen, errors = [], {}, []
for fn,_ in SRC:
    arr = json.load(open(BASE / fn))
    for p in arr:
        miss=[k for k in REQ if not p.get(k)]
        if miss: errors.append(f"{fn}:{p.get('id','?')} missing {miss}")
        wp=p.get("where_posed")
        if not (isinstance(wp,dict) and wp.get("text")): errors.append(f"{fn}:{p.get('id','?')} weak where_posed")
        pid=p.get("id","")
        if pid in seen: errors.append(f"DUP {pid} ({fn} & {seen[pid]}) skipped"); continue
        seen[pid]=fn
        p.setdefault("tags",[]); p.setdefault("additional_refs",[])
        p.setdefault("known_results",""); p.setdefault("confidence","medium")
        problems.append(p)

for i,p in enumerate(problems,1):
    p["number"]=i; p["ref"]=f"ORDOS-{i:03d}"
    p["open_problem"]=derive_open_problem(p)

order=["number","ref","id","title","collection","area","status","confidence","tags",
       "short_statement","open_problem","full_statement","known_results","where_posed","source","additional_refs"]
problems=[{k:p[k] for k in order if k in p} for p in problems]

col=Counter(p["collection"] for p in problems)
area=Counter(p["area"] for p in problems)
st=Counter(p["status"] for p in problems)
cf=Counter(p["confidence"] for p in problems)

# discipline rollup for OR/OM/MS share
disc=Counter()
for p in problems:
    c=p["collection"]
    if c in ("Operations Research","Operations Management","Management Science","Applied Probability"): disc[c]+=1
    elif c.startswith("Online Resource"): disc["Operations Research"]+=1
    else: disc["Algorithms / EC / Market Design"]+=1

out={"metadata":{
   "title":"ORDOS Problems",
   "description":"Crowdsourced open problems in Operations Research, Operations Management, and Management Science (with related market design and online algorithms). Modeled on erdosproblems.com. Each problem has a short statement and a complete, model-level statement suitable for handing to a solver.",
   "generated":datetime.date.today().isoformat(),
   "count":len(problems),
   "collections":dict(col.most_common()),
   "areas":dict(sorted(area.items())),
   "status_breakdown":dict(st),
   "confidence_breakdown":dict(cf),
   "discipline_rollup":dict(disc),
   "schema_version":"2.0"
  },"problems":problems}
json.dump(out,open(ROOT / "problems.json","w"),indent=2,ensure_ascii=False)

print("\nTOTAL:",len(problems))
print("\nBy collection:")
for c,n in col.most_common(): print(f"  {n:3d}  {c}")
print("\nDiscipline rollup:")
for c,n in disc.most_common(): print(f"  {n:3d}  {c}")
print("\nStatus:",dict(st),"| Confidence:",dict(cf))
print("\nISSUES:"); print("\n".join(errors) if errors else "none")
