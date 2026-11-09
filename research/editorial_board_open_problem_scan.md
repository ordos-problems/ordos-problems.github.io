# Editorial-board open-problem scan

Date: 2026-06-21

This note records the first editorial-board-driven curation pass. It is not a claim that every associate editor's full corpus has been exhausted; it is a source trail for the problems added in this pass and for leads that should be revisited.

## Board sources

- Management Science editorial board: https://pubsonline.informs.org/page/mnsc/editorial-board
  - Official page lists the associate editors by department and says it was last updated June 10, 2026.
  - OR/analytics-adjacent AE groups scanned first: Data Science; Market Design, Platform, and Demand Analytics; Operations Management; Optimization and Decision Analytics; Stochastic Models and Simulation.
- Operations Research editorial board: https://pubsonline.informs.org/page/opre/editorial-board
  - Official page lists area editors and associate editors.
  - Priority names from the overlap with the site's scope included Ali Aouad, Santiago Balseiro, Gah-Yi Ban, Hamsa Bastani, Daniel Freund, Negin Golrezaei, Vishal Gupta, Henry Lam, Yash Kanoria, Thodoris Lykouris, Will Ma, Ali Makhdoumi, Vahideh Manshadi, Hongseok Namkoong, Alexandre Proutiere, Dan Russo, Daniela Saban, Cong Shi, Huseyin Topaloglu, Phebe Vayanos, Stefan Wager, Yehua Wei, Cathy Wu, Jiaming Xu, and Zhengyuan Zhou.

## Added in this pass

1. `two-sided-flexibility-random-graph-matching`
   - Source: Daniel Freund, Sebastien Martin, Jiayu Kamessi Zhao, "Two-Sided Flexibility in Platforms", arXiv:2404.04709.
   - Reason for inclusion: clean random bipartite-graph model; the open question is a theorem-level extremal characterization for the expected maximum-matching metric.

2. `contextual-dynamic-pricing-heterogeneous-buyers-k-dependence`
   - Source: Thodoris Lykouris, Sloan Nietert, Princewill Okoroafor, Chara Podimata, Julian Zimmert, "Contextual Dynamic Pricing with Heterogeneous Buyers", arXiv:2512.09513.
   - Reason for inclusion: explicit regret gap in the dependence on latent type support size plus a computational gap for POPS.

3. `new-product-exploration-heterogeneous-priors-assortment`
   - Source: Jackie Baek, Atanas Dinev, Thodoris Lykouris, "Optimal Exploration of New Products under Assortment Decisions", arXiv:2604.18800.
   - Reason for inclusion: existing MNL assortment-learning model is solved for homogeneous priors; heterogeneous priors remain only partially characterized.

4. `battery-market-power-poa-correlated-demand`
   - Source: Jerry Anunrojwong, Santiago R. Balseiro, Omar Besbes, Bolun Xu, "Battery Operations in Electricity Markets: Strategic Behavior and Distortions", arXiv:2406.18685.
   - Reason for inclusion: explicit multi-period covariance-structure question. The two-period jointly normal case already allows arbitrary correlation, and the multi-period independent-normal case is proved. Appendix E gives a partial $T=3$ positive-correlation argument for the upper bound and notes that arbitrary covariance can produce pathological larger PoA values.

5. `optimal-contest-design-gradient-patterns`
   - Source: Negin Golrezaei, MohammadTaghi Hajiaghayi, Suho Shin, "Optimal Contest Beyond Convexity", STOC 2026 / arXiv:2604.04844.
   - Reason for inclusion: explicit structural open problem for optimal rank-based contest policies beyond currently covered gradient patterns.

## Older-paper additions from the second pass

6. `online-monotone-subsequence-second-order-gap`
   - Source: Alessandro Arlotto, Yehua Wei, Xinchang Xie, "An adaptive O(log n)-optimal policy for the online selection of a monotone subsequence from a random sample", Random Structures & Algorithms 2018 / arXiv:1605.03998.
   - Reason for inclusion: older, clean sequential-selection model; first-order asymptotics are known, but the second-order deficit $g(n)=\sqrt{2n}-\mathbb{E}L_n^*$ remains unresolved.

7. `known-iid-online-stochastic-matching-ratio`
   - Source: Vahideh H. Manshadi, Shayan Oveis Gharan, Amin Saberi, "Online Stochastic Matching: Online Actions Based on Offline Statistics", Mathematics of Operations Research 2012 / arXiv:1007.1673.
   - Reason for inclusion: older online matching/ad-allocation model with known i.i.d. arrivals; algorithms beat $1-1/e$, but a substantial constant gap remains to the upper bound.

## Deeper older-paper additions from the third pass

8. `polling-gated-one-limited-pgf`
   - Source: Marko Boon, Onno Boxma, Erik Winands, "On open problems in polling systems", Queueing Systems 2011 / arXiv:1408.0142.
   - Reason for inclusion: explicit old open problem in a standard two-queue polling model. The question is an exact transform/PGF characterization, not a modelling extension.

9. `polling-renewal-large-switchover-limit`
   - Source: Marko Boon, Onno Boxma, Erik Winands, "On open problems in polling systems", Queueing Systems 2011 / arXiv:1408.0142.
   - Reason for inclusion: explicit conjecture for branching-type cyclic polling systems with renewal arrivals in the large switch-over-time limit.

10. `adaptive-polling-limited-service-stability-region`
   - Source: Natalia Chernova, Sergey Foss, Bara Kim, "On the Stability of a Polling System with an Adaptive Service Mechanism", Annals of Operations Research 2012 / arXiv:1105.2069.
   - Reason for inclusion: exact stability region remains unclear in a fixed adaptive limited-service polling model; the paper gives evidence that full primitive distributions may matter.

11. `random-ksat-satisfiability-threshold`
   - Source: Mohsen Bayati, David Gamarnik, Prasad Tetali, "Combinatorial approach to the interpolation method and scaling limits in sparse random graphs", Annals of Probability 2013 / arXiv:0912.2444; with earlier Coppersmith-Gamarnik-Hajiaghayi-Sorkin context.
   - Reason for inclusion: older Gamarnik line of work around random CSP phase transitions. I initially considered the MAX-$k$-SAT limiting-function conjecture, but later interpolation results make that too stale-risky; the exact small-$k$ satisfiability threshold problem is the cleaner still-open formulation.

