# Project Status — crypto-lab

**Last Updated:** 2026-02-16
**Current Phase:** Automation (Phase 2)

---

## Quick Status

| Metric | Status | Notes |
|--------|--------|-------|
| **Phase** | 🔄 Automation (Phase 2) | Bootstrap complete |
| **Mining Status** | ⏸️ Not Started | Awaiting wallet setup |
| **Profitability Runner** | ✅ Imported | Scripts in repo (PR #2) |
| **Auto-Switcher** | ⏸️ Not Implemented | Phase 3 feature |
| **Wallet** | ⏸️ Not Created | Pending algorithm selection |
| **Hardware** | ✅ Operational | Both GPUs ready |

---

## Current Phase: Phase 2 (Automation)

### Phase 2 Progress: 25% Complete

```
Bootstrap ████████████████████ 100%
Automation █████░░░░░░░░░░░░░░  25%
Optimization ░░░░░░░░░░░░░░░░░░   0%
Scale ░░░░░░░░░░░░░░░░░░░░░░   0%
```

---

## Active Tasks

### In Progress:
1. **Repository Bootstrap** ✅
   - Directory structure created
   - Governance documents written
   - Security protocols defined
   - Status: COMPLETE

2. **Profit-Run Integration** ✅
   - Scripts imported to crypto-lab repo (PR #2)
   - Manual profitability analysis complete
   - Automate data fetching (next step)
   - Status: COMPLETE

3. **Algorithm Selection** 🔄
   - Benchmark data available
   - Top candidate: Pyrin on RTX 3060
   - Need wallet creation
   - Status: PENDING

4. **CPU Strategic Utilization Analysis** ✅
   - CPU alternatives to mining documented (STRATEGY.md)
   - 6 workload options analyzed vs CPU mining baseline
   - Decision DEC-011 recorded (exploration approved, no implementation yet)
   - Status: COMPLETE (documentation-only)

### Queued:
5. **Wallet Setup** ⏸️
   - Waiting for final algorithm decision
   - Will create after repo bootstrap

6. **First 72h Test** ⏸️
   - Blocked by wallet creation
   - Target: Pyrin on ai-1 (RTX 3060)

---

## Hardware Status

### ai-1 (RTX 3060)
- **Status:** ✅ Ready
- **Temperature:** Idle (~50°C)
- **Power Limit:** 120W (configured)
- **Availability:** 100% (not mining)
- **Last Benchmark:** 2026-02-16 (Pyrin: 3113.51 MH/s)

### ai-2 (GTX 1660 SUPER)
- **Status:** ✅ Ready
- **Temperature:** Idle (~30°C)
- **Power Limit:** 80W (configured)
- **Availability:** 100% (not mining)
- **Last Benchmark:** 2026-02-16 (Pyrin: 1137.33 MH/s)
- **Known Limitation:** Cannot run Octopus (VRAM insufficient)

### dev-main (Control Node)
- **Status:** ✅ Operational
- **SSH Access:** Verified to both AI nodes
- **Disk Space:** Adequate for logs and scripts
- **Network:** Stable connection to mining pools tested

---

## Software Status

### Installed Miners:
- ✅ **lolMiner v1.98a** (ai-1, ai-2)
  - Location: `~/crypto/miners/lolminer/`
  - Supports: Autolykos2, Flux, Pyrin, Octopus
- ✅ **T-Rex v0.26.8** (ai-1, ai-2)
  - Location: `~/crypto/miners/trex-miner/`
  - Supports: KawPow, Autolykos2

### Scripts Ready:
- ✅ Paper ranking analyzer
- ✅ Real benchmark analyzer
- ⏸️ Profitability runner (needs migration)
- ⏸️ Monitoring automation (planned)

---

## Benchmark Results Summary

**Date:** 2026-02-16
**Duration:** 3 minutes per test

| Algorithm | ai-1 (RTX 3060) | ai-2 (GTX 1660 S) | Winner |
|-----------|-----------------|-------------------|--------|
| **KawPow** | 9.55 MH/s @ 119W | **10.10 MH/s @ 78W** | ai-2 |
| **Autolykos2** | **103.05 MH/s @ 119W** | 49.66 MH/s @ 79W | ai-1 |
| **Octopus** | **80.27 MH/s @ 112W** | ❌ FAIL (VRAM) | ai-1 |
| **Flux** | **41.1 Sol/s @ 111W** | 17.6 Sol/s @ 70W | ai-1 |
| **Pyrin** | **3113.51 MH/s @ 112W** | 1137.33 MH/s @ 74W | ai-1 |

**Best Overall:** Pyrin on RTX 3060 (27.8 MH/W efficiency)

---

## Financial Status

### Revenue:
- **Total Earned:** $0.00 (mining not started)
- **Pending Payouts:** $0.00
- **Total Withdrawn:** $0.00

### Costs:
- **Hardware:** $0 (using existing cluster)
- **Software:** $0 (open source / dev fees deducted from mining)
- **Electricity (incremental):** $0 (cluster already running)

### ROI:
- **Net Profit:** $0.00
- **Break-Even Status:** N/A (not mining yet)
- **Target:** Positive daily net profit after dev fees

---

## Risk Dashboard

### Current Risks:

| Risk | Level | Status | Mitigation |
|------|-------|--------|------------|
| Thermal | 🟢 Low | Idle | Power limits enforced |
| Security | 🟢 Low | No keys on nodes | Following protocols |
| Financial | 🟡 Medium | Zero earnings yet | Awaiting real data |
| Complexity | 🟢 Low | Simple setup | Avoiding over-engineering |
| Regulatory | 🟢 Low | Experimental scale | Monitoring developments |

### Incidents This Phase:
- None (Phase 0/Bootstrap)

---

## Upcoming Milestones

### Next 7 Days:
- [ ] Complete repository bootstrap
- [ ] Migrate profit-run scripts to crypto-lab
- [ ] Select final algorithm for first test
- [ ] Create wallet for selected cryptocurrency
- [ ] Launch first 72h mining test

### Next 30 Days:
- [ ] Complete Phase 2 (Automation)
- [ ] 3-5 algorithm tests completed
- [ ] Real profitability data collected
- [ ] Go/No-Go decision for Phase 3

### Next 90 Days:
- [ ] Phase 3 (Optimization) if Phase 2 successful
- [ ] Auto-switching logic implemented
- [ ] Solar-aware scheduling prototype
- [ ] Long-term viability assessment

---

## Blockers and Issues

### Current Blockers:
1. **None** (bootstrap phase complete)

### Open Questions:
1. Which pool to use for Pyrin? (HeroMiners vs WoolyPooly)
2. Wallet type: software (Zelcore) or hardware?
3. Payout threshold: daily vs weekly?

### Resolved Recently:
- ✅ Which GPUs to use → Both (DEC-001)
- ✅ Which miners to install → T-Rex + lolMiner (DEC-009)
- ✅ Power limits → 120W/80W (DEC-010)

---

## Performance Metrics (Phase 2 Target)

### Automation Goals:
- **Manual intervention:** <2 hours/week
- **Uptime:** >95% when mining
- **Data collection:** Daily automated reports
- **Response time:** <1 hour for critical alerts

### Current Performance:
- **Manual intervention:** ~4 hours (bootstrap)
- **Uptime:** N/A (not mining)
- **Data collection:** Manual
- **Response time:** N/A

---

## Health Check

### System Health:
- ✅ All nodes accessible via SSH
- ✅ GPU drivers up to date
- ✅ Power limits configured
- ✅ Monitoring tools installed
- ✅ Documentation complete

### Repository Health:
- ✅ SSOT enforced (main branch protected)
- ✅ Governance documents in place
- ✅ Security protocols defined
- ✅ Decision log started
- ✅ Experiment log template ready

### Project Health:
- ✅ Clear objectives defined
- ✅ Exit criteria established
- ✅ Phases planned
- ✅ Risk assessment complete
- ✅ Human oversight confirmed

---

## Decision Pending

**Next Major Decision: Algorithm Selection for 72h Test**

**Options:**
1. **Pyrin** (Recommended)
   - Pros: Best efficiency (27.8 MH/W), stable temps, good hashrate
   - Cons: Less established than some alternatives
2. **Autolykos2 (Ergo)**
   - Pros: Well-established coin, good hashrate (103 MH/s)
   - Cons: Lower efficiency than Pyrin
3. **KawPow (Ravencoin)**
   - Pros: Large market cap ($100M), established
   - Cons: Lower efficiency, higher temps on ai-2

**Decision Maker:** Repository Owner
**Deadline:** Before wallet creation
**Impact:** Determines Phase 2 success metrics

---

## Communication Log

### Recent Updates:
- **2026-02-16:** Repository bootstrap initiated
- **2026-02-16:** Governance documents created
- **2026-02-16:** Security protocols defined
- **2026-02-16:** Benchmark data collected

### Upcoming Communications:
- Weekly status update (starting next week)
- Phase 2 completion report (in ~2 weeks)
- Go/No-Go decision for Phase 3 (in ~4 weeks)

---

## Notes

- This is the initial STATUS.md for crypto-lab repository
- Will be updated after each significant milestone
- Reflects accurate state as of bootstrap completion
- Next update: after first 72h mining test

---

**Status Report Generated:** 2026-02-16
**Next Update Due:** After first mining test launch
**Report Owner:** Repository Maintainer
