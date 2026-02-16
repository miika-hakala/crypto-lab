# Experiment Log — crypto-lab

**Purpose:** Track all mining experiments with detailed metrics for analysis and decision-making.

**Last Updated:** 2026-02-16

---

## Log Format

Each experiment entry should include:
- Date and duration
- Hardware used (GPU)
- Algorithm and miner
- Pool information
- Hashrate (average, min, max)
- Power consumption (average, min, max)
- Temperature (average, max)
- Accepted/Rejected shares
- Earnings (if applicable)
- Issues and observations
- Conclusions

---

## Template

```markdown
## EXP-XXX: [Experiment Title]

**Date:** YYYY-MM-DD
**Duration:** Xh Xm
**Phase:** Discovery | Automation | Optimization

### Configuration
- **GPU:** ai-1 (RTX 3060) | ai-2 (GTX 1660 SUPER)
- **Algorithm:** [Algorithm name]
- **Miner:** [Software name] v[version]
- **Pool:** [Pool name + URL]
- **Wallet:** [Last 8 chars of address]

### Performance Metrics
- **Hashrate (avg):** X.XX MH/s | Sol/s
- **Hashrate (min/max):** X.XX / X.XX MH/s
- **Power (avg):** XXW
- **Power (min/max):** XX / XXW
- **Temperature (avg):** XX°C
- **Temperature (max):** XX°C
- **Fan Speed (avg):** XX%

### Network Stats
- **Accepted Shares:** XXX
- **Rejected Shares:** XX (X.X%)
- **Stale Shares:** XX (X.X%)
- **Pool Latency:** XXms
- **Uptime:** XX.X%

### Financial
- **Estimated Revenue:** $X.XX/day
- **Actual Earnings:** $X.XX (if completed)
- **Dev Fee Deducted:** X.X%
- **Net After Fees:** $X.XX

### Observations
- [Notable behavior]
- [Issues encountered]
- [Stability notes]

### Conclusions
- [What was learned]
- [Decision impact]
- [Next steps]

---
```

---

## Experiments

### EXP-000: Baseline Benchmarking (Discovery Phase)

**Date:** 2026-02-16
**Duration:** 3 minutes per algorithm × 5 algorithms × 2 GPUs
**Phase:** Discovery

### Configuration
- **GPUs:** ai-1 (RTX 3060) + ai-2 (GTX 1660 SUPER)
- **Algorithms:** KawPow, Autolykos2, Octopus, Flux, Pyrin
- **Miners:** T-Rex v0.26.8 (KawPow, Autolykos2), lolMiner v1.98a (others)
- **Mode:** Benchmark (offline, no pool)

### Performance Summary

#### ai-1 (RTX 3060) Results:
| Algorithm | Hashrate | Power | Temp | Efficiency |
|-----------|----------|-------|------|------------|
| KawPow | 9.55 MH/s | 119W | 60°C | 0.08 MH/W |
| Autolykos2 | 103.05 MH/s | 119W | 62°C | 0.87 MH/W |
| Octopus | 80.27 MH/s | 112W | 62°C | 0.72 MH/W |
| Flux | 41.1 Sol/s | 111W | 61°C | 0.37 SH/W |
| Pyrin | 3113.51 MH/s | 112W | 62°C | 27.80 MH/W |

#### ai-2 (GTX 1660 SUPER) Results:
| Algorithm | Hashrate | Power | Temp | Efficiency |
|-----------|----------|-------|------|------------|
| KawPow | 10.10 MH/s | 78W | 75°C | 0.13 MH/W |
| Autolykos2 | 49.66 MH/s | 79W | 72°C | 0.63 MH/W |
| Octopus | FAILED | — | — | VRAM insufficient |
| Flux | 17.6 Sol/s | 70W | 70°C | 0.25 SH/W |
| Pyrin | 1137.33 MH/s | 74W | 77°C | 15.37 MH/W |

### Key Findings

**Best Overall:**
- **Pyrin on RTX 3060:** 3113.51 MH/s @ 112W = 27.80 MH/W (highest efficiency)

**Interesting Results:**
- **GTX 1660 SUPER beats RTX 3060 on KawPow** (10.1 vs 9.55 MH/s)
- **RTX 3060 dominates memory-heavy algorithms** (Autolykos2, Octopus)
- **GTX 1660 SUPER runs hotter** (+10-15°C across all algorithms)

**Hardware Limitations:**
- **GTX 1660 SUPER cannot run Octopus** (requires >6GB VRAM)

### Conclusions

1. **Algorithm Selection:** Pyrin is clear winner for efficiency
2. **GPU Allocation:**
   - ai-1 (RTX 3060): Best for most algorithms
   - ai-2 (GTX 1660 SUPER): Competitive on KawPow, thermal concerns
3. **Next Steps:**
   - Create Pyrin wallet
   - Select mining pool
   - Launch 72h test on Pyrin @ ai-1

**Decision Impact:** DEC-001 validated (use both GPUs), new data for Phase 2 planning

---

### EXP-001: Ergo 72h Production Test (Planned)

**Date:** TBD (Pending wallet creation)
**Duration:** 72 hours continuous
**Phase:** Automation (Phase 2)
**Status:** ⏸️ Awaiting Ergo wallet address

### Configuration
- **GPUs:** gpu-node-1 (RTX 3060) + gpu-node-2 (GTX 1660 SUPER)
- **Algorithm:** Autolykos2 (Ergo)
- **Miner:** lolMiner v1.98a
- **Pool:** HeroMiners (ergo.herominers.com:1180)
- **Workers:** ERG_WALLET_ADDRESS_HERE.ai1 and .ai2
- **Wallet:** [Will be filled after wallet creation]
- **Runbook:** docs/runbooks/ERG_72H_TEST.md