12. `deletion-channel-small-deletion-capacity-expansion`
   - Source: Yashodhan Kanoria, Andrea Montanari, "Optimal coding for the deletion channel with small deletion probability", IEEE Transactions on Information Theory 2011 / arXiv:1104.5546.
   - Reason for inclusion: clean information-theory model from a board-adjacent scholar's older work; the remaining question is a precise higher-order capacity/asymptotic structure question.

## Fourth pass: older queueing/stability open-problem source

This pass was triggered by the request to search more deeply rather than only reading recent papers by current AEs. I used the Operations Research and Management Science board pages as the seed list, but broadened to older applied-probability/queueing open-problem papers because several board-adjacent areas point back to these classical stability gaps. The additions below come from Sergey Foss, "Some Open Problems Related to Stability", arXiv:0909.0462. They were accepted because each has a fixed mathematical model and a theorem-level target; none asks for a new healthcare/marketplace model.

13. `ggm-fcfs-stationary-ergodic-tv-convergence`
   - Source: Sergey Foss, "Some Open Problems Related to Stability", Section 1.1, arXiv:0909.0462.
   - Reason for inclusion: the stable FCFS $G/G/m$ model and Kiefer-Wolfowitz recursion are fixed; the open question is total-variation convergence under stationary ergodic input alone.

14. `jsq-stationary-ergodic-stability-regimes`
   - Source: Sergey Foss, "Some Open Problems Related to Stability", Section 2, arXiv:0909.0462.
   - Reason for inclusion: join-the-shortest-queue is a canonical load-balancing model; the unresolved issue is existence/uniqueness/convergence of stationary regimes under stationary ergodic primitives, where monotone Loynes machinery fails.

15. `greedy-server-circle-stability`
   - Source: Sergey Foss, "Some Open Problems Related to Stability", Section 3.1, arXiv:0909.0462.
   - Reason for inclusion: continuous-space nearest-neighbor service has a clean Poisson-rain model and a crisp conjecture: stability for every $\lambda<1$.

16. `multiaccess-success-feedback-stable-protocol`
   - Source: Sergey Foss, "Some Open Problems Related to Stability", Section 6, arXiv:0909.0462.
   - Reason for inclusion: slotted random access with only success/non-success feedback is a precise Markov-chain control problem; the unresolved question is whether any positive arrival rate can be stabilized.

17. `supermarket-heavy-traffic-stationary-short-queue-profile`
   - Source: Patrick Eschenfeldt, David Gamarnik, "Supermarket Queueing System in the Heavy Traffic Regime. Short Queue Dynamics", arXiv:1610.03522.
   - Reason for inclusion: the supermarket/JSQ($d$) model is classical, and the paper explicitly conjectures the stationary short-queue profile in the heavy-traffic scaling after proving the transient limiting dynamics and identifying the fixed point. This is a clean interchange-of-limits/stationary-distribution problem, not a modeling question.

18. `gross-substitutes-constructive-description`
   - Source: Eric Balkanski, Renato Paes Leme, "On the Construction of Substitutes", arXiv:1805.03726.
   - Reason for inclusion: gross substitutes are central in economics and market design, the valuation model is fixed, and the paper explicitly identifies the constructive-description problem as a major open problem. The entry is framed around the remaining complete generative representation problem after the negative result for positive combinations of matroid rank functions.

19. `optimal-dynamic-pricing-combinatorial-market-frontier`
   - Source: Ben Berger, Alon Eden, Michal Feldman, "On the Power and Limits of Dynamic Pricing in Combinatorial Markets", arXiv:2002.06863; with Berczi, Berczi-Kovacs, Szogi, "A dual approach for dynamic pricing in multi-demand markets", arXiv:2107.05131 as follow-up progress.
   - Reason for inclusion: the model is a fixed dynamic posted-price implementation problem for welfare maximization over indivisible goods. The source explicitly states that the valuation-domain frontier admitting optimal dynamic prices remains open, and later dual-method work narrows but does not close the frontier.

## Fifth pass: COLT/open-learning problems with OR relevance

This pass broadened beyond INFORMS editorial-board papers into COLT open-problem notes that are directly relevant to sequential decision-making, ranking-and-selection, pricing, experimentation, and recommendation systems. I added only records where the model is already formal and the unresolved target is a theorem-level regret/complexity bound.

20. `contextual-bandit-model-selection-optimal-regret`
   - Source: Dylan Foster, Akshay Krishnamurthy, Haipeng Luo, "Open Problem: Model Selection for Contextual Bandits", arXiv:2006.10940, plus their 2019 model-selection paper and Simchi-Levi-Xu's known-class realizable contextual-bandit reduction.
   - Reason for inclusion: clean nested-model contextual-bandit formulation; the unresolved issue is whether regret can adapt optimally to the smallest correct class instead of paying for the largest class or an extra $T^{2/3}$/$T^{3/4}$ term.

21. `kernelized-bernoulli-bandits-tight-bounds`
   - Source: Marco Mussi, Simone Drago, Alberto Maria Metelli, "Open Problem: Tight Bounds for Kernelized Multi-Armed Bandits with Bernoulli Rewards", arXiv:2407.06321.
   - Reason for inclusion: fixed RKHS bandit model with Bernoulli feedback; the gap is a sharp regret theory, not a new application model. It connects finite-armed Bernoulli/KL bandits, logistic bandits, and additive-noise kernelized bandits.

## Sixth pass: deeper cleanup of older OR/scheduling and stochastic-optimization gaps

This pass responded to the concern that several entries were still too thin. I used the source text of Mnich and van Bevern's Computers & Operations Research open-problem list, rather than relying on short summaries, and expanded weak records where the model and the open parameterized-complexity question were already present.

22. `single-machine-precedence-wct-lp-kernel`
   - Source: Mnich and van Bevern, Open Problem 2 in "Parameterized complexity of machine scheduling: 15 open problems".
   - Reason for inclusion: clean LP-above-lower-bound kernelization question for $1|prec|\\sum w_jC_j$, tied to the Ambuehl-Mastrolilli vertex-cover formulation.

23. `single-machine-throughput-bounded-processing-times`
   - Source: Sgall, "Open problems in throughput scheduling", and Mnich-van Bevern Open Problem 3.
   - Reason for inclusion: fixed release-date throughput model; the unresolved issue is the exact bounded-processing-time complexity frontier, not a modeling choice.

