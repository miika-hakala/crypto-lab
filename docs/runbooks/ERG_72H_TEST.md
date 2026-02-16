# Ergo 72h Mining Test — EXP-001

**Purpose:** Execute controlled 72-hour Ergo (Autolykos2) mining test on gpu-node-1 and gpu-node-2 to validate profitability estimates and system stability.

**Experiment ID:** EXP-001
**Date:** 2026-02-16
**Status:** Planned (awaiting wallet creation)
**Duration:** 72 hours continuous
**Algorithm:** Autolykos2 (Ergo)
**Pool:** HeroMiners (ergo.herominers.com:1180)

---

## ⚠️ CRITICAL PREREQUISITES

### STOP — Do Not Proceed Unless:
- ✅ **Ergo wallet created** (see `ERG_WALLET_CREATION.md`)
- ✅ **Seed phrase backed up offline** (paper, secure location)
- ✅ **Wallet recovery tested** (verified you can restore)
- ✅ **Receive address obtained** (starts with `9`, ~50-60 characters)
- ✅ **NO seed phrase or private keys on mining nodes**
- ✅ **ONLY public receive address will be used in mining config**

**If any of the above is incomplete, STOP and complete wallet creation first.**

---

## Preconditions Checklist

### Hardware Access:
- [ ] gpu-node-1 reachable via SSH
- [ ] gpu-node-2 reachable via SSH
- [ ] Both nodes idle (not running other mining operations)
- [ ] GPU temps at idle baseline (<50°C gpu-node-1, <40°C gpu-node-2)

### Software Installed:
- [ ] lolMiner v1.98a installed at `~/crypto/miners/lolminer/` on both nodes
- [ ] tmux installed on both nodes (`which tmux`)
- [ ] nvidia-smi available (`nvidia-smi` works)

### Power Limits Configured:
```bash
# gpu-node-1 (RTX 3060) — 120W limit
ssh gpu-node-1 "sudo nvidia-smi -i 0 -pl 120"

# gpu-node-2 (GTX 1660 SUPER) — 80W limit
ssh gpu-node-2 "sudo nvidia-smi -i 0 -pl 80"

# Verify limits applied
ssh gpu-node-1 "nvidia-smi --query-gpu=power.limit --format=csv,noheader"
ssh gpu-node-2 "nvidia-smi --query-gpu=power.limit --format=csv,noheader"
```

**Expected output:**
- gpu-node-1: `120.00 W`
- gpu-node-2: `80.00 W`

- [ ] Power limits verified

### Pool Connectivity:
```bash
# Test pool reachability (from control-node or either gpu-node)
nc -zv ergo.herominers.com 1180
```

**Expected:** `Connection to ergo.herominers.com 1180 port [tcp/*] succeeded!`

- [ ] Pool reachable

### Wallet Address Ready:
- [ ] Ergo receive address copied (starts with `9`)
- [ ] Address verified in wallet (matches exactly)
- [ ] Address length ~50-60 characters
- [ ] **NO seed phrase or private keys in mining config**

---

## Pool Configuration

**Pool:** HeroMiners Ergo
**URL:** `stratum+tcp://ergo.herominers.com:1180`
**Protocol:** Stratum (SSL/TLS available on port 11180 if preferred)
**Payment Threshold:** 1.0 ERG (configurable in pool dashboard)
**Worker Naming:** `ERG_WALLET_ADDRESS_HERE.ai1` and `.ai2`

**Pool Dashboard:**
After mining starts, monitor at: `https://ergo.herominers.com/?address=YOUR_WALLET_ADDRESS`

---

## Start Procedure

### Step 1: Prepare Miner Commands

**IMPORTANT:** Replace `ERG_WALLET_ADDRESS_HERE` with your actual Ergo receive address (from wallet).

**gpu-node-1 command:**
```bash
cd ~/crypto/miners/lolminer
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user ERG_WALLET_ADDRESS_HERE.ai1 \
  --pass x \
  --watchdog exit \
  --apiport 0 \
  --digits 2
```

**gpu-node-2 command:**
```bash
cd ~/crypto/miners/lolminer
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user ERG_WALLET_ADDRESS_HERE.ai2 \
  --pass x \
  --watchdog exit \
  --apiport 0 \
  --digits 2
```

