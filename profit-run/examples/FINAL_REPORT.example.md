# CRYPTO: Profitability Runner — Final Report

**Date:** 2026-02-16
**Duration:** Single-session benchmark + analysis
**Nodes:** control-node + gpu-node-1 (RTX 3060) + gpu-node-2 (GTX 1660 SUPER)

---

## Executive Summary

Completed comprehensive cryptocurrency mining profitability analysis including:
- ✅ Paper ranking from WhatToMine API (25 GPU-mineable coins)
- ✅ Real benchmarks on 5 algorithms across 2 GPUs
- ✅ Power consumption and temperature monitoring
- ✅ Efficiency analysis and 72h test recommendation

### 🏆 **Recommendation: Pyrin (HeavyHash) on RTX 3060**
- **Hashrate:** 3113.51 MH/s
- **Power:** 112W (at 120W limit)
- **Temperature:** 62°C (stable)
- **Efficiency:** 27.80 MH/W ← **Best in class**

---

## Process Overview

### STEP 0 — GPU Status Check ✅
Both GPUs idle and ready:
- **gpu-node-1 (RTX 3060):** 0% util, 17.92W, 51°C
- **gpu-node-2 (GTX 1660 SUPER):** 0% util, 8.36W, 31°C

### STEP 1 — Workspace Creation ✅
Created: `~/crypto/profit-run/` on control-node

### STEP 2 — API Data Collection ✅
- **WhatToMine:** 26KB JSON, 25 GPU-mineable coins
- **Minerstat:** Failed (401 Unauthorized)

### STEP 3 — Paper Ranking ✅
**Top 5 Coins by Composite Score:**
1. **Ravencoin (RVN)** — KawPow, $100.7M mcap
2. **Zano (ZANO)** — ProgPowZ, $132.5M mcap
3. **Quai (QUAI)** — KawPow, $50.8M mcap
4. **EthereumClassic (ETC)** — Etchash, $1.36B mcap
5. **Ergo (ERG)** — Autolykos2, $27.4M mcap

**Target Algorithms Found:**
- ✅ KawPow (6 coins)
- ✅ Autolykos2 (2 coins)
- ✅ Octopus (2 coins)
- ❌ KHeavyHash (not in WhatToMine)
- ❌ ZelHash (not in WhatToMine)

### STEP 4 — Miner Strategy ✅
**Dual-miner approach:**
- **lolMiner v1.98a** (open source) for Autolykos2, Octopus, Flux, Pyrin
- **T-Rex v0.26.8** (closed source) for KawPow, Autolykos2

### STEP 5 — Non-Invasive Installation ✅
Installed to both nodes:
- `~/crypto/miners/lolminer/` (14MB)
- `~/crypto/miners/trex-miner/` (45MB)

No system daemons, no autostart, user-space only.

### STEP 6 — Real Benchmarks ✅

Power limits applied:
- gpu-node-1: 120W (default 170W)
- gpu-node-2: 80W (default 125W)

**Benchmark Results:**

| Algorithm | GPU | Hashrate | Power | Temp | Efficiency |
|-----------|-----|----------|-------|------|------------|
| **KawPow** | RTX 3060 | 9.55 MH/s | 119W | 60°C | 0.08 MH/W |
| **KawPow** | GTX 1660 S | **10.10 MH/s** ⭐ | 78W | 75°C | **0.13 MH/W** |
| **Autolykos2** | RTX 3060 | **103.05 MH/s** ⭐ | 119W | 62°C | 0.87 MH/W |
| **Autolykos2** | GTX 1660 S | 49.66 MH/s | 79W | 72°C | 0.63 MH/W |
| **Octopus** | RTX 3060 | **80.27 MH/s** ⭐ | 112W | 62°C | 0.72 MH/W |
| **Octopus** | GTX 1660 S | ❌ **FAILED** | — | — | VRAM < 6GB |
| **Flux** | RTX 3060 | **41.1 Sol/s** ⭐ | 111W | 61°C | 0.37 SH/W |
| **Flux** | GTX 1660 S | 17.6 Sol/s | 70W | 70°C | 0.25 SH/W |
| **Pyrin** | RTX 3060 | **3113.51 MH/s** ⭐ | 112W | 62°C | **27.80 MH/W** 🏆 |
| **Pyrin** | GTX 1660 S | 1137.33 MH/s | 74W | 77°C | 15.37 MH/W |

**Key Findings:**
- ⭐ RTX 3060 wins 4/5 algorithms (all except KawPow)
- 🔥 GTX 1660 SUPER runs hotter (+10-15°C across all algos)
- ❌ GTX 1660 SUPER cannot run Octopus (VRAM limitation)
- 🏆 Pyrin has **27.8 MH/W** — highest efficiency by far
- 💡 GTX 1660 SUPER beats RTX 3060 on KawPow (10.1 vs 9.55 MH/s)

### STEP 7 — Real Ranking Analysis ✅

**Top 3 by Efficiency:**
1. **Pyrin on RTX 3060** — 27.80 MH/W
2. **Pyrin on GTX 1660 S** — 15.37 MH/W
3. **Autolykos2 on RTX 3060** — 0.87 MH/W

**Most Stable (Lowest Temp):**
1. **KawPow on RTX 3060** — 60°C
2. **Flux on RTX 3060** — 61°C
3. **Pyrin on RTX 3060** — 62°C

**Winner per Algorithm:**
- **KawPow:** GTX 1660 SUPER (10.1 MH/s, more efficient)
- **Autolykos2:** RTX 3060 (103.05 MH/s, 2× faster)
- **Octopus:** RTX 3060 (only compatible GPU)
- **Flux:** RTX 3060 (41.1 Sol/s, 2× faster)
- **Pyrin:** RTX 3060 (3113.51 MH/s, best efficiency)