24. `job-shop-makespan-fpt-as-machines`
   - Source: Mnich and van Bevern, Open Problem 13.
   - Action in this pass: expanded statement/model/known-results/verification notes to make explicit that the route-length parameter $n_{\\max}$ must be removed from the non-polynomial running-time dependence.

25. `total-weighted-tardiness-pmax-fpt`
   - Source: Mnich and van Bevern, Open Problem 1; Lawler's pseudo-polynomial dynamic program as partial progress.
   - Action in this pass: rewrote the record around the precise $p_{\\max}$-FPT classification and separated it from pseudo-polynomial dependence on horizon or due-date magnitudes.

26. `uniform-decision-tree-constant-approximation`
   - Source: Li, Liang, and Mussmann, "A Tight Analysis of Greedy Yields Subexponential Time Approximation for Uniform Decision Tree", plus Chawla et al. on correlated Pandora's Box.
   - Reason for inclusion: fixed finite adaptive-testing model with a crisp polynomial-time constant-approximation gap. The problem also connects to stochastic probing/search and correlated Pandora's Box, making it relevant to OR-style adaptive decision-making.

## Seventh pass: source-backed cleanup of online allocation and applied-probability records

This pass did not add new records. It strengthened five existing weak records whose sources were already present but whose formal models and verification guidance were too terse.

27. `matroid-random-order-extends-to-resource-allocation`
   - Sources: Lee and Singla, "Optimal Online Contention Resolution Schemes via Ex-Ante Prophet Inequalities"; Kleinberg and Weinberg on matroid prophet inequalities; Jiang-Ma-Zhang on multi-unit prophet/online stochastic knapsack.
   - Action in this pass: clarified that the random-order $1-1/e$ theorem is matroid-specific, while the broader online resource-allocation extension is a composed open problem from Will Ma's notes rather than a theorem already posed verbatim in Lee-Singla.

28. `adwords-unknown-budgets-optimal-ratio`
   - Source: Rajan Udwani, "Adwords with Unknown Budgets and Beyond".
   - Action in this pass: expanded the unknown-budget feedback model, small-bids qualification, and randomized competitive-ratio verification requirements.

29. `limited-switch-contextual-bandits-with-knapsacks`
   - Sources: Simchi-Levi-Xu-Zhao on limited-switch BwK/NRM; Agrawal-Devanur-Li on contextual BwK; Badanidiyuru-Kleinberg-Slivkins on BwK.
   - Action in this pass: added a full contextual BwK plus switching-budget model and separated minimax/oracle-class/switch-count interpretations.

30. `online-monotone-subsequence-second-order-gap`
   - Sources: Samuels-Steele; Bruss-Delbaen; Arlotto-Wei-Xie.
   - Action in this pass: made the second-order deficit $g(n)=\\sqrt{2n}-\\mathbb E[L_n^*]$ explicit and clarified what a bounded-gap or divergence proof must establish for the true optimal dynamic program.

31. `deletion-channel-small-deletion-capacity-expansion`
   - Sources: Mitzenmacher's deletion-channel survey; Kanoria-Montanari small-deletion expansion papers.
   - Action in this pass: clarified the stationary-input capacity formulation and the need for matching achievability/converse bounds for any new higher-order coefficient.

## Eighth pass: clearing the remaining depth-audit failures

This pass targeted the remaining records whose model statements, known-results sections, or agent verification notes were still too short. It also corrected one stale open-problem status.

32. `polling-gated-one-limited-pgf`
   - Source: Boon, Boxma, Winands, "On open problems in polling systems".
   - Action in this pass: added the full two-queue gated/one-limited model, expanded the branching-property obstruction, and added transform-verification requirements.

33. `polling-renewal-large-switchover-limit`
   - Source: Boon-Boxma-Winands; Winands's Poisson-arrival large-switch-over theorem.
   - Action in this pass: expanded the renewal-arrival fluid-limit statement and clarified what a proof must control about renewal ages and scaling.

34. `mg1-response-time-tail-optimal-scheduling`
   - Source: Grosof, Yang, Scully, Harchol-Balter, "Nudge: Stochastically Improving upon FCFS".
   - Action in this pass: expanded the distinction between mean optimality, asymptotic-tail optimality, stochastic dominance, and high-quantile objectives.

35. `jsq-stationary-ergodic-stability-regimes`
   - Source: Foss, "Some Open Problems Related to Stability".
   - Action in this pass: strengthened the stationary-ergodic JSQ model and clarified why iid/Markovian stability proofs do not settle the problem.

36. `random-spatial-network-length-route-tradeoff`
   - Source: Aldous and Shun, "Connected Spatial Networks over Random Points and a Route-Length Statistic".
   - Action in this pass: expanded the random geometric network model and the distinction between proximity-graph evidence, spanner theory, and a true optimal tradeoff frontier.

37. `real-period-pinwheel-density-threshold`
   - Sources: Kawamura's proof of the integer-period density threshold; Fujiwara-Miyagi-Ouchi on real periods.
   - Action in this pass: clarified that the integer-period conjecture is now solved and that the repository record is about the real-period all-window extension.

38. `closed-form-optimal-policy-general-assembly-systems`
   - Sources: Rosling; Chen-Muharremoglu; Clark-Scarf.
   - Action in this pass: strengthened the remaining problem statement around explicit computation of moving base-stock levels and fixed-ordering-cost structure.

39. `svf-appointment-sequencing`
   - Source: de Kemp, Mandjes, Olver, "Performance of the smallest-variance-first rule in appointment sequencing".
   - Action in this pass: expanded the appointment-time optimization model and switched the primary source to the modern approximation-ratio paper rather than the older SVF conjecture source.

40. `prophet-cancellation-costs-small-buyback`
   - Source: Ekbatani, Niazadeh, Nuti, Vondrak, "Prophet Inequalities with Cancellation Costs".
   - Action in this pass: added related prophet/buyback context and verification requirements for fixed $0<f<1$ claims.

41. `positive-shortest-path-games-pure-stationary-equilibrium`
   - Source: Boros, Elbassioni, Gurvich, Vyalyi, "Two-person positive shortest path games have Nash equilibria in pure stationary strategies".
   - Action in this pass: corrected the stale status. The original two-person pure stationary existence problem is solved; the remaining open problem is the terminal-equilibrium conjecture under mere terminal reachability.