**Flag explanations:**
- `--algo AUTOLYKOS2` — Ergo's mining algorithm
- `--pool` — Pool URL with stratum protocol
- `--user` — Wallet address + worker name (`.ai1` or `.ai2`)
- `--pass x` — Pool password (usually `x` for public pools)
- `--watchdog exit` — Exit on critical error (prevents runaway GPU usage)
- `--apiport 0` — Disable API (not needed for this test)
- `--digits 2` — Show 2 decimal places in hashrate

---

### Step 2: Start gpu-node-1 Mining

```bash
# SSH to gpu-node-1
ssh gpu-node-1

# Verify power limit
nvidia-smi --query-gpu=power.limit --format=csv,noheader

# Create tmux session
tmux new -s ergo-ai1

# Inside tmux, navigate to miner directory
cd ~/crypto/miners/lolminer

# Start mining (REPLACE ERG_WALLET_ADDRESS_HERE with your address!)
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user ERG_WALLET_ADDRESS_HERE.ai1 \
  --pass x \
  --watchdog exit \
  --apiport 0 \
  --digits 2
```

**After starting:**
1. Observe initial output (pool connection, GPU detection)
2. Wait for "Accepted share" message (should appear within 1-2 minutes)
3. **Detach from tmux:** Press `Ctrl+b`, then `d`
4. Exit SSH (miner keeps running in tmux)

**Reattach later:**
```bash
ssh gpu-node-1
tmux attach -t ergo-ai1
```

---

### Step 3: Start gpu-node-2 Mining

```bash
# SSH to gpu-node-2
ssh gpu-node-2

# Verify power limit
nvidia-smi --query-gpu=power.limit --format=csv,noheader

# Create tmux session
tmux new -s ergo-ai2

# Inside tmux, navigate to miner directory
cd ~/crypto/miners/lolminer

# Start mining (REPLACE ERG_WALLET_ADDRESS_HERE with your address!)
./lolMiner --algo AUTOLYKOS2 \
  --pool stratum+tcp://ergo.herominers.com:1180 \
  --user ERG_WALLET_ADDRESS_HERE.ai2 \
  --pass x \
  --watchdog exit \
  --apiport 0 \
  --digits 2
```

**After starting:**
1. Observe initial output
2. Wait for "Accepted share"
3. **Detach from tmux:** Press `Ctrl+b`, then `d`
4. Exit SSH

---

### Step 4: Record Start Time

**EXP-001 Start:**
- Date/Time: ________________
- gpu-node-1 tmux session: `ergo-ai1`
- gpu-node-2 tmux session: `ergo-ai2`
- Pool: HeroMiners (ergo.herominers.com:1180)
- Worker names: `.ai1`, `.ai2`

**Target End:** 72 hours from start

---

## Monitoring — First 30-60 Minutes (CRITICAL)

**This is the most important monitoring period.** Issues typically appear in the first hour.

### Immediate Checks (First 5 Minutes):

**For EACH node (gpu-node-1 and gpu-node-2):**

1. **Pool Connection:**
   - [ ] "Connected to pool" message appears
   - [ ] No repeated connection failures
   - [ ] No firewall/network errors

2. **First Share Accepted:**
   - [ ] "Accepted share" message within 1-2 minutes
   - [ ] Share counter incrementing
   - [ ] **NO "Rejected share" messages**

3. **GPU Detection:**
   - [ ] Correct GPU detected (RTX 3060 on gpu-node-1, GTX 1660 SUPER on gpu-node-2)
   - [ ] Hashrate displayed (should match benchmark)
   - [ ] Power draw within limits (120W / 80W)

4. **Temperature Baseline:**
   ```bash
   # Check temps (while tmux detached)
   ssh gpu-node-1 "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
   ssh gpu-node-2 "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
   ```
   - [ ] gpu-node-1: <75°C
   - [ ] gpu-node-2: <65°C

---

### 30-Minute Check:

**Hashrate Stability:**
- [ ] gpu-node-1: ~103 MH/s (Autolykos2, per benchmark)
- [ ] gpu-node-2: ~50 MH/s (Autolykos2, per benchmark)
- [ ] Hashrate not fluctuating wildly (±5% is normal)

**Accepted vs Rejected Shares:**
- [ ] Rejection rate <2% (ideally 0%)
- [ ] If rejections >5%, investigate (pool latency? overclock unstable?)

**Temperatures:**
- [ ] gpu-node-1: stabilized (65-75°C expected)
- [ ] gpu-node-2: stabilized (55-65°C expected)
- [ ] **NO thermal throttling warnings**

