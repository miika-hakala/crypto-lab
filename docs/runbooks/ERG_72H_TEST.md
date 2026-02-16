# ERG_72H_TEST — Ergo Mining 72-Hour Production Test

## Purpose

Validate real-world mining profitability and stability for Ergo (ERG) using Autolykos2 algorithm across both GPU nodes (ai-1 + ai-2) over a continuous 72-hour period.

**Target metrics:**
- Actual revenue/day vs estimated (~$0.50-0.80/day)
- Pool-reported hashrate stability vs benchmark (152.71 MH/s combined)
- Hardware stability (temps <75°C, no throttling)
- Share acceptance rate (>95%)
- Power consumption consistency

---

## Preconditions

### Hardware
- ✅ ai-1 (RTX 3060 12GB) power limit: **120W**
- ✅ ai-2 (GTX 1660 SUPER 6GB) power limit: **80W**
- ✅ Both GPUs idle before test start
- ✅ Temps <55°C at idle

**Verify power limits:**
```bash
# ai-1
ssh miika@ai-1 'nvidia-smi -q -d POWER | grep "Power Limit"'
# Expected: 120.00 W

# ai-2
ssh miika@ai-2 'nvidia-smi -q -d POWER | grep "Power Limit"'
# Expected: 80.00 W
```

### Software
- ✅ lolMiner v1.98a installed: `~/crypto/miners/lolminer/lolMiner`
- ✅ tmux installed on both nodes: `which tmux`
- ✅ No other GPU processes running (check: `nvidia-smi`)

### Wallet & Pool
- ⚠️ **Ergo wallet address required** (see Wallet Setup below)
- ✅ Pool: HeroMiners Ergo (`ergo.herominers.com:1180`)

---

## Wallet Setup

**IMPORTANT:** Create an Ergo wallet BEFORE starting the test.

### Recommended Wallets

1. **Nautilus Wallet** (browser extension) — RECOMMENDED
   - Website: https://nautilus.com
   - Supports: Chrome, Firefox, Brave
   - Quick setup, easy address export

2. **Ergo Mobile Wallet** (official)
   - iOS/Android app stores
   - Backup seed phrase offline (NOT on cluster)

**⚠️ CORRECTION:** Yoroi wallet does **NOT** support Ergo. Do not use Yoroi for this test.

### Security Rules

1. ✅ **ONLY** store public receive address on cluster
2. ❌ **NEVER** store seed phrase or private keys in any file
3. ❌ **NEVER** commit wallet addresses to git
4. ✅ Use placeholder in runbook examples: `YOUR_ERGO_WALLET_ADDRESS`

**Export wallet address:**
- Nautilus: Click "Receive" → copy address (starts with `9`)
- Mobile: Tap "Receive" → copy address

---

## Expected Performance (from benchmarks)

| Node | GPU | Hashrate | Power | Temp | Efficiency |
|------|-----|----------|-------|------|------------|
| ai-1 | RTX 3060 | 103.05 MH/s | 119W | 62°C | 0.87 MH/W |
| ai-2 | GTX 1660 S | 49.66 MH/s | 79W | 72°C | 0.63 MH/W |
| **TOTAL** | — | **152.71 MH/s** | **198W** | — | **0.77 MH/W** |

**Revenue estimate:**
- Pool: ~$0.50-0.80/day (before pool fees, 1-2%)
- Electricity: ~$0.48/day (@$0.10/kWh, 4.75 kWh/day)
- **Net: ~$0.02-0.32/day**

---

## Start Mining

### Step 1: Start ai-1 (RTX 3060)

```bash
ssh miika@ai-1

# Create tmux session
tmux new -s ergo-mining

# Start lolMiner
cd ~/crypto/miners/lolminer
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user YOUR_ERGO_WALLET_ADDRESS.ai1 \
  --pass x

# Detach: Ctrl+B, then D
```

**Verify startup:**
- Wait 30-60 seconds for DAG generation
- Should see: "Subscribed to stratum server"
- Should see: "GPU 0: RTX 3060" with ~103 MH/s
- Should see: "Accepted share" within 5 minutes

### Step 2: Start ai-2 (GTX 1660 SUPER)