Deferred from the same Foss source:

- Heavy-tailed two-server waiting-time tail asymptotics at integer load.
  - Deferred because Blanchet and Murthy (2015) made substantial progress for the half-loaded $GI/GI/2$ case with regularly varying job sizes. A refined entry may still be appropriate for sharp constants or broader integer-load regimes, but it needs a separate post-2015 status check.
- Three-server partially accessible JSQ-like system where stability may depend on the full distribution.
  - Deferred because the current formulation is still more of a counterexample program than a single clean theorem target for the site.
- Random-fluid-limit polling system with a positive-measure null-recurrence conjecture.
  - Deferred until the exact parameterization and later Foss/Last follow-up literature are checked more carefully.

## Removed from public site

- `battery-market-power-poa-correlated-demand`
  - Disabled after a deeper read. The open direction is real but too narrow and appendix-level for the current repository: the two-period correlated-normal case is already solved, and the remaining issue concerns multi-period covariance structures.

## Ninth pass: deeper source-backed additions beyond keyword "open problem" hits

This pass responded to the criticism that the search was still too shallow. I shifted from recent AE-name keyword searches to older approximation, online-algorithm, fair-allocation, and stochastic-optimization sources where the remaining issue is a formal theorem gap. I added six records, each with a fixed model, current best bounds, and agent verification notes.

42. `random-order-best-fit-bin-packing-ratio`
   - Source: Hebbar, Khan, Sreenivas, "Bin Packing under Random-Order: Breaking the Barrier of 3/2", SODA 2024 / arXiv:2401.04714.
   - Reason for inclusion: fixed Best-Fit algorithm, adversarial multiset plus random arrival order, and a long-standing exact constant gap between the $1.144$ lower bound and the best upper bound below $1.5$.

43. `submodular-facility-location-constant-approximation`
   - Source: Abbasi, Adamczyk, Bosch-Calvo, Byrka, Grandoni, Sornat, Tinguely, "An O(loglog n)-Approximation for Submodular Facility Location", arXiv:2211.05474.
   - Reason for inclusion: clean facility-location generalization with monotone submodular opening costs; the open problem is whether the current $O(\log\log n)$ approximation can be made constant.

44. `steiner-forest-below-two`
   - Source: Byrka, Grandoni, Traub, "On the Bidirected Cut Relaxation for Steiner Forest", arXiv:2412.06518.
   - Reason for inclusion: classic network-design approximation gap; the factor-2 primal-dual barrier has not been beaten for general Steiner Forest.

45. `online-steiner-forest-greedy-ratio`
   - Source: Bamas, Drygala, Maggiori, "An Improved Analysis of Greedy for Online Steiner Forest", SODA 2022 / arXiv:2111.10086.
   - Reason for inclusion: fixed online greedy algorithm with an $O(\log^2 k)$ classical analysis, improved partial analysis, and an unresolved $O(\log k)$ versus superlogarithmic frontier.

46. `generic-budget-ce-additive-goods`
   - Source: Babaioff, Nisan, Talgam-Cohen, "Competitive Equilibrium with Indivisible Goods and Generic Budgets", Mathematics of Operations Research 2021 / arXiv:1703.08150; Segal-Halevi, "Competitive Equilibrium For Almost All Incomes", AAMAS 2020 / arXiv:1705.04212.
   - Reason for inclusion: parsimonious market-design model with additive valuations over indivisible goods; the unresolved frontier is the almost-everywhere existence characterization, especially broad additive regimes.

47. `stochastic-probing-subadditive-adaptivity-gap`
   - Source: Li, Liu, Zhang, "Adaptivity Gaps for Stochastic Probing with Subadditive Functions", FOCS 2025 / arXiv:2504.15547.
   - Reason for inclusion: stochastic probing is a standard adaptive stochastic-optimization model; recent work leaves a concrete asymptotic gap for general subadditive Bernoulli probing.

## Tenth pass: supply-chain, game-complexity, and SDP-gap additions

This pass continued the deeper search after filtering out duplicates already covered by the dataset (unrelated-machine makespan, fully online matching, subadditive prophet inequalities, and fixed-budget best-arm identification). I added three records where the model is fixed and the remaining gap is a theorem-level algorithmic or integrality-gap question.

48. `joint-replenishment-approximation-ratio`
   - Sources: Bienkowski, Byrka, Chrobak, Jez, Sgall, "Better Approximation Bounds for the Joint Replenishment Problem", arXiv:1307.2531; Bienkowski et al., "Approximation Algorithms for the Joint Replenishment Problem with Deadlines", Journal of Scheduling 2015 / arXiv:1212.3233; Segev, "Improved Approximation Guarantees for Joint Replenishment in Continuous Time", Mathematics of Operations Research 2025 / arXiv:2408.05443.
   - Reason for inclusion: this is a classical supply-chain/inventory optimization problem with explicit approximation constants and LP gaps; it is more concrete than the broader one-warehouse stochastic policy-structure record.

49. `mean-payoff-games-polynomial-time`
   - Source: Allamigeon, Benchimol, Gaubert, Joswig, "Combinatorial simplex algorithms can solve mean payoff games", SIAM Journal on Optimization 2014 / arXiv:1309.5925.
   - Reason for inclusion: fixed finite two-player infinite-horizon game with positional strategies and $NP \cap coNP$ membership; the open problem is the exact polynomial-time complexity.

50. `goemans-linial-sparsest-cut-gap`
   - Source: Kane and Meka, "A PRG for Lipschitz Functions of Polynomials with Applications to Sparsest Cut", STOC 2013 / arXiv:1211.1109.
   - Reason for inclusion: fixed SDP relaxation and fixed uniform Sparsest Cut model; the unresolved issue is the asymptotic integrality gap between known lower bounds and ARV-type upper bounds.

## Eleventh pass: capacitated clustering, lattice FPP, and worst-case dense-subgraph approximation

This pass targeted underrepresented theorem gaps that were not already covered by the existing metric $k$-median, planted-structure, or random-spatial-network records. I rejected several leads that were either already in the dataset or were primarily model-extension questions. Three additions survived the duplicate and status checks.