**Power Draw:**
- [ ] gpu-node-1: ~119W (at or below 120W limit)
- [ ] gpu-node-2: ~79W (at or below 80W limit)

**Pool Dashboard:**
- [ ] Visit `https://ergo.herominers.com/?address=YOUR_WALLET_ADDRESS`
- [ ] Both workers (`.ai1`, `.ai2`) show as online
- [ ] Hashrate displayed matches miner output

---

### 60-Minute Check:

**Earnings Started:**
- [ ] Pool dashboard shows pending balance >0
- [ ] Estimated earnings per 24h displayed
- [ ] Compare estimate to profitability analysis (from profit-run/)

**Stability:**
- [ ] No miner crashes or restarts
- [ ] tmux sessions still active (`tmux ls` on each node)
- [ ] No error messages in miner output

**Decision Point:**
- ✅ **If all checks pass:** Continue to daily monitoring
- ⚠️ **If issues detected:** See "Stop Conditions" section below

---

## Daily Monitoring (Days 1, 2, 3)

**Perform once per day (same time each day for consistency):**

### Daily Checklist:

**1. Miner Uptime:**
```bash
# Check tmux sessions exist
ssh gpu-node-1 "tmux ls"
ssh gpu-node-2 "tmux ls"
```
- [ ] `ergo-ai1` session running on gpu-node-1
- [ ] `ergo-ai2` session running on gpu-node-2

**2. Hashrate Check:**
- [ ] Reattach to tmux, verify hashrate matches expected
- [ ] No significant degradation (<10% drop)

**3. Share Stats:**
- [ ] Check accepted share count (incrementing)
- [ ] Rejection rate still <2%

**4. Temperature Trend:**
```bash
ssh gpu-node-1 "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
ssh gpu-node-2 "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
```
- [ ] gpu-node-1: <75°C
- [ ] gpu-node-2: <65°C (CRITICAL: watch for creep on GTX 1660 S)
- [ ] **STOP if gpu-node-2 >78°C sustained** (see Stop Conditions)

**5. Pool Dashboard:**
- [ ] Both workers online
- [ ] Pending balance increasing
- [ ] No "offline" warnings

**6. Earnings Tracking:**
- [ ] Record current pending balance: _______ ERG
- [ ] Compare to estimate (is actual higher or lower?)
- [ ] Note any deviations for closeout analysis

**7. System Health:**
- [ ] No unexpected reboots
- [ ] SSH access still working
- [ ] No network issues

---

## Stop Conditions (Emergency / Planned)

### IMMEDIATE STOP — Critical Issues:

**1. Temperature Excursion:**
- **Trigger:** gpu-node-2 >78°C sustained for >5 minutes
- **Action:** Stop miner immediately, investigate cooling

**2. Thermal Throttling:**
- **Trigger:** nvidia-smi shows GPU clock dropping due to heat
- **Action:** Stop miner, reduce power limit, or improve airflow

**3. High Rejection Rate:**
- **Trigger:** >10% rejected shares sustained
- **Action:** Check pool latency, verify network stability, consider different pool

**4. Miner Crashes:**
- **Trigger:** Miner exits unexpectedly >2 times per day
- **Action:** Check logs, verify GPU stability, reduce overclock if any

**5. Hardware Errors:**
- **Trigger:** nvidia-smi reports GPU errors or memory errors
- **Action:** STOP immediately, run diagnostics

**6. Pool Issues:**
- **Trigger:** Pool offline >1 hour, or payment issues reported
- **Action:** Switch to backup pool or pause test

---

### PLANNED STOP — 72h Complete:

**After 72 hours:**

```bash
# Stop gpu-node-1
ssh gpu-node-1
tmux attach -t ergo-ai1
# Press Ctrl+C to stop miner gracefully
# Wait for "Shutting down" message
exit

# Stop gpu-node-2
ssh gpu-node-2
tmux attach -t ergo-ai2
# Press Ctrl+C to stop miner
exit
```

**Record stop time:** _______________

---

## 72h Closeout Procedure

### Step 1: Final Data Collection

**Earnings:**
- [ ] Pool dashboard: Final pending balance: _______ ERG
- [ ] Pool dashboard: Total shares accepted: _______
- [ ] Pool dashboard: Total shares rejected: _______
- [ ] Rejection rate: _______% (should be <2%)

**Performance Metrics:**