### Target Performance Metrics

**gpu-node-1 (RTX 3060):**
- **Expected Hashrate:** ~103 MH/s (from EXP-000 benchmark)
- **Power Limit:** 120W
- **Target Temperature:** <75°C
- **Target Uptime:** >95% (68.4+ hours)

**gpu-node-2 (GTX 1660 SUPER):**
- **Expected Hashrate:** ~50 MH/s (from EXP-000 benchmark)
- **Power Limit:** 80W
- **Target Temperature:** <65°C (watch for thermal issues)
- **Target Uptime:** >95%

### Success Criteria
- [ ] Pool connection stable (uptime >95%)
- [ ] Rejection rate <2%
- [ ] No thermal throttling events
- [ ] No miner crashes (or <2 total)
- [ ] Earnings match profitability estimate (±20%)
- [ ] Daily net profit >$0

### Results
**[To be filled after 72h test completes]**

**Performance:**
- Hashrate (avg gpu-node-1): _______ MH/s
- Hashrate (avg gpu-node-2): _______ MH/s
- Power (avg gpu-node-1): _______ W
- Power (avg gpu-node-2): _______ W
- Temperature (max gpu-node-1): _______ °C
- Temperature (max gpu-node-2): _______ °C

**Network:**
- Accepted Shares: _______
- Rejected Shares: _______ (____%)
- Uptime: _______% (_____ hours)

**Financial:**
- Total ERG Earned: _______ ERG
- ERG Price at End: $_______ per ERG
- Total Revenue: $_______
- Daily Average: $_______/day
- Variance from Estimate: _____%

**Observations:**
- [To be documented during test]

**Conclusions:**
- [To be documented after test]
- **Decision:** GO / ADJUST / NO-GO (continue Ergo, adjust settings, or switch algorithm)

**See Also:** docs/runbooks/ERG_WALLET_CREATION.md, docs/runbooks/ERG_72H_TEST.md

---

## Future Experiments (Planned)

### EXP-002: Pyrin 72h Test (Alternative)
- **Target:** Alternative algorithm if EXP-001 (Ergo) is not profitable
- **GPU:** gpu-node-1 (RTX 3060) + gpu-node-2 (GTX 1660 S)
- **Duration:** 72 hours
- **Status:** 📋 Planned (if Ergo NO-GO decision)

### EXP-003: KawPow Comparison Test
- **Target:** Compare pool vs solo mining
- **GPU:** ai-2 (GTX 1660 SUPER)
- **Duration:** 48 hours
- **Status:** 📋 Planned (if EXP-002 successful)

### EXP-004: Autolykos2 Efficiency Optimization
- **Target:** Test power limit variations (100W, 110W, 120W)
- **GPU:** ai-1 (RTX 3060)
- **Duration:** 3 × 12 hours
- **Status:** 📋 Planned

### EXP-005: Dual-GPU Coordination
- **Target:** Run different algorithms on each GPU simultaneously
- **GPUs:** Both
- **Duration:** 24 hours
- **Status:** 📋 Planned (Phase 3)

---

## Experiment Statistics

### Total Experiments: 2
- ✅ Completed: 1 (EXP-000)
- 🔄 In Progress: 0
- ⏸️ Awaiting Start: 1 (EXP-001, pending wallet)
- 📋 Planned: 4 (EXP-002 through EXP-005)
- ❌ Failed: 0

### Phase Breakdown:
- **Discovery:** 1 completed (EXP-000)
- **Automation:** 1 awaiting start (EXP-001)
- **Optimization:** 0 started

### GPU Utilization:
- **ai-1 (RTX 3060):** 3 min test runtime (baseline)
- **ai-2 (GTX 1660 SUPER):** 3 min test runtime (baseline)
- **Total Mining Time:** 0h 0m (production)

---

## Issues Tracker

### Open Issues:
- None currently

### Resolved Issues:
- ✅ **CSV corruption in nvidia-smi logs** (EXP-001)
  - Cause: Formatting bug in nvidia-smi output
  - Resolution: Manual metric extraction from miner output

---

## Notes and Best Practices

### Lessons Learned:
1. **3-minute benchmarks sufficient** for hashrate stability assessment
2. **Power limits critical** for thermal management (stayed <70°C on ai-1)
3. **GTX 1660 SUPER thermal headroom limited** (75-77°C at 80W)
4. **lolMiner benchmark mode unreliable** for Autolykos2 (memory allocation error)
5. **T-Rex benchmark mode works perfectly** for all supported algorithms

### Recommendations:
- Always run nvidia-smi logging in parallel with mining
- Use 10-second sampling interval for thermal monitoring
- Minimum 72h for real profitability assessment
- Verify pool connection before long-term tests
- Keep power limits conservative (10-20% below TDP)

---

## Data Locations

### Benchmark Raw Data:
- **Location:** `~/crypto/profit-run/bench_results/`
- **Files:** 10 × CSV (nvidia-smi logs) + 10 × TXT (miner outputs)
- **Size:** ~108MB total
- **Retention:** Permanent (for analysis)

### Production Logs:
- **Location:** `~/mining-test/` (on each AI node)
- **Format:** CSV (nvidia-smi) + TXT (miner logs)
- **Rotation:** Manual (review after each experiment)

---

## Changelog

**2026-02-16:**
- Created experiment log template
- Added EXP-000 baseline benchmarking results
- Added EXP-001 template (Ergo 72h test, awaiting wallet)
- Planned future experiments EXP-002 through EXP-005

---

**Log Owner:** Repository Maintainer
**Next Experiment:** EXP-001 (Ergo 72h test, awaiting wallet creation)
**Last Entry:** EXP-000 (completed)