51. `capacitated-k-median-constant-approximation`
   - Sources: Adamczyk, Byrka, Marcinkowski, Meesum, Wlodarczyk, "Constant factor FPT approximation for capacitated k-median", APPROX/RANDOM 2019 / arXiv:1809.05791; Li, "On Uniform Capacitated k-Median Beyond the Natural LP Relaxation", TALG 2016 / arXiv:1409.6739; Cohen-Addad and Li, "On the Fixed-Parameter Tractability of Capacitated Clustering", arXiv:2208.14129.
   - Reason for inclusion: fixed hard-capacitated metric clustering model; FPT constant approximations and bicriteria algorithms exist, but the polynomial-time constant approximation without capacity/cardinality violation remains open.

52. `first-passage-percolation-variance-exponent`
   - Sources: Auffinger, Damron, Hanson, "50 years of first passage percolation", AMS University Lecture Series 2017 / arXiv:1511.03262; Benjamini, Kalai, Schramm, "First Passage Percolation Has Sublinear Distance Variance", Annals of Probability 2003; Basu, Sidoravicius, Sly, "Rotationally invariant first passage percolation: Breaking the n/log n variance barrier", arXiv:2604.01214.
   - Reason for inclusion: canonical applied-probability/stochastic-shortest-path model; recent continuous-model progress changes the context but leaves the ordinary lattice FPP polynomial-variance problem open.

53. `densest-k-subgraph-approximation`
   - Sources: Bhaskara, Charikar, Chlamtac, Feige, Vijayaraghavan, "Detecting High Log-Densities -- an O(n^1/4) Approximation for Densest k-Subgraph", STOC 2010 / arXiv:1001.2891; Manurangsi, "Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph", STOC 2017 / arXiv:1611.05991; Jones, Potechin, Rajendran, Xu, "Sum-of-Squares Lower Bounds for Densest k-Subgraph", arXiv:2303.17506.
   - Reason for inclusion: distinct from the existing planted-structure entry because this is the worst-case approximation problem; the $n^{1/4}$ algorithmic benchmark and hardness evidence still do not meet.

## Twelfth pass: convex sampling, information theory, POMDP planning, stochastic games, and integer-programming geometry

This pass responded to the concern that the previous additions were still too close to local search hits. I broadened the search to older durable gaps in probability/optimization/information theory and to COLT-style open problems that intersect OR through stochastic control and sampling. I rejected the unrelated-machine $R||C_{\max}$ lead because it is already in the dataset.

54. `kls-log-concave-isoperimetry-constant`
   - Sources: Kannan, Lovasz, Simonovits, "Isoperimetric problems for convex bodies and a localization lemma", Discrete & Computational Geometry 1995; Chen, "An Almost Constant Lower Bound of the Isoperimetric Coefficient in the KLS Conjecture", GAFA 2021 / arXiv:2011.13661; Chen and Eldan, "Hit-and-run mixing via localization schemes", arXiv:2212.00297.
   - Reason for inclusion: canonical applied-probability/convex-optimization conjecture with a fixed log-concave model; the gap is now almost constant but still not dimension-free.

55. `graph-shannon-capacity-odd-cycles`
   - Sources: Shannon, "The zero error capacity of a noisy channel", IRE Transactions on Information Theory 1956; Lovasz, "On the Shannon capacity of a graph", IEEE Transactions on Information Theory 1979; Alon and Lubetzky, "The Shannon capacity of a graph and the independence numbers of its powers", IEEE Transactions on Information Theory 2006 / arXiv:cs/0608021; Mathew and Ostergard, "New Lower Bounds for the Shannon Capacity of Odd Cycles", Designs, Codes and Cryptography 2015 / arXiv:1504.01472.
   - Reason for inclusion: clean asymptotic combinatorial optimization invariant; even $C_7$ remains unresolved and finite-prefix methods provably cannot settle the general problem.

56. `pomdp-memoryless-policy-planning`
   - Sources: Azizzadenesheli, Lazaric, Anandkumar, "Open Problem: Approximate Planning of POMDPs in the class of Memoryless Policies", COLT 2016 / arXiv:1608.04996; Smallwood and Sondik, "The optimal control of partially observable Markov processes over a finite horizon", Operations Research 1973; Muller and Montufar, "The Geometry of Memoryless Stochastic Policy Optimization in Infinite-Horizon POMDPs", arXiv:2110.07409.
   - Reason for inclusion: fixed finite POMDP model and fixed memoryless stochastic policy class; the missing piece is a global exact or approximation algorithm, not a new application model.

57. `simple-stochastic-games-polynomial-time`
   - Sources: Condon, "The complexity of stochastic games", Information and Computation 1992; Ludwig, "A subexponential randomized algorithm for the simple stochastic game problem", Information and Computation 1995; Gimbert and Horn, "Solving Simple Stochastic Games with Few Random Vertices", arXiv:0712.1765; Rudich, Rudich, Rue, "Simple Stochastic Stopping Games: A Generator and Benchmark Library", arXiv:2402.02571.
   - Reason for inclusion: foundational finite stochastic-game model with positional strategies and practical algorithms; polynomial-time solvability is still open.

58. `flatness-constant-integer-programming`
   - Sources: Kannan, "Minkowski's convex body theorem and integer programming", Mathematics of Operations Research 1987; Kannan and Lovasz, "Covering minima and lattice-point-free convex bodies", Annals of Mathematics 1988; Mayrhofer, Schade, Weltge, "Lattice-free simplices with lattice width 2d - o(d)", arXiv:2111.08483; Reis and Rothvoss, "The Subspace Flatness Conjecture and Faster Integer Programming", arXiv:2303.14605.
   - Reason for inclusion: old OR/integer-programming geometry problem with direct algorithmic consequences; the open gap is $2d-o(d)$ versus $O(d\log^3 d)$ for the flatness constant.

## Thirteenth pass: geometric routing, clustering, and low-dimensional discrepancy

This pass added three non-duplicate problems after rejecting randomized metrical task systems as already essentially settled in the existing randomized $k$-server entry. The emphasis was on clean OR/data-mining/discrepancy models where the current literature has strong partial progress but a sharp theorem gap.