**gpu-node-1 (RTX 3060):**
- [ ] Average hashrate over 72h: _______ MH/s (from pool dashboard)
- [ ] Average power draw: _______ W (from daily checks)
- [ ] Average temperature: _______ °C
- [ ] Peak temperature: _______ °C
- [ ] Uptime: _______ hours (should be ~72h)

**gpu-node-2 (GTX 1660 SUPER):**
- [ ] Average hashrate over 72h: _______ MH/s
- [ ] Average power draw: _______ W
- [ ] Average temperature: _______ °C
- [ ] Peak temperature: _______ °C
- [ ] Uptime: _______ hours

---

### Step 2: Profitability Calculation

**Electricity Cost (if applicable):**
- Total energy used: (120W + 80W) × 72h = 14.4 kWh
- Cost per kWh: $_______ (if tracking)
- Total electricity cost: $_______

**Revenue:**
- Total ERG earned: _______ ERG
- ERG price at test end: $_______ per ERG (from CoinGecko/exchange)
- Total revenue: $_______

**Net Profit (72h):**
- Revenue - Electricity = $_______

**Daily Average:**
- Net profit per day: $_______ (72h total ÷ 3)
- Daily revenue: $_______ (before electricity)

**Comparison to Estimate:**
- Estimated daily (from profit-run/): $_______
- Actual daily: $_______
- Variance: _______% (positive = better than expected)

---

### Step 3: Performance vs Benchmark

**gpu-node-1 Hashrate:**
- Benchmark (3 min test): 103.05 MH/s
- 72h average: _______ MH/s
- Difference: _______% (should be within ±5%)

**gpu-node-2 Hashrate:**
- Benchmark (3 min test): 49.66 MH/s
- 72h average: _______ MH/s
- Difference: _______% (should be within ±5%)

**Interpretation:**
- If 72h average is lower than benchmark, investigate: thermal throttling, pool latency, hardware degradation
- If 72h average matches benchmark (±5%), system is stable

---

### Step 4: Stability Assessment

**Downtime:**
- Total uptime: _______ hours (out of 72h)
- Uptime percentage: _______%
- **Target:** >95% (68.4 hours minimum)

**Crashes/Restarts:**
- Number of miner crashes: _______
- Number of manual restarts: _______
- **Target:** Zero (or <2 for acceptable)

**Temperature Issues:**
- Peak temp gpu-node-1: _______ °C (max acceptable: 80°C)
- Peak temp gpu-node-2: _______ °C (max acceptable: 75°C)
- Any thermal throttling events: Yes / No

**Pool/Network Issues:**
- Pool disconnections: _______
- Network errors: _______
- **Target:** Zero (or minimal)

---

### Step 5: Go/No-Go Decision

**Decision Criteria:**

**✅ GO (Continue Mining Ergo):**
- Daily net profit >$0 (after electricity if tracked)
- Uptime >95%
- No critical thermal issues
- Earnings match or exceed estimate (within 20%)
- System stable (no crashes)

**⚠️ ADJUST (Continue with Changes):**
- Profitability marginal but positive
- Minor stability issues (addressable with tuning)
- Consider: reduce power limits, switch pools, adjust overclock

**❌ NO-GO (Switch Algorithm/Coin):**
- Daily net profit ≤$0 (or below threshold)
- Earnings significantly below estimate (>30% worse)
- Persistent stability issues
- High rejection rate (>5%)
- Thermal problems unresolved

**Record Decision:** ___________________

**Reasoning:** ___________________________________________________________

---

### Step 6: Update Documentation

**After 72h test, update these files:**

1. **docs/EXPERIMENT_LOG.md:**
   - Fill in EXP-001 results section
   - Record all metrics (earnings, hashrate, temps, uptime)
   - Document any issues encountered
   - Record go/no-go decision

2. **docs/STATUS.md:**
   - Update Mining Status: ⏸️ Not Started → ✅ 72h Test Complete
   - Update Financial Status: Total Earned, Pending Payouts
   - Update Risk Dashboard if thermal or stability issues occurred

3. **docs/DECISIONS.md:**
   - If decision is GO: Document as new ADR (continue Ergo mining)
   - If decision is NO-GO: Document decision to switch algorithm
   - If decision is ADJUST: Document tuning changes

---

## Troubleshooting

### "Pool not connecting"
- Check firewall: `sudo ufw status` (should allow outbound on port 1180)
- Test pool: `nc -zv ergo.herominers.com 1180`
- Try alternate port: 11180 (SSL) or 1180 (standard)
- Check pool status: https://ergo.herominers.com/