```bash
ssh miika@ai-2

# Create tmux session
tmux new -s ergo-mining

# Start lolMiner
cd ~/crypto/miners/lolminer
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user YOUR_ERGO_WALLET_ADDRESS.ai2 \
  --pass x

# Detach: Ctrl+B, then D
```

**Verify startup:**
- Should see: "GPU 0: GTX 1660 SUPER" with ~49 MH/s
- Temperature should stay <75°C

### Step 3: Check Pool Dashboard

- Visit: https://ergo.herominers.com
- Search: `YOUR_ERGO_WALLET_ADDRESS`
- After 15-30 min: should see workers `ai1` and `ai2`
- Reported hashrate: ~152 MH/s (±10% variance normal)

---

## Monitoring

### First 6 Hours — Intensive Monitoring

**Every 30 minutes:**
```bash
# ai-1 quick check
ssh miika@ai-1 'tmux attach -t ergo-mining'
# Look for: hashrate stable, no errors, temp <65°C
# Detach: Ctrl+B, D

# ai-2 quick check
ssh miika@ai-2 'tmux attach -t ergo-mining'
# Look for: hashrate stable, temp <75°C
# Detach: Ctrl+B, D
```

**GPU stats:**
```bash
# ai-1
ssh miika@ai-1 'nvidia-smi --query-gpu=temperature.gpu,power.draw,utilization.gpu --format=csv,noheader'
# Expected: ~62°C, ~119W, ~100%

# ai-2
ssh miika@ai-2 'nvidia-smi --query-gpu=temperature.gpu,power.draw,utilization.gpu --format=csv,noheader'
# Expected: ~72°C, ~79W, ~100%
```

**Pool stats:**
- Check dashboard every 2 hours
- Verify: hashrate stable (~152 MH/s ±10%)
- Verify: shares being accepted (>95% acceptance)

### After 6h — Daily Checks

**Once per day (same time):**
1. Check pool dashboard: hashrate, workers online, earnings
2. SSH check temps (nvidia-smi)
3. View miner logs (tmux attach)
4. Record: daily earnings, avg hashrate, any errors

**Daily log template:**
```
Day X/3:
- Pool hashrate: ___ MH/s
- ai-1 temp: ___°C, power: ___W
- ai-2 temp: ___°C, power: ___W
- Shares: ___ accepted, ___ rejected (___% acceptance)
- Earnings (24h): $___.__ USD
- Issues: [none / describe]
```

---

## Stop Conditions — IMMEDIATE SHUTDOWN

**Stop mining immediately if ANY of these occur:**

1. ❌ **GPU temp >80°C sustained** (>5 minutes)
2. ❌ **Share rejection rate >10%** (>100 rejects in 1000 shares)
3. ❌ **Pool disconnects repeatedly** (>5 disconnects/hour)
4. ❌ **Miner crashes** or GPU driver errors
5. ❌ **Hardware artifacts** (screen glitches, system instability)
6. ❌ **Power draw exceeds limit** (ai-1 >125W, ai-2 >85W sustained)

**Emergency stop:**
```bash
# ai-1
ssh miika@ai-1 'tmux kill-session -t ergo-mining'

# ai-2
ssh miika@ai-2 'tmux kill-session -t ergo-mining'

# Verify GPUs idle
ssh miika@ai-1 'nvidia-smi'
ssh miika@ai-2 'nvidia-smi'
```

---

## Normal Shutdown (after 72h)

### Step 1: Stop miners gracefully

```bash
# ai-1
ssh miika@ai-1 'tmux attach -t ergo-mining'
# Press Ctrl+C to stop miner
# Type: exit
# Detach: Ctrl+B, D

# ai-2
ssh miika@ai-2 'tmux attach -t ergo-mining'
# Press Ctrl+C
# Type: exit
```

### Step 2: Kill tmux sessions

```bash
ssh miika@ai-1 'tmux kill-session -t ergo-mining'
ssh miika@ai-2 'tmux kill-session -t ergo-mining'
```

### Step 3: Verify GPUs idle

```bash
ssh miika@ai-1 'nvidia-smi'
ssh miika@ai-2 'nvidia-smi'
# Expected: 0% GPU util, <20W power, <55°C temp
```

---

## 72h Closeout Checklist

After stopping miners, collect final data:

### Pool Dashboard
- [ ] Final total earnings (USD)
- [ ] Final total earnings (ERG)
- [ ] Average reported hashrate (72h)
- [ ] Total shares accepted
- [ ] Total shares rejected
- [ ] Rejection rate (%)
- [ ] Effective hashrate vs reported

### Hardware Performance
- [ ] ai-1 average temp (from pool dashboard or logs)
- [ ] ai-2 average temp
- [ ] ai-1 average power draw
- [ ] ai-2 average power draw
- [ ] Any thermal throttling events?
- [ ] Any driver crashes?
- [ ] Total uptime (should be ~72h)

### Financial Analysis
- [ ] Gross revenue: $___.__
- [ ] Pool fee (1-2%): $___.__
- [ ] Net revenue: $___.__
- [ ] Electricity cost: $___.__
- [ ] **Net profit/loss: $___.__**
- [ ] Profit per day: $___.__
- [ ] Monthly projection: $___.__

### Comparison to Estimates
| Metric | Estimated | Actual | Variance |
|--------|-----------|--------|----------|
| Revenue/day | $0.50-0.80 | $____ | ___% |
| Hashrate | 152.71 MH/s | ____ MH/s | ___% |
| ai-1 temp | 62°C | ____°C | ___°C |
| ai-2 temp | 72°C | ____°C | ___°C |
| ai-1 power | 119W | ____W | ___W |
| ai-2 power | 79W | ____W | ___W |

### Decision
- [ ] Continue mining Ergo? (Yes / No)
- [ ] Switch to different coin? (specify: _____)
- [ ] Stop mining entirely? (Yes / No)
- [ ] Adjust power limits? (new limits: ai-1=___W, ai-2=___W)

---

## View Logs & Status

### View live miner output
```bash
# ai-1
ssh miika@ai-1 'tmux attach -t ergo-mining'
# Detach: Ctrl+B, D

# ai-2
ssh miika@ai-2 'tmux attach -t ergo-mining'
```

### Check if mining is running
```bash
ssh miika@ai-1 'pgrep -af lolMiner'
ssh miika@ai-2 'pgrep -af lolMiner'
# Should show: lolMiner process if running
```

### GPU quick status
```bash
ssh miika@ai-1 'nvidia-smi --query-gpu=name,temperature.gpu,power.draw,utilization.gpu --format=csv'
ssh miika@ai-2 'nvidia-smi --query-gpu=name,temperature.gpu,power.draw,utilization.gpu --format=csv'
```

---

## Troubleshooting

### Miner won't start
- Check: wallet address correct? (starts with `9`, 51+ chars)
- Check: pool reachable? `ping ergo.herominers.com`
- Check: GPU idle? `nvidia-smi` should show 0% util before start
- Check: lolMiner binary exists? `ls -lh ~/crypto/miners/lolminer/lolMiner`

### Low hashrate
- Wait 5-10 min for warmup
- Check: power limit applied? (nvidia-smi -q -d POWER)
- Check: thermal throttling? (temp >75°C on ai-2)
- Restart miner if persistent

### High rejection rate
- Check: system clock accurate? `date` (should be NTP synced)
- Check: network latency? `ping ergo.herominers.com` (<100ms)
- If >5% rejects: try different pool (e.g., 2miners: erg.2miners.com:8888)

### Pool not showing workers
- Wait 15-30 minutes (pool reporting lag)
- Check: wallet address exact match on dashboard search
- Check: miner connected? (tmux attach, look for "Subscribed to stratum")

### GPU temperature too high
- ai-1: should stay <65°C (if >70°C, investigate cooling)
- ai-2: 72-75°C normal (if >77°C, reduce power limit to 75W)

**Reduce ai-2 power limit:**
```bash
ssh miika@ai-2 'sudo nvidia-smi -pl 75'
# Restart miner after power limit change
```

---

## References

- Benchmark report: `~/crypto/profit-run/FINAL_REPORT.md`
- Profitability analysis: `~/crypto/profit-run/TOP3_PROFIT.md`
- HeroMiners Ergo pool: https://ergo.herominers.com
- lolMiner documentation: https://github.com/Lolliedieb/lolMiner-releases

---

**Status:** Ready for execution (pending wallet address)
**Created:** 2026-02-16
**Owner:** crypto-lab