59. `euclidean-cvrp-ptas-arbitrary-capacity`
   - Sources: Das and Mathieu, "A quasi-polynomial time approximation scheme for Euclidean capacitated vehicle routing", Algorithmica 2015 / arXiv:0812.1595; Jayaprakash and Salavatipour, "Approximation Schemes for Capacitated Vehicle Routing on Graphs of Bounded Treewidth, Bounded Doubling, or Highway Dimension", arXiv:2106.15034; Sitters, "An n^{O(log log n)} time approximation scheme for capacitated VRP in the Euclidean plane", arXiv:2507.15549.
   - Reason for inclusion: core geometric vehicle-routing problem with arbitrary capacity; QPTAS results are known, but the Euclidean PTAS remains open.

60. `correlation-clustering-complete-graph-threshold`
   - Sources: Bansal, Blum, Chawla, "Correlation Clustering", Machine Learning 2004; Cohen-Addad, Lee, Li, Newman, "Handling Correlated Rounding Error via Preclustering", FOCS 2023 / arXiv:2309.17243; Cao, Cohen-Addad, Lee, Li, Newman, Vogl, "Understanding the Cluster LP for Correlation Clustering", arXiv:2404.17509.
   - Reason for inclusion: fixed complete signed-graph clustering objective with practical data-mining relevance; the best current approximation, cluster-LP gap, and hardness ratio remain separated.

61. `tusnady-low-dimensional-box-discrepancy`
   - Sources: Beck, "Balanced two-colorings of finite sets in the square", Combinatorica 1981; Nikolov, "Tighter Bounds for the Discrepancy of Boxes and Polytopes", Mathematika 2017 / arXiv:1701.05532; Bansal and Garg, "Algorithmic Discrepancy Beyond Partial Coloring", STOC 2017 / arXiv:1611.01805; Dutta, "On Shallow Packings and Tusnady's Problem", arXiv:2109.05693.
   - Reason for inclusion: canonical geometric-discrepancy problem; recent work settles $d\ge5$ but leaves concrete logarithmic gaps in dimensions 2, 3, and 4.

## Fourteenth pass: older approximation, mechanism-design, and game-complexity gaps

This pass responded to the criticism that the search was still too shallow. I deliberately moved away from only recent INFORMS-board papers and checked older approximation-algorithm and algorithmic-game-theory sources where the unresolved issue is a durable theorem gap. I also rejected stale framings: for example, "beat factor 2 for weighted tree augmentation" is no longer a correct open problem after Traub-Zenklusen and follow-up work, so the added record is framed around the current threshold/LP-gap question instead.

62. `truthful-submodular-combinatorial-auctions`
   - Sources: Assadi-Singla, "Improved Truthful Mechanisms for Combinatorial Auctions with Submodular Bidders", arXiv:1911.02716; Dobzinski's 2016 logarithmic-barrier paper; Dobzinski's value-query impossibility result.
   - Reason for inclusion: clean welfare-maximization model with fixed submodular valuations and incentive constraints. The current best truthful mechanism is $O((\log\log m)^3)$, while constant-factor truthfulness remains a major mechanism-design frontier.

63. `parity-games-polynomial-time`
   - Sources: Jurdzinski, "Deciding the winner in parity games is in UP intersect co-UP"; Calude-Jain-Khoussainov-Li-Stephan on quasi-polynomial time; Fearnley-Jain-Schewe-Stephan-Wojtczak on quasi-polynomial implementation.
   - Reason for inclusion: canonical finite two-player game with memoryless strategies, $UP\cap coUP$ membership, and quasi-polynomial algorithms. The open question is exact polynomial-time solvability, not a modeling issue.

64. `capacitated-facility-location-relaxation-gap`
   - Sources: Kolliopoulos-Moysoglou, "Integrality gaps for strengthened LP relaxations of Capacitated and Lower-Bounded Facility Location"; their Sherali-Adams/flow-cover follow-up; Chudak-Williamson approximation background.
   - Reason for inclusion: classic OR/facility-location problem where constant combinatorial approximations exist, but the Shmoys-Williamson relaxation-based open problem remains unresolved after strong negative evidence for natural LP families.

65. `weighted-tree-augmentation-threshold`
   - Sources: Traub-Zenklusen 2021 weighted tree augmentation papers; Cohen-Addad-Drygala-Klein-Svensson, "A Strong Linear Programming Relaxation for Weighted Tree Augmentation", arXiv:2603.29582; Kortsarz-Nutov's older LP-framing paper.
   - Reason for inclusion: tree augmentation is a minimal survivable-network-design model. The old factor-2 question has been solved, but the exact threshold and strong-relaxation gap around the $1.5$ frontier remain open and machine-checkable through finite tree-link instances.

66. `minimum-feedback-arc-set-constant-approximation`
   - Sources: Even-Naor-Schieber-Sudan, "Approximating Minimum Feedback Sets and Multicuts in Directed Graphs"; Kenyon-Mathieu-Schudy's tournament PTAS; Guruswami-Manokaran-Raghavendra Unique-Games hardness evidence.
   - Reason for inclusion: fixed directed-graph ordering/cycle-breaking problem with applications to ranking and deadlock/circuit analysis. General directed FAS still has a qualitative gap between polylogarithmic algorithms, constant-factor hardness under standard assumptions, and UGC-based no-constant evidence.

## Fifteenth pass: directed network design and cut/metric-relaxation gaps

This pass continued the deeper search through durable approximation-theory problems with strong OR/network-design relevance. I explicitly checked the apparent 2024 Directed Steiner Tree "polylog in polynomial time" lead and found the arXiv record currently marks that version as withdrawn/proof-collapsed, so the entry below treats the general polynomial-time polylogarithmic question as still open and cites the reliable quasi-polynomial and planar-special-case literature.

67. `directed-steiner-tree-polylog-approximation`
   - Sources: Chekuri, Jain, Kulkarni, Zheng, Zhu, "From Directed Steiner Tree to Directed Polymatroid Steiner Tree in Planar Graphs", arXiv:2407.01904; Grandoni-Laekhanukit-Li and Ghuge-Nagarajan quasi-polynomial algorithms.
   - Reason for inclusion: canonical directed network-design model. Quasi-polynomial algorithms achieve $O(\log^2 k/\log\log k)$ and planar digraphs admit polynomial-time polylogarithmic algorithms, but the arbitrary directed-graph polynomial-time polylogarithmic question remains open.

