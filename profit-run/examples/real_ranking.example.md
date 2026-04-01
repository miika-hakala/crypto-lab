# Real Benchmark Results & Profitability Analysis

**GPU Nodes:** RTX 3060 (12GB), GTX 1660 SUPER (6GB)
**Date:** 2026-02-16

## Raw Benchmark Results

| GPU | Algorithm | Coin | Hashrate | Power | Temp | Efficiency |
|-----|-----------|------|----------|-------|------|------------|
| RTX 3060 (12GB) | KawPow | Ravencoin | 9.55 MH/s | 119.0W | 60°C | 0.08 MH/W ✅ |
| RTX 3060 (12GB) | Autolykos2 | Ergo | 103.05 MH/s | 119.0W | 62°C | 0.87 MH/W ✅ |
| RTX 3060 (12GB) | Octopus | Conflux | 80.27 MH/s | 112.0W | 62°C | 0.72 MH/W ✅ |
| RTX 3060 (12GB) | Flux | Flux | 41.10 Sol/s | 111.0W | 61°C | 0.37 SH/W ✅ |
| RTX 3060 (12GB) | Pyrin | Pyrin | 3113.51 MH/s | 112.0W | 62°C | 27.80 MH/W ✅ |
| GTX 1660 SUPER (6GB) | KawPow | Ravencoin | 10.10 MH/s | 78.0W | 75°C | 0.13 MH/W ✅ |
| GTX 1660 SUPER (6GB) | Autolykos2 | Ergo | 49.66 MH/s | 79.0W | 72°C | 0.63 MH/W ✅ |
| GTX 1660 SUPER (6GB) | Octopus | Conflux | 0.00 MH/s | 0.0W | 0°C | 0.00 MH/W ❌ |
| GTX 1660 SUPER (6GB) | Flux | Flux | 17.60 Sol/s | 70.0W | 70°C | 0.25 SH/W ✅ |
| GTX 1660 SUPER (6GB) | Pyrin | Pyrin | 1137.33 MH/s | 74.0W | 77°C | 15.37 MH/W ✅ |

## Ranking 1: Best GPU per Algorithm (by Hashrate)

| Algorithm | Winner | Hashrate | Power | Efficiency | Notes |
|-----------|--------|----------|-------|------------|-------|
| Autolykos2 | **RTX 3060 (12GB)** | 103.05 MH/s | 119W | 0.87 | — |
| Flux | **RTX 3060 (12GB)** | 41.10 Sol/s | 111W | 0.37 | — |
| KawPow | **GTX 1660 SUPER (6GB)** | 10.10 MH/s | 78W | 0.13 | ⚠️ High temp |
| Octopus | **RTX 3060 (12GB)** | 80.27 MH/s | 112W | 0.72 | — |
| Pyrin | **RTX 3060 (12GB)** | 3113.51 MH/s | 112W | 27.80 | 💚 Efficient |

## Ranking 2: Most Efficient (Hashrate per Watt)

| Rank | GPU | Algorithm | Efficiency | Hashrate | Power |
|------|-----|-----------|------------|----------|-------|
| 1 | RTX 3060 (12GB) | Pyrin | **27.80** MH/W | 3113.51 MH/s | 112W |
| 2 | GTX 1660 SUPER (6GB) | Pyrin | **15.37** MH/W | 1137.33 MH/s | 74W |
| 3 | RTX 3060 (12GB) | Autolykos2 | **0.87** MH/W | 103.05 MH/s | 119W |
| 4 | RTX 3060 (12GB) | Octopus | **0.72** MH/W | 80.27 MH/s | 112W |
| 5 | GTX 1660 SUPER (6GB) | Autolykos2 | **0.63** MH/W | 49.66 MH/s | 79W |
| 6 | RTX 3060 (12GB) | Flux | **0.37** SH/W | 41.10 Sol/s | 111W |
| 7 | GTX 1660 SUPER (6GB) | Flux | **0.25** SH/W | 17.60 Sol/s | 70W |
| 8 | GTX 1660 SUPER (6GB) | KawPow | **0.13** MH/W | 10.10 MH/s | 78W |
| 9 | RTX 3060 (12GB) | KawPow | **0.08** MH/W | 9.55 MH/s | 119W |

## Ranking 3: Most Stable (Low Temperature)

| Rank | GPU | Algorithm | Avg Temp | Max Temp | Power | Hashrate |
|------|-----|-----------|----------|----------|-------|----------|
| 1 | RTX 3060 (12GB) | KawPow | 60°C 🟢 | 60°C | 119W | 9.55 MH/s |
| 2 | RTX 3060 (12GB) | Flux | 61°C 🟢 | 61°C | 111W | 41.10 Sol/s |
| 3 | RTX 3060 (12GB) | Pyrin | 62°C 🟢 | 62°C | 112W | 3113.51 MH/s |
| 4 | RTX 3060 (12GB) | Autolykos2 | 62°C 🟢 | 62°C | 119W | 103.05 MH/s |
| 5 | RTX 3060 (12GB) | Octopus | 62°C 🟢 | 62°C | 112W | 80.27 MH/s |
| 6 | GTX 1660 SUPER (6GB) | Flux | 70°C 🟡 | 70°C | 70W | 17.60 Sol/s |
| 7 | GTX 1660 SUPER (6GB) | Autolykos2 | 72°C 🟡 | 72°C | 79W | 49.66 MH/s |
| 8 | GTX 1660 SUPER (6GB) | KawPow | 75°C 🔴 | 75°C | 78W | 10.10 MH/s |
| 9 | GTX 1660 SUPER (6GB) | Pyrin | 77°C 🔴 | 77°C | 74W | 1137.33 MH/s |

## Summary & 72h Test Recommendation

### 🏆 Recommended: Pyrin (Pyrin)

**Hardware:** RTX 3060 (12GB)
**Hashrate:** 3113.51 MH/s
**Power Consumption:** 112.0W
**Temperature:** 62°C (max 62°C)
**Efficiency:** 27.80 MH/W

**Rationale:**
- Excellent power efficiency (27.80 MH/W)
- Low operating temperature (62°C) = long-term stability
- RTX 3060 has 12GB VRAM for future flexibility

**Alternative options:**
2. **Pyrin** on GTX 1660 SUPER (6GB): 1137.33 MH/s, 74W, 77°C
3. **KawPow** on RTX 3060 (12GB): 9.55 MH/s, 119W, 60°C
4. **KawPow** on GTX 1660 SUPER (6GB): 10.10 MH/s, 78W, 75°C

## Important Notes

1. **GTX 1660 SUPER Octopus FAIL:** Insufficient VRAM (6GB < requirement)
2. **Power Limits Active:** gpu-node-1=120W, gpu-node-2=80W (hardware throttled)
3. **Profitability estimates** are based on WhatToMine data and may vary with:
   - Network difficulty changes
   - Cryptocurrency price fluctuations
   - Pool fees and payout methods
4. **72h test** should monitor:
   - Actual shares accepted vs rejected
   - Pool-reported hashrate stability
   - Hardware stability and temperature trends
   - Actual earnings vs estimates

---

**Next Step:** Configure chosen algorithm for 72h production test with real wallet address.