---

## 72-Hour Test Recommendation

### Primary: Pyrin on RTX 3060 (gpu-node-1) 🏆

**Hardware:**
- NVIDIA GeForce RTX 3060 (12GB)
- PCI Express x16 Gen 4
- 120W power limit (enforced)

**Expected Performance:**
- Hashrate: 3113 MH/s (~3.1 GH/s)
- Power: 112W average
- Temperature: 62°C (stable)
- Efficiency: 27.8 MH/W
- Fan speed: ~61%

**Miner Configuration:**
```bash
cd ~/crypto/miners/lolminer
./lolMiner --algo PYRIN \
  --pool stratum+tcp://PYRIN_POOL_URL:PORT \
  --user YOUR_PYRIN_WALLET_ADDRESS.worker1 \
  --pass x
```

**Rationale:**
1. **Best efficiency** — 27.8 MH/W is exceptional
2. **Stable temps** — 62°C allows for 72h continuous operation
3. **Low power** — 112W well under limit, headroom for stability
4. **Future-proof** — 12GB VRAM supports future algo changes

**Monitoring Plan (72h):**
- Check pool dashboard every 12h for reported hashrate
- Monitor nvidia-smi: `watch -n 60 nvidia-smi`
- Track accepted/rejected shares ratio (target: >99%)
- Verify stable temperature (<70°C)
- Log daily earnings to compare vs estimates

### Alternative Options

#### Option 2: KawPow on GTX 1660 SUPER (gpu-node-2)
- Hashrate: 10.1 MH/s
- Power: 78W
- Temp: 75°C ⚠️ (borderline high)
- Use for: Ravencoin (RVN) — larger market cap

⚠️ **Concern:** Temperature at 75°C for short test; may climb during 72h run.

#### Option 3: Autolykos2 on RTX 3060 (gpu-node-1)
- Hashrate: 103.05 MH/s
- Power: 119W
- Temp: 62°C
- Use for: Ergo (ERG) — established coin

---

## Critical Constraints & Safety

### Hardware Limitations
1. **GTX 1660 SUPER cannot run Octopus** — needs >6GB VRAM
2. **Power limits enforced:** gpu-node-1=120W, gpu-node-2=80W
3. **STOP conditions:**
   - GPU temp >75°C continuously
   - Power draw consistently exceeds limit
   - Accepted share rate <95%
   - Hardware instability or crashes

### Security Notes
- ✅ No private keys stored anywhere
- ✅ No seed phrases in configs
- ⚠️ Replace placeholder wallet addresses before 72h test
- ✅ All installations in user-space only
- ✅ No systemd autostart configured

### 72h Test Checklist
- [ ] Choose coin and create wallet (or use existing)
- [ ] Select mining pool (recommend: HeroMiners, WoolyPooly, or 2Miners)
- [ ] Update miner config with real wallet address
- [ ] Start miner in tmux/screen session
- [ ] Set up monitoring (nvidia-smi logging)
- [ ] Record baseline: time, hashrate, temp, power
- [ ] Check pool dashboard after 1h (confirm shares)
- [ ] Daily checks: hashrate stability, earnings, hardware health
- [ ] After 72h: calculate actual ROI vs estimates

---

## Output Artifacts

All files in `~/crypto/profit-run/`:

### Data Files
- ✅ `whattomine_coins.json` — 26KB API data (25 coins)
- ✅ `paper_ranking.md` — Top 10 coin/algo rankings
- ✅ `real_ranking.md` — Benchmark analysis + efficiency rankings

### Scripts
- ✅ `rank_paper.py` — Paper profitability analysis
- ✅ `rank_real.py` — Real benchmark + power analysis

### Documentation
- ✅ `INSTALL_NOTES.md` — Miner installation details
- ✅ `FINAL_REPORT.md` — This report

### Benchmark Results (in `bench_results/`)
- `bench_kawpow_ai1.csv` + `_ai2.csv`
- `bench_autolykos2_ai1.csv` + `_ai2.csv`
- `bench_octopus_ai1.csv` + `_ai2.csv`
- `bench_flux_ai1.csv` + `_ai2.csv`
- `bench_pyrin_ai1.csv` + `_ai2.csv`
- Corresponding `*_output.txt` files with full miner logs

---

## Next Steps

### For 72h Test
1. **Select algorithm** (recommend: Pyrin on RTX 3060)
2. **Create/verify wallet** for chosen coin
3. **Choose pool** and configure connection
4. **Update miner script** with real wallet address
5. **Start mining** in persistent session (tmux/screen)
6. **Monitor closely** for first 6 hours
7. **Daily check-ins** to verify stability
8. **Collect data** after 72h: actual earnings, uptime, avg hashrate

### For Long-Term Mining
- Compare 72h earnings vs estimates → adjust strategy
- Consider dual-mining on separate GPUs
- Implement automatic failover to backup pool
- Set up alerting for hardware issues
- Calculate break-even point vs electricity costs
- Monitor coin profitability weekly and switch if needed

---

## Conclusion

Successfully completed comprehensive mining profitability analysis:
- **5 algorithms benchmarked** across 2 GPUs
- **Clear winner identified:** Pyrin on RTX 3060 (27.8 MH/W)
- **Hardware limitations noted:** GTX 1660 SUPER VRAM constraint
- **Safe for 72h test:** All temps <70°C on recommended config
- **Ready to deploy:** Miners installed, benchmarked, and documented

**Status:** ✅ **Complete and ready for 72-hour production test**

---

**Generated:** 2026-02-16
**Analyst:** Claude Code (Sonnet 4.5)
**Project:** crypto/profit-run
