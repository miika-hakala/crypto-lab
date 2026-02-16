# Architecture Decision Records (ADRs) — crypto-lab

This document tracks all significant architectural and strategic decisions for the crypto-lab project using the ADR (Architecture Decision Record) format.

---

## DEC-001: Use Both GPU Nodes (ai-1 and ai-2)

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Discovery

### Context
We have two available GPU nodes with different specifications:
- **ai-1:** RTX 3060 (12GB VRAM, 120W limit)
- **ai-2:** GTX 1660 SUPER (6GB VRAM, 80W limit)

### Decision
Both GPUs will be utilized for mining experiments, with algorithm selection optimized per GPU capabilities.

### Rationale
1. Doubles available hashrate capacity
2. Provides comparison data between GPU architectures
3. GTX 1660 SUPER excels at certain algorithms (e.g., KawPow)
4. Allows testing different algorithms simultaneously

### Consequences
**Positive:**
- Increased total hashrate
- Better data for algorithm comparison
- Flexibility in algorithm selection

**Negative:**
- More complex management (2 nodes vs 1)
- GTX 1660 SUPER has VRAM limitations (can't run Octopus)
- Higher total power consumption

### Implementation
- Both nodes configured with mining software
- Per-GPU algorithm optimization based on benchmarks
- Power limits enforced: ai-1=120W, ai-2=80W

---

## DEC-002: Start Simple, Optimize Later

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Automation

### Context
Mining automation can be complex with many potential optimizations: auto-switching, dual-mining, overclocking, etc.

### Decision
Begin with manual single-algorithm mining per GPU, then incrementally add automation features based on proven need.

### Rationale
1. Reduces initial complexity and failure points
2. Establishes baseline performance metrics
3. Validates profitability before investing in automation
4. Allows learning mining fundamentals first

### Consequences
**Positive:**
- Faster time to first results
- Easier troubleshooting
- Lower development cost
- Clear baseline for future optimization

**Negative:**
- Manual intervention required for algorithm changes
- May miss short-term profit opportunities
- Slower to reach optimal profitability

### Implementation
- Phase 2: Manual coin selection and deployment
- Phase 3: Add automation after 72h manual test validates approach
- Prioritize stability over feature richness initially

---

## DEC-003: Single Algorithm per Test Period

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Discovery

### Context
Multiple testing strategies possible:
- Test one algorithm for extended period (72h+)
- Rapidly switch between algorithms
- Run different algorithms on each GPU

### Decision
Test one algorithm at a time for minimum 72 hours to gather statistically valid profitability data.

### Rationale
1. 72h provides meaningful sample of variance (day/night, weekday/weekend)
2. Eliminates switching overhead as variable
3. Allows proper thermal stability assessment
4. Simplifies data analysis and comparison

### Consequences
**Positive:**
- High-quality data per algorithm
- Clear profitability picture
- Easier to diagnose issues
- Reliable baseline for future switching logic

**Negative:**
- Slower to test all algorithms
- May miss short-term profitability spikes in other algorithms
- Sequential testing takes weeks vs days

### Implementation
- First 72h test: Pyrin on RTX 3060
- Subsequent tests: Top 3-5 algorithms based on paper ranking
- Each test: full metrics collection (hashrate, power, temp, earnings)

---

## DEC-004: Optimize for Maximum Gross Revenue (Phase 2)

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Automation

### Context
Different optimization targets possible:
- Maximum gross revenue (highest hashrate × coin value)
- Maximum profit per watt (efficiency focus)
- Most stable algorithm (lowest variance)

### Decision
Phase 2 focuses on **maximum gross revenue**, deferring per-watt optimization to Phase 3.

### Rationale
1. Electricity cost is fixed (cluster runs regardless)
2. Maximizing gross revenue is simpler metric
3. Per-watt optimization requires solar integration (Phase 3)
4. Easier to communicate and validate results

### Consequences
**Positive:**
- Clear, understandable primary metric
- Aligns with opportunistic mining model
- Simplifies initial algorithm selection
- Faster decision-making

**Negative:**
- May not be most environmentally friendly
- Could miss high-efficiency but lower-revenue algorithms
- Less relevant if electricity becomes variable cost

### Future Review
Re-evaluate in Phase 3 when solar integration is considered. May shift to profit-per-watt optimization.

---

## DEC-005: Defer Wallet Creation Until Algorithm Selected

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Automation

### Context
Wallet required before mining, but creating wallets for all potential coins is time-consuming and creates security surface area.

### Decision
Wait until Phase 1 analysis completes and top algorithm is selected before creating wallet.

### Rationale
1. Reduces unnecessary wallet proliferation
2. Focuses security effort on one coin initially
3. Allows informed decision on wallet type (hot/cold, hardware/software)
4. Analysis may reveal unexpected top performer

### Consequences
**Positive:**
- Minimal security surface area
- No unused wallets to manage
- Wallet choice informed by final algorithm selection
- Reduces setup time

**Negative:**
- Delays start of actual mining by ~1 day
- Can't test payout mechanics until wallet created
- Risk of choosing algorithm then discovering wallet setup issues

### Implementation
- Phase 1 completes → identifies top algorithm
- Create wallet for that specific cryptocurrency
- Verify pool payout mechanics before 72h test
- Document wallet setup process in EXPERIMENT_LOG.md

---

## DEC-006: No Private Keys on Mining Nodes

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** All Phases

### Context
Mining requires wallet address for payouts, but private keys enable spending.

### Decision
Mining nodes only store **public receiving addresses**. Private keys kept offline on secure device.

### Rationale
1. Minimizes risk of theft if node compromised
2. Follows industry best practice (hot wallet separation)
3. Losses limited to unpaid mining rewards (typically <24h)
4. No additional security infrastructure needed on nodes

### Consequences
**Positive:**
- Major security vulnerability eliminated
- Node compromise has limited financial impact
- Simpler node security requirements
- Peace of mind for long-running tests

**Negative:**
- Cannot automate transfers from mining wallet
- Manual payout withdrawals required
- Small risk of pool-side issues if wallet unreachable

### Implementation
- Wallet created on separate secure device (offline)
- Only public address added to miner configurations
- Regular manual withdrawals to cold storage (weekly)
- Document wallet backup procedure

---

## DEC-007: User-Space Mining Software Only

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** All Phases

### Context
Mining software can be installed as:
- System daemon (systemd service, root-level)
- User-space application (manual start/stop)

### Decision
All mining software runs as **user-space applications**, no system daemons or root-level installations.

### Rationale
1. Preserves system integrity
2. Easier to uninstall/rollback
3. No sudo/root privileges required
4. Aligns with non-invasive experimental approach
5. Doesn't interfere with primary GPU usage (Ollama)

### Consequences
**Positive:**
- Clean installation/removal
- No system-wide impact
- Can coexist with other GPU applications
- Lower risk of breaking primary infrastructure

**Negative:**
- No automatic start on boot
- Requires manual startup (or user cron)
- Process management more manual
- Survival of SSH disconnect requires tmux/screen

### Implementation
- Miners installed to ~/crypto/miners/
- Launched via tmux/screen for persistence
- No systemd service files
- All configurations in user home directory

---

## DEC-008: Use Established Mining Pools Only

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** All Phases

### Context
Many mining pools available, ranging from well-established to new/unknown.

### Decision
Only use mining pools with:
- Established reputation (>1 year operation)
- Public transparency (hashrate, users, payments visible)
- Reasonable fees (<2%)
- SSL/TLS support
- Regular payouts

**Approved pools (initial):**
- HeroMiners
- WoolyPooly
- 2Miners
- Nanopool

### Rationale
1. Reduces risk of pool scams or disappearance
2. Ensures payouts actually occur
3. Better uptime and DDoS protection
4. Community-verified legitimacy
5. Documented API for automation

### Consequences
**Positive:**
- High confidence in payout reliability
- Lower risk of wasted mining effort
- Better pool infrastructure (lower latency, failover)
- Community support available

**Negative:**
- May miss slightly higher rewards from smaller pools
- Popular pools have more competition
- Fees may be higher than new pools (but safer)

### Implementation
- Verify pool reputation before use
- Test with small hashrate first
- Monitor first payout before committing long-term
- Document pool performance in EXPERIMENT_LOG.md

---

## DEC-009: Bootstrap with T-Rex and lolMiner

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** Discovery

### Context
Many mining software options available, each with different algorithm support and efficiency.

### Decision
Use **T-Rex Miner** and **lolMiner** as primary mining software:
- **T-Rex:** For KawPow, Autolykos2 (closed source, high efficiency)
- **lolMiner:** For Octopus, Flux, Pyrin, Autolykos2 (open source)

### Rationale
1. Benchmark data already collected for both miners
2. Cover all target algorithms between two miners
3. T-Rex proven most efficient for NVIDIA GPUs
4. lolMiner provides open-source alternative and wider algorithm support
5. Both have active development and community support

### Consequences
**Positive:**
- No additional benchmark time needed
- Known performance characteristics
- Community support available
- Development fees are reasonable (1-2%)

**Negative:**
- T-Rex is closed source (trust required)
- Development fees reduce net earnings by 1-2%
- May not be absolutely optimal miners for all algorithms

### Future Review
Evaluate alternative miners if:
- Significant performance gap discovered
- Open-source alternative to T-Rex becomes competitive
- New algorithm requires different miner

---

## DEC-010: Power Limits Enforced at Hardware Level

**Date:** 2026-02-16
**Status:** ✅ Accepted
**Phase:** All Phases

### Context
GPUs can be power-limited via:
- Software (miner settings)
- Driver (nvidia-smi)
- Hardware (BIOS, firmware)

### Decision
Enforce power limits using **nvidia-smi** driver-level settings:
- **ai-1 (RTX 3060):** 120W limit (default 170W)
- **ai-2 (GTX 1660 SUPER):** 80W limit (default 125W)

### Rationale
1. Hardware-enforced = most reliable
2. Survives miner crashes or misconfiguration
3. Protects against aggressive miner power settings
4. Reduces thermal load and extends GPU lifespan
5. Benchmark data already collected at these limits

### Consequences
**Positive:**
- Guaranteed power consumption ceiling
- Lower temps and fan noise
- GPU longevity preserved
- No risk of exceeding electrical capacity

**Negative:**
- Reduced maximum hashrate vs unlimited power
- May not be optimal for all algorithms
- Some efficiency loss at power limit

### Implementation
```bash
# Set on boot or before mining
sudo nvidia-smi -pm 1  # Persistence mode
sudo nvidia-smi -pl 120  # Power limit (ai-1)
sudo nvidia-smi -pl 80   # Power limit (ai-2)
```

---

## DEC-011: CPU Mining vs Strategic CPU Utilization

**Date:** 2026-02-16
**Status:** Accepted
**Phase:** Automation (Phase 2)

### Context

CPU mining profitability is negligible to negative on modern consumer hardware:
- RandomX (Monero): ~$0.10-0.50/day per 12-16 core CPU
- Electricity cost typically exceeds earnings
- GPU mining delivers 50-100x better performance per watt

However, the cluster CPUs (ai-1, ai-2) remain idle during GPU-only mining operations. The question arises: **Are there higher-value CPU workloads than mining?**

Additionally, existing infrastructure (Ollama AI, crawler) suggests potential synergies for CPU-intensive tasks beyond cryptocurrency mining.

### Decision

**Approved:** Exploration of strategic CPU utilization alternatives to mining.

**Scope of approval:**
- Documentation of 6 CPU workload alternatives (completed in STRATEGY.md)
- Analysis of ROI potential vs CPU mining baseline
- Ranking by strategic fit with existing infrastructure

**Not approved (yet):**
- Implementation of any specific alternative
- Resource allocation for development
- Pivot away from GPU mining focus

**Rationale for exploration:**
1. CPU mining baseline is effectively zero ROI
2. Any positive-ROI CPU workload is categorically better
3. Existing infrastructure (AI, crawler) creates natural synergies
4. Opportunistic CPU utilization doesn't conflict with GPU mining experiments

### Rationale

**Why explore alternatives:**
1. **CPU mining is economically unviable** — Even best-case scenarios (Monero RandomX) yield <$0.50/day, often negative after electricity
2. **Idle CPU capacity exists** — During GPU mining, CPUs sit at <10% utilization
3. **Infrastructure synergies** — Existing Ollama (AI) and crawler infrastructure create natural extension points
4. **Low opportunity cost** — Documentation-only analysis requires minimal investment
5. **Data-driven approach** — Consistent with project philosophy (test, measure, decide)

**Why not commit to implementation yet:**
1. **GPU mining focus maintained** — Phase 2 (Automation) still in progress
2. **Insufficient data** — Need market validation for specific alternatives
3. **Resource constraints** — Development time is opportunity cost vs GPU optimization
4. **Phase discipline** — Avoid scope creep during active GPU experiments

### Consequences

**Positive:**
- ✅ Documented alternative compute strategies for future reference
- ✅ Framework for evaluating CPU workload ROI vs mining baseline
- ✅ Identified high-synergy options (data enrichment, AI inference)
- ✅ No resource commitment required (documentation-only)
- ✅ Preserves optionality for future pivots if GPU mining fails

**Negative:**
- ⚠️ Potential distraction from GPU mining focus
- ⚠️ Creates additional decision paralysis (more options to evaluate)
- ⚠️ No immediate revenue impact (exploration, not execution)

**Neutral:**
- Analysis reveals arbitrage/trading as highest potential ROI but also highest risk (noted for awareness)

### Implementation

**Completed:**
- [x] CPU alternatives section added to STRATEGY.md
- [x] 6 alternatives documented with ROI analysis
- [x] Strategic fit ranking completed
- [x] Decision recorded in DECISIONS.md (DEC-011)

**Not started (pending future decision):**
- [ ] Market validation for specific alternatives
- [ ] Technical feasibility prototyping
- [ ] Resource allocation for development
- [ ] Customer/revenue source identification

**Next steps (if pursued):**
1. Complete Phase 2 (GPU mining automation)
2. Evaluate Phase 2 results (go/no-go for GPU mining)
3. If GPU mining is not viable → prioritize CPU alternatives
4. If GPU mining is viable → CPU alternatives remain opportunistic

### Future Review

**Review triggers:**
- **End of Phase 2** — If GPU mining shows negative ROI, re-evaluate CPU alternatives as primary strategy
- **Infrastructure changes** — If new workloads emerge (e.g., large-scale transcription needs), reassess fit
- **Market opportunities** — If customer/revenue source appears for specific alternative
- **Quarterly review** — General strategic reassessment

**Success criteria for implementation (if pursued later):**
- Identified revenue source or customer for specific workload
- Technical feasibility validated (prototype or proof-of-concept)
- ROI projection >10x CPU mining baseline (minimum threshold)
- Development effort <2 weeks for MVP

**Decision owner:** Repository Maintainer

---

## Template for Future Decisions

```markdown
## DEC-XXX: [Decision Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Rejected | Superseded | Deprecated
**Phase:** Discovery | Automation | Optimization | Scale

### Context
[Why this decision is needed. What is the background?]

### Decision
[What is being decided? State clearly and concisely.]

### Rationale
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

### Consequences
**Positive:**
- [Benefit 1]
- [Benefit 2]

**Negative:**
- [Cost 1]
- [Risk 1]

### Implementation
[How will this be implemented? Any code/config changes needed?]

### Future Review
[Under what conditions should this decision be revisited?]
```

---

## Decision Status Legend

- **Proposed:** Under consideration, not yet approved
- **Accepted:** Approved and active
- **Rejected:** Considered but not approved
- **Superseded:** Replaced by newer decision (link to replacement)
- **Deprecated:** No longer applicable, kept for historical reference

---

**Last Updated:** 2026-02-16
**Total Decisions:** 11
**Active Decisions:** 11
