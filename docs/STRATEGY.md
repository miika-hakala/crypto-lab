# Strategy — crypto-lab

**Version:** 1.0
**Last Updated:** 2026-02-16
**Status:** Active

---

## Vision

Determine the **profitability potential** of our GPU cluster through systematic experimentation, automation, and data-driven optimization — with a clear exit strategy if returns are negative.

---

## Non-Goals

This project explicitly **does not** aim to:
- ❌ Replace primary GPU cluster use (Ollama/AI workloads)
- ❌ Become a permanent mining operation
- ❌ Guarantee positive ROI
- ❌ Provide investment advice
- ❌ Compete with industrial mining operations

---

## Core Assumptions

1. **GPU availability is opportunistic** — mining only when GPUs are idle
2. **Electricity cost is fixed** — cluster runs regardless of mining
3. **Solar integration is future possibility** — optimize for excess capacity
4. **Time-to-market matters** — iterate quickly, validate assumptions
5. **Exit if negative** — no sunk cost fallacy, shut down if unprofitable

---

## Strategic Phases

### Phase 1: Discovery ✅ COMPLETE
**Duration:** 1-2 days
**Goal:** Understand baseline profitability and hardware capabilities

**Activities:**
- [x] Hardware inventory and specifications
- [x] Initial profitability analysis (paper ranking)
- [x] Multi-algorithm benchmarking
- [x] Power consumption measurement
- [x] Thermal characterization

**Deliverables:**
- [x] Benchmark report with top algorithms
- [x] Power/thermal profiles per GPU
- [x] Initial ROI estimates

**Key Findings:**
- RTX 3060: Best overall performance (4/5 algorithms)
- GTX 1660 SUPER: Limited by VRAM (6GB constraint)
- Pyrin algorithm: Highest efficiency (27.8 MH/W)
- All temperatures stable (<75°C)

**Exit Criteria Met:** ✅ Positive efficiency indicators justify Phase 2

---

### Phase 2: Automation 🔄 IN PROGRESS
**Duration:** 1-2 weeks
**Goal:** Build automated profitability monitoring and switching logic

**Objectives:**
1. **Profitability Runner:**
   - Automated API data fetching (WhatToMine, CoinWarz, etc.)
   - Real-time profitability calculation
   - Historical trend analysis
   - Daily/weekly reports

2. **Benchmark Engine:**
   - On-demand algorithm benchmarking
   - Hashrate verification vs pool stats
   - Power consumption tracking
   - Thermal monitoring

3. **Algorithm Switcher (MVP):**
   - Manual coin selection
   - Single-GPU deployment
   - Profit tracking vs baseline
   - 72h test runs

**Success Criteria:**
- [ ] Automated daily profitability reports
- [ ] Successful 72h test run on top algorithm
- [ ] Actual earnings data collected
- [ ] ROI calculation framework validated

**Exit Criteria:**
- If 72h test shows **negative ROI** after electricity → abort Phase 3
- If technical complexity exceeds value → simplify or exit

---

### Phase 3: Optimization 📋 PLANNED
**Duration:** 2-4 weeks
**Goal:** Maximize returns through intelligent automation

**Planned Features:**

1. **Dynamic Algorithm Switching:**
   - Auto-detect most profitable algorithm
   - Switch between coins/pools automatically
   - Minimize downtime during switches
   - Track switching overhead

2. **Solar-Aware Scheduling:**
   - Monitor solar production (if available)
   - Mine during excess solar capacity
   - Reduce mining during grid hours
   - Calculate carbon-neutral mining windows

3. **Multi-Pool Management:**
   - Failover to backup pools
   - Compare pool profitability
   - Optimize for payout frequency
   - Minimize pool fees

4. **Performance Dashboard:**
   - Real-time monitoring UI
   - Historical charts (hashrate, earnings, efficiency)
   - Alert system for anomalies
   - Mobile notifications

**Success Criteria:**
- [ ] Automatic switching reduces manual intervention to <1hr/week
- [ ] Solar integration improves net profitability by >20%
- [ ] Dashboard provides actionable insights
- [ ] System runs stable for 30+ days

**Exit Criteria:**
- If automation complexity costs more than gains → revert to manual
- If sustained negative ROI → project termination

---

### Phase 4: Scale (Conditional) ⏸️ ON HOLD
**Prerequisites:** Phase 3 success + sustained positive ROI

**Potential Expansions:**
- Additional GPU nodes
- Dedicated mining hardware evaluation
- Pool hosting exploration
- Community mining coordination

**Note:** Phase 4 only proceeds if:
1. Phases 1-3 demonstrate clear profitability
2. Infrastructure capacity allows expansion
3. Regulatory environment remains favorable
4. Human resources available for maintenance

---

## Strategic Priorities

### Priority 1: Data-Driven Decisions
- Collect objective metrics at every phase
- Compare estimates vs actuals rigorously
- Pivot based on evidence, not assumptions
- Document all findings for future reference

### Priority 2: Minimize Complexity
- Start simple, add features only when proven necessary
- Avoid over-engineering
- Prefer manual steps over buggy automation
- Technical debt is acceptable if project is exploratory

### Priority 3: Security First
- Never compromise cluster security for mining
- Wallet management stays off-cluster
- No root-level modifications
- All changes reversible