### "High rejection rate (>5%)"
- Check pool latency: `ping ergo.herominers.com` (should be <100ms)
- Switch to geographically closer pool if available
- Verify GPU stability (reduce overclock if applied)
- Check for network issues (packet loss)

### "Hashrate lower than benchmark"
- Check thermal throttling: nvidia-smi (GPU clock should be stable)
- Verify power limit still applied: `nvidia-smi --query-gpu=power.limit`
- Check GPU utilization: should be near 100%
- Reboot node and restart miner

### "Miner crashes repeatedly"
- Check logs in tmux session for error messages
- Verify lolMiner version: `./lolMiner --version` (should be 1.98a)
- Test with reduced power limit (110W / 70W)
- Check for GPU hardware errors: `nvidia-smi -q | grep -i error`

### "Temperature rising above limits"
- Verify power limit enforced: `nvidia-smi -pl 80` (gpu-node-2)
- Check ambient temperature (room too hot?)
- Verify GPU fans working: `nvidia-smi --query-gpu=fan.speed`
- Consider stopping test if >78°C sustained on gpu-node-2

### "Earnings not appearing in pool dashboard"
- Wait 15-30 minutes (pool updates delayed)
- Verify wallet address entered correctly (starts with `9`)
- Check worker names show as online
- Ensure shares are being accepted (check miner output)

### "Cannot reattach to tmux session"
- List sessions: `tmux ls`
- If session missing, miner stopped (check why)
- If session exists but won't attach, try: `tmux attach -t ergo-ai1 -d`
- Worst case: kill and restart miner

---

## Safety Reminders

**Throughout the 72h test:**

- ❌ **NEVER** enter seed phrase on mining nodes
- ❌ **NEVER** store wallet backup on mining nodes
- ❌ **NEVER** run miners as root/sudo
- ✅ **ONLY** use public receive address in miner config
- ✅ **ALWAYS** enforce power limits (120W / 80W)
- ✅ **MONITOR** temperatures daily (especially gpu-node-2)
- ✅ **STOP** mining if temperatures exceed 78°C sustained

**If you notice anything suspicious:**
- Stop mining immediately
- Document the issue
- Do NOT restart until root cause identified

---

## Post-Test Cleanup

**After test completes and data recorded:**

1. **Terminate tmux sessions:**
   ```bash
   ssh gpu-node-1 "tmux kill-session -t ergo-ai1"
   ssh gpu-node-2 "tmux kill-session -t ergo-ai2"
   ```

2. **Verify GPUs idle:**
   ```bash
   ssh gpu-node-1 "nvidia-smi"
   ssh gpu-node-2 "nvidia-smi"
   ```
   - GPU utilization should be 0%
   - Temps should return to idle (<50°C / <40°C)

3. **Wait for pool payout:**
   - Minimum payout threshold: 1.0 ERG (default)
   - Check wallet for incoming transaction
   - Confirm payout in blockchain explorer: https://explorer.ergoplatform.com/

4. **Archive test data:**
   - Save pool dashboard screenshot
   - Export earnings CSV if available
   - Update EXPERIMENT_LOG.md with final results

---

## Next Experiment

**If EXP-001 decision is GO:**
- Continue mining Ergo long-term
- Proceed to Phase 3 (Optimization)
- Consider auto-switcher implementation

**If EXP-001 decision is NO-GO:**
- Select next algorithm from profit-run/ ranking
- Create wallet for new cryptocurrency
- Plan EXP-002 (72h test on new algorithm)

**If EXP-001 decision is ADJUST:**
- Implement tuning changes (power limits, pool, etc.)
- Run EXP-001b (72h retest with adjustments)
- Compare results before final decision

---

## References

- **Ergo Wallet Creation:** `ERG_WALLET_CREATION.md` (this directory)
- **Pool Stats:** https://ergo.herominers.com/
- **Ergo Explorer:** https://explorer.ergoplatform.com/
- **Profitability Data:** `../../profit-run/` (paper and real rankings)
- **Safety Protocols:** `../SAFETY.md`
- **Experiment Log:** `../EXPERIMENT_LOG.md`

---

**Runbook Version:** 1.0
**Created:** 2026-02-16
**For:** EXP-001 (72h Ergo mining test)
**Scope:** gpu-node-1 (RTX 3060) + gpu-node-2 (GTX 1660 SUPER)
**Safety Level:** 🔒 Maximum (no private keys on nodes)
