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

## Removed from public site

- `battery-market-power-poa-correlated-demand`
  - Disabled after a deeper read. The open direction is real but too narrow and appendix-level for the current repository: the two-period correlated-normal case is already solved, and the remaining issue concerns multi-period covariance structures.

## Deferred leads

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