### Priority 4: Respect Primary Mission
- GPU cluster's primary purpose: AI/ML workloads (Ollama)
- Mining is opportunistic secondary use
- If mining interferes with primary use → mining stops
- Thermal/power budgets must not degrade primary performance

---

## Key Metrics (KPIs)

### Financial:
- **Daily Revenue (USD):** Actual earnings from mining
- **Electricity Cost (USD/day):** Power consumption cost
- **Net Profit (USD/day):** Revenue - Electricity
- **ROI Percentage:** (Net Profit / Initial Investment) × 100
- **Break-Even Timeline:** Days until cumulative profit > 0

### Technical:
- **Average Hashrate:** Per algorithm, per GPU
- **Uptime Percentage:** Mining time / available time
- **Efficiency (MH/W):** Hashrate per watt consumed
- **Temperature (°C):** Average and peak per GPU
- **Rejected Shares (%):** Network communication quality

### Operational:
- **Manual Intervention Hours:** Time spent managing mining
- **Incidents Count:** Crashes, thermal events, errors
- **Algorithm Switches:** Frequency and reasons
- **Experiment Velocity:** Tests completed per week

---

## Decision Framework

### Go/No-Go Criteria

**Continue if:**
- ✅ Net profit > $0/day (after electricity)
- ✅ System stability >95% uptime
- ✅ No security incidents
- ✅ Manual effort <2 hours/week
- ✅ Primary workloads unaffected

**Pause/Re-evaluate if:**
- ⚠️ Net profit marginal ($0-2/day)
- ⚠️ Frequent technical issues
- ⚠️ High manual intervention needed
- ⚠️ Uncertainty about regulatory changes

**Terminate if:**
- ❌ Sustained negative ROI (>7 days)
- ❌ Security breach or risk
- ❌ Primary GPU use compromised
- ❌ Regulatory prohibition
- ❌ Hardware damage risk

---

## Risk Management

### Technical Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| GPU overheating | Low | High | Power limits + monitoring |
| Software crashes | Medium | Low | Watchdogs + auto-restart |
| Network issues | Medium | Medium | Pool failover |
| Hardware failure | Low | High | Thermal monitoring + limits |

### Financial Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Crypto price crash | High | High | Exit strategy + diversification |
| Difficulty increase | High | Medium | Algorithm switching |
| Electricity cost rise | Low | Medium | Solar awareness |
| Negative ROI | Medium | High | Continuous monitoring + exit plan |

### Security Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Wallet theft | Low | High | No private keys on cluster |
| Mining malware | Low | Medium | Binary verification |
| Pool compromise | Low | Low | Use established pools only |
| SSH breach | Very Low | High | Key-based auth only |

---

## Success Definition

**Phase 2 Success:**
- 72h test completes without incidents
- Actual earnings match estimates within ±20%
- ROI calculation framework validated
- Decision to proceed to Phase 3 is data-backed

**Project Success:**
- Net positive earnings sustained >30 days
- Automation reduces manual work to <1hr/week
- Primary GPU use unaffected
- Replicable methodology documented

**Exit with Success:**
- If negative ROI confirmed → document findings thoroughly
- If positive ROI but too marginal → shut down cleanly
- If regulatory issues → compliance documented
- All learnings captured for future reference

---

## Strategic Constraints

### Time Constraints:
- No more than 2 hours/week manual management (Phase 3 target)
- Major decisions reviewed within 48 hours
- Experiments run 72h minimum for statistical validity

### Budget Constraints:
- Zero additional hardware purchases (use existing cluster)
- Minimal software costs (prefer open source)
- Electricity cost already incurred (not incremental)

### Resource Constraints:
- Limited to 2 GPU nodes (ai-1, ai-2)
- SSH access required (no physical access)
- Development time is opportunity cost

---

## Communication Plan

### Internal Documentation:
- Update STATUS.md after each phase completion
- Log all experiments in EXPERIMENT_LOG.md
- Record decisions in DECISIONS.md (ADR format)
- Maintain this STRATEGY.md as living document

### Stakeholder Updates:
- Weekly summary (if project active)
- Immediate alert on critical issues
- Phase completion reports
- Exit decision documentation

---

## Roadmap Timeline

```
Week 1: ✅ Phase 1 Complete (Discovery)
Week 2: 🔄 Phase 2 Start (Automation)
Week 3-4: Phase 2 Continued (72h tests)
Week 5: Phase 2 Decision (Go/No-Go)
Week 6-9: Phase 3 (if approved)
Week 10+: Phase 4 (conditional)
```

---

## Open Questions

1. **Solar Integration:**
   - How to detect excess solar capacity programmatically?
   - What's the carbon footprint comparison?

2. **Regulatory:**
   - What are tax implications of mining income?
   - Any local regulations on residential mining?

3. **Optimization:**
   - Is dual-mining (ETH+ALEPH) more profitable than single?
   - What's the optimal algorithm switch frequency?

4. **Long-Term:**
   - Will GPU cluster scale beyond current 2 nodes?
   - Should we consider ASIC evaluation?

---

## Strategy Review Schedule

- **Weekly:** Review KPIs and immediate decisions
- **End of Phase:** Comprehensive phase retrospective
- **Monthly:** Strategic direction reassessment
- **Quarterly:** Long-term viability evaluation

---

**Next Review:** End of Phase 2 (estimated Week 4-5)
**Owner:** Repository Maintainer
**Last Updated:** 2026-02-16