68. `zero-extension-integrality-gap`
   - Sources: Schwartz and Tur, "The Metric Relaxation for 0-Extension Admits an Omega(log^{2/3} k) Gap", STOC 2021 / arXiv:2104.11670; Chen and Tan, "Lower Bounds on 0-Extension with Steiner Nodes", arXiv:2401.09585; Calinescu-Karloff-Rabani and Fakcharoenphol-Harrelson-Rao-Talwar.
   - Reason for inclusion: fixed metric-labeling/graph-compression model with a clean gap between $O(\log k/\log\log k)$ rounding and $\Omega((\log k)^{2/3})$ lower bounds; also tied to vertex sparsifier open problems.

69. `multiway-cut-approximation-threshold`
   - Sources: Berczi, Chandrasekaran, Kiraly, Madan, "Improving the Integrality Gap for Multiway Cut", arXiv:1807.09735; Calinescu-Karloff-Rabani; Sharma-Vondrak; Angelidakis-Makarychev-Manurangsi.
   - Reason for inclusion: classical graph-cut problem with a precise numerical approximation gap: best algorithm $1.2965$, hardness/integrality evidence just above $1.2$, and finite CKR-gap instances that are suitable for machine verification.

## Sixteenth pass: deeper theorem-gap sweep after duplicate audit

This pass followed the complaint that the search was still too shallow. I broadened beyond literal "open problem" keyword hits and looked for durable gaps in older OR-adjacent theory: routing, graph partitioning, stochastic networks, and survivable network design. I also ran a duplicate check against the active corpus before merging; the strongest rejected duplicate was the unknown-budget AdWords problem, which is already present as `adwords-unknown-budgets-optimal-ratio`.

70. `metric-tsp-approximation-threshold`
   - Sources: Karlin-Klein-Oveis Gharan, "A (Slightly) Improved Approximation Algorithm for Metric TSP", STOC 2021 / arXiv:2007.01409; their deterministic follow-up; Karpinski-Lampis-Schmied hardness.
   - Reason for inclusion: the existing dataset has the Held-Karp $4/3$ integrality-gap conjecture, but not the top-level computational approximation-threshold question. This is a canonical OR routing problem where the $3/2$ barrier has only been beaten by a tiny constant and hardness is still barely above 1.

71. `sparsest-cut-approximation-threshold`
   - Sources: Kolmogorov's simplified/parallelizable $O(\sqrt{\log n})$ algorithm; Naor-Young's matching Goemans-Linial SDP gap; Khot-Vishnoi and Arora-Lee-Naor metric-embedding papers.
   - Reason for inclusion: the existing dataset has the fixed Goemans-Linial SDP gap problem; this entry asks the broader computational question of whether arbitrary polynomial-time algorithms can beat $O(\sqrt{\log n})$ or whether matching hardness exists.

72. `queueing-network-stability-clean-undecidability`
   - Sources: Gamarnik-Katz, "On deciding stability of multiclass queueing networks under buffer priority scheduling policies", arXiv:0708.1034 / Mathematics of Operations Research; Dai and Bramson fluid-model papers.
   - Reason for inclusion: a clean applied-probability/queueing conjecture from older OR literature. Undecidability is proved for a broader model, and the open target is whether it persists for the more standard infinite-buffer, strictly-positive-service setting.

73. `forest-augmentation-approximation-threshold`
   - Sources: Grandoni-Jabal Ameli-Traub, "Breaching the 2-Approximation Barrier for the Forest Augmentation Problem", arXiv:2112.11799; Jain's generalized Steiner network 2-approximation; Traub-Zenklusen weighted tree augmentation.
   - Reason for inclusion: basic survivable network design problem with a fixed model. The factor-2 barrier has been breached, but the actual approximation threshold and matching hardness/integrality-gap story remain open.

## Seventeenth pass: game-theory, random-metric, and flow-cut conjectures

This pass continued screening older theorem-gap sources rather than relying on recent keyword hits. I rejected several stale leads whose search snippets said "open" but whose status is now solved, including directed multicut with three terminal pairs. Three additions survived duplicate checks against the active corpus.

74. `bimatrix-approximate-nash-threshold`
   - Sources: Deligkas-Fasoulakis-Markakis, "A Polynomial-Time Algorithm for 1/3-Approximate Nash Equilibria in Bimatrix Games", arXiv:2204.11525; Rubinstein's PPAD-ETH lower bound; Chen-Deng-Teng exact PPAD-completeness.
   - Reason for inclusion: clean finite normal-form game model at the economics/CS boundary. The current polynomial-time guarantee is $1/3+\delta$, while hardness is known only for some smaller constant under strong PPAD assumptions.

75. `fpp-bigeodesics-nonexistence`
   - Sources: Damron-Hanson, "Bigeodesics in first-passage percolation", arXiv:1512.00804; Ahlberg-Hoffman random coalescing geodesics; Brito-Damron-Hanson backward-infinite-path results; Auffinger-Damron-Hanson survey.
   - Reason for inclusion: fixed i.i.d. random metric model with a famous conjecture and substantial partial progress. This complements the existing FPP variance entry by focusing on geodesic geometry rather than fluctuation scale.

76. `minor-free-flow-cut-gap-gnrs`
   - Sources: Salmasi-Sidiropoulos-Sridhar, "On constant multi-commodity flow-cut gaps for directed minor-free graphs", arXiv:1711.01370; Chekuri-Shepherd-Weibel integer/fractional multiflow gaps; Lee-Sidiropoulos pathwidth/minor-closed embedding progress.
   - Reason for inclusion: foundational multicommodity-routing and metric-embedding conjecture with direct network-design relevance. It is distinct from the Sparsest Cut approximation-threshold entry because the supply graph is restricted to fixed-minor-free families and the target is a constant flow-cut gap.

## Deferred leads

- Eighteenth-pass stale/modeling rejections:
  - Directed multicut with three terminal pairs was rejected because later work appears to resolve the older open-status framing.
  - Several dynamic-pricing, inventory, and assortment hits were rejected because the unresolved item was mainly a richer application model or a recently solved special case rather than a durable theorem gap.
  - The EFX-for-chores lead was not re-added because the active `efx-chores` record already reflects the June 2026 three-agent additive-chores development.
  - The unknown-budget AdWords and fully-online matching leads were not re-added because the active corpus already contains those problems.

- `adwords-unknown-budgets-tight-ratio`
  - Deferred because it is already covered by the active record `adwords-unknown-budgets-optimal-ratio`; the new draft was deleted after duplicate audit.

- Negin Golrezaei and Sourav Sahoo, "Learning Safe Strategies for Value Maximizing Buyers in Uniform Price Auctions", arXiv:2406.03674.
  - Deferred because the conclusion mostly points to richer auction formats, budget-plus-RoI constraints, and equilibrium dynamics. These are useful leads, but the current open questions are closer to model extension than to a single clean theorem gap.

- Yan Dai, Negin Golrezaei, Patrick Jaillet, "Policy Regret for Embedding Model Routing: Contextual Bandits with Low-Rank Experts", arXiv:2606.14929.
  - Deferred because the open problem is real but currently tied to a very new LLM-routing formulation. Revisit if the repository wants a section on modern contextual bandit problems for foundation-model systems.

- Omar Besbes, Yash Kanoria, Akshit Kumar, "Impact of Rankings and Personalized Recommendations in Marketplaces", arXiv:2506.03369.
  - Deferred because it is a good technical gap on general distributional assumptions for capacitated marketplaces, but it is authored by the site owner; add only if you want your own open problem included.

- William Overman and Mohsen Bayati, "Annealed Softmax Greedy in Many-Armed Bayesian Bandits", arXiv:2605.31034.
  - Deferred because the open question is broad: characterize the boundary where upper-tail abundance makes uncertainty-agnostic reweighting effective.

- Jiaming Xu / Hajek-Oh-Xu, "Minimax-optimal Inference from Partial Rankings", arXiv:1406.5638.
  - Deferred because the visible gap is mostly logarithmic/statistical-design sharpness, and the conclusion did not present a clean unresolved problem at the same level as the polling or matching entries.

- Yash Kanoria et al., bargaining dynamics in exchange networks, arXiv:0911.1767 and arXiv:1004.2079.
  - Deferred for now. There are interesting open questions about asynchronous updates and exact computation in unsymmetric bargaining, but the repository already has several market-design/game-theory entries and this needs a separate check against later exchange-network literature.

- Proutiere and coauthors on stochastic online shortest-path routing and unimodal/Lipschitz bandits.
  - Deferred because the scanned papers mostly solve the stated lower-bound gaps; any remaining general-topology issues looked more like algorithm-extension leads than clean open problems.

## Notes for the next pass

- The arXiv scan was throttled after the first wave of authors. A serious second pass should continue through the remaining Operations Research AEs and broaden to Management Science departments beyond the OR-heavy groups.
- The best search terms were not just "open problem"; theorem-gap searches such as "lower bound", "upper bound", "conjecture", "remains open", "tight", and "optimal dependence" found better candidates.
- Avoid adding entries whose main unresolved issue is choosing a better real-world model. The repository standard should remain: a clean existing model, an identifiable hard question, and known partial results.

## Eighteenth pass: geometric network optimization and exposition cleanup

This pass continued the deeper search for older theorem-level gaps while also auditing records where the short card text duplicated the formal open problem. The strongest new survivor was a geometric network-design conjecture rather than a recent editorial-board paper: it has a clean finite model, a famous sharp constant, a documented flawed-proof history, and a recent AI-assisted lower-bound paper.

77. `gilbert-pollak-steiner-ratio`
   - Sources: Gilbert and Pollak, "Steiner Minimal Trees", SIAM Journal on Applied Mathematics 1968; Du and Hwang's claimed proof in PNAS 1990; Innami-Kim-Mashiko-Shiohama and Ivanov-Tuzhilin clarification papers in Algorithmica; Ke-Huang-Shu-He-Gai-Wang, "Towards Solving the Gilbert-Pollak Conjecture via Large Language Models", arXiv:2601.22365.
   - Reason for inclusion: fixed Euclidean network-design model with a sharp constant conjecture, not a modeling problem. The recent AI-assisted paper reports a certified lower bound of 0.8559 for `SMT/MST`, while the conjectured value is `sqrt(3)/2`.

78. `single-machine-forbidden-times-fpt`
   - Action in this pass: exposition cleanup rather than a new problem. The old short statement was essentially the open problem itself, so the card now states the context: fixed-`tau` polynomial algorithms are known but the exponent depends on `tau`; the detail page still asks the formal FPT-vs-hardness question.

## Nineteenth pass: exact numerical comparison for geometric optimization

This pass followed a geometric-optimization thread after the Gilbert-Pollak entry. Several search hits around minimum-weight triangulation were useful but too broad to add directly as a modeling entry: NP-hardness is known, QPTAS-style approximation is known, and the clean unresolved core is the exact comparison of Euclidean lengths. I therefore added the underlying fixed numerical-complexity problem rather than duplicating a triangulation article.

79. `square-root-sum-polynomial-time`
   - Sources: Eisenbrand-Haeberle-Singer, "An improved bound on sums of square roots via the subspace theorem", arXiv:2312.02057; Allender-Burgisser-Kjeldgaard-Pedersen-Miltersen, "On the Complexity of Numerical Analysis", SIAM Journal on Computing 2009; Cheng-Meng-Sun-Chen, "Bounding the Sum of Square Roots via Lattice Reduction", Mathematics of Computation 2010.
   - Reason for inclusion: finite integer input, crisp Turing-model question, and direct relevance to exact Euclidean optimization problems where objective values are sums of radicals. This is not a modeling problem; it asks whether a fully specified arithmetic comparison problem has a polynomial-time algorithm.

80. `metric-tsp-four-thirds-integrality-gap`
   - Action in this pass: exposition cleanup rather than a new problem. The old entry had good citations but a short formal model and a thin verification checklist. The enrichment now spells out the subtour LP constraints and what an agent/referee must certify for a counterexample or a universal rounding proof.

Deferred in this pass:

- Minimum-weight triangulation as a standalone entry was deferred because the clean durable unresolved core found in the sweep is the square-root-sum exact-comparison issue. A separate MWT entry may still be worthwhile later if framed around exact NP membership or the PTAS-vs-QPTAS frontier with verified primary sources.
- Queueing with predictions/LLM scheduling was deferred because the open questions are interesting but currently look closer to emerging model formulation than to the repository's fixed-model theorem-gap standard.
