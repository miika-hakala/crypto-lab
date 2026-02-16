# Safety & Security Protocols — crypto-lab

**Version:** 1.0
**Last Updated:** 2026-02-16
**Criticality:** MANDATORY

---

## Purpose

This document defines **mandatory** safety and security protocols for all cryptocurrency mining experiments in crypto-lab. Violation of these protocols may result in immediate project termination.

---

## Security Protocols

### 1. Key and Seed Management

#### FORBIDDEN ❌

**Never, under any circumstances:**
- ❌ Store private keys on mining nodes (ai-1, ai-2, dev-main)
- ❌ Store seed phrases in files, environment variables, or configuration
- ❌ Commit private keys to git (even in "deleted" commits)
- ❌ Share private keys over SSH, Slack, or any communication channel
- ❌ Store unencrypted wallet files on cluster nodes
- ❌ Use the same wallet for testing and production
- ❌ Create wallets on nodes with internet-facing services

#### REQUIRED ✅

**Mandatory practices:**
- ✅ Private keys stored on **offline device** only (hardware wallet or air-gapped machine)
- ✅ Seed phrases written on paper, stored in secure physical location
- ✅ Mining nodes only have **public receiving addresses**
- ✅ Wallet backups encrypted and stored separately from primary
- ✅ Test wallet with small amounts before committing to long-term use
- ✅ Separate wallets for different experiments (if significant funds involved)

#### Wallet Setup Checklist

Before mining:
- [ ] Wallet created on secure offline device
- [ ] Seed phrase written down (12-24 words)
- [ ] Seed phrase verified by restoring wallet
- [ ] Seed phrase stored in secure physical location
- [ ] Public address verified (receive test transaction)
- [ ] Only public address added to miner config
- [ ] Backup procedure documented

#### Supported Wallets by Cryptocurrency

**Ergo (ERG) — For 72h Test:**
- ✅ **Nautilus Wallet** (browser extension, recommended) — https://nautilus.com
- ✅ **Ergo Mobile Wallet** (official iOS/Android app)
- ✅ **Ergo Desktop Wallet** (full node, advanced users)
- ❌ **Yoroi Wallet** — Does NOT support Ergo (Cardano only, common mistake)

**Ravencoin (RVN):**
- ✅ **Ravencoin Core** (official desktop wallet)
- ✅ **Trust Wallet** (mobile)
- ✅ **Exodus** (multi-currency)

**Pyrin (PYI):**
- ✅ **Pyrin Desktop Wallet** (official)
- ✅ **pyrinwallet** (CLI, requires full node)

**IMPORTANT:** Always verify wallet compatibility before creating. Yoroi is frequently confused with Ergo wallets but does NOT support ERG.

---

### 2. SSH and Network Security

#### SSH Configuration

**Required settings on all nodes:**

```bash
# /etc/ssh/sshd_config (or user ~/.ssh/config)
StrictHostKeyChecking yes           # MANDATORY
PasswordAuthentication no           # Key-based only
PubkeyAuthentication yes
PermitRootLogin no                  # No root SSH
```

**Never:**
- ❌ Disable StrictHostKeyChecking (even temporarily)
- ❌ Use password authentication
- ❌ Share SSH private keys between machines
- ❌ Run miners as root user

**Always:**
- ✅ Use SSH key-based authentication only
- ✅ Verify host keys on first connection
- ✅ Run miners as regular user (miika)
- ✅ Use tmux/screen for persistent sessions

#### Network Isolation

- Mining nodes should not host public-facing services
- Firewall rules: allow SSH (port 22) and stratum protocol only
- No port forwarding to mining nodes without explicit justification
- Monitor unusual network traffic patterns

---

### 3. Software Security

#### Binary Verification

**Before running any mining software:**

1. **Download from official source only:**
   - GitHub releases (verify repository ownership)
   - Official website (https:// only)
   - Never third-party download sites

2. **Verify checksums:**
   ```bash
   sha256sum miner-binary
   # Compare with official published hash
   ```

3. **Inspect configuration files:**
   - No unexpected network connections
   - No credential requests
   - No rootkit-like behavior

4. **Test in isolated environment first:**
   - Run with minimal permissions
   - Monitor system calls (strace if suspicious)
   - Check for unexpected file access

#### Known Safe Miners (as of 2026-02-16):

| Miner | Version | Source | Verified |
|-------|---------|--------|----------|
| lolMiner | 1.98a | GitHub: Lolliedieb/lolMiner-releases | ✅ |
| T-Rex | 0.26.8 | GitHub: trexminer/T-Rex | ✅ |

**Red Flags:**
- ❌ Miner requests sudo/root access
- ❌ Asks for wallet private key (only address needed)
- ❌ Makes network connections to non-pool addresses
- ❌ Modifies system files outside user directory
- ❌ Requests access to SSH keys or credentials

---

### 4. Data Security and Privacy

#### What Gets Committed to Git:

**Safe to commit:**
- ✅ Public wallet addresses (receiving addresses only)
- ✅ Pool URLs and ports
- ✅ Hashrate and performance data
- ✅ Configuration templates with placeholders
- ✅ Experiment results and analysis

**Never commit:**
- ❌ Private keys or seed phrases
- ❌ API keys with write permissions
- ❌ SSH private keys
- ❌ Passwords or credentials
- ❌ Personal identifying information
- ❌ Miner binaries (reference download links instead)

#### .gitignore Requirements

```gitignore
# Secrets (MANDATORY)
.env
.env.*
secrets*
wallet*
*.key
*.pem
private*

# Miner binaries
miners/
*.tar.gz
*.zip
*.bin

# Logs with sensitive data
*.log
logs/

# Local configuration
config.local.*
```

---

## Thermal Safety Protocols

### 1. Temperature Limits

#### Hard Limits (STOP IMMEDIATELY)

| Condition | Limit | Action |
|-----------|-------|--------|
| GPU Core Temp | >85°C | **STOP MINING IMMEDIATELY** |
| Sustained High Temp | >75°C for >10 min | Investigate, reduce power |
| Rapid Temp Rise | +20°C in <5 min | Stop and diagnose |
| Fan Failure | 0 RPM reported | Stop mining, investigate |

#### Soft Limits (Investigate)

| Condition | Limit | Action |
|-----------|-------|--------|
| GPU Temp Rising | >70°C | Check fan speed, reduce power limit |
| High Ambient Temp | >30°C room | Consider mining pause |
| Memory Temp | >95°C | Reduce memory overclock (if any) |

#### Monitoring Requirements

**Continuous monitoring during mining:**
```bash
# Run on each mining node (10s interval)
watch -n 10 nvidia-smi
```

**Automated logging:**
```bash
# Log temps every 60s to file
nvidia-smi --query-gpu=timestamp,temperature.gpu,power.draw,fan.speed \
  --format=csv -l 60 > ~/mining-test/thermal_log.csv
```

**Alert thresholds:**
- Set up manual checks every 6 hours minimum
- Daily review of max temperatures
- Weekly trend analysis

---

### 2. Thermal Emergency Procedures

#### If GPU temp >85°C:

1. **STOP MINING IMMEDIATELY:**
   ```bash
   pkill -SIGTERM lolMiner t-rex
   ```

2. **Verify GPU cooling down:**
   ```bash
   watch -n 5 nvidia-smi
   ```

3. **Do not restart until:**
   - [ ] Temp drops below 50°C
   - [ ] Root cause identified
   - [ ] Mitigation implemented (power limit reduction, fan speed, etc.)
   - [ ] 10-minute test run with monitoring

4. **Document incident:**
   - Log to EXPERIMENT_LOG.md
   - Record max temp reached
   - Note time to cool down
   - Identify cause (if known)
   - List corrective actions

---

## Power Safety Protocols

### 1. Power Consumption Limits

#### Hardware Limits (Enforced)

| GPU | Default TDP | Mining Limit | Reason |
|-----|-------------|--------------|--------|
| RTX 3060 | 170W | **120W** | Thermal headroom + efficiency |
| GTX 1660 SUPER | 125W | **80W** | Thermal headroom + efficiency |

**Enforcement:**
```bash
# Set on each boot / before mining
sudo nvidia-smi -pm 1
sudo nvidia-smi -pl 120  # ai-1
sudo nvidia-smi -pl 80   # ai-2
```

**Verification:**
```bash
nvidia-smi -q -d POWER | grep "Power Limit"
```

#### Total System Power Budget

- **ai-1 max:** 120W GPU + ~50W system = 170W total
- **ai-2 max:** 80W GPU + ~40W system = 120W total
- **Combined max:** ~290W

**Electrical safety:**
- Verify circuit breaker rating (should be ≥15A @ 120V or ≥10A @ 240V)
- Do not daisy-chain power strips
- Use surge protectors with adequate rating
- Monitor for overheating outlets or cables

---

### 2. Power Monitoring

**Real-time monitoring:**
```bash
# Check current power draw
nvidia-smi --query-gpu=power.draw --format=csv
```

**Logging:**
- Log power consumption every 60 seconds during mining
- Calculate average and peak power per 24h period
- Compare to electricity cost for ROI calculation

**Red flags:**
- Power draw exceeding enforced limit (indicates limit not applied)
- Sudden power drops (potential GPU issue)
- Erratic power consumption (unstable mining)

---

## Operational Safety Protocols

### 1. Mining Process Management

#### Startup Checklist

Before starting any mining operation:
- [ ] GPU temperatures <50°C (cool start)
- [ ] Power limits verified and applied
- [ ] Monitoring logging started
- [ ] Pool connection tested (ping pool URL)
- [ ] Wallet address verified correct
- [ ] tmux/screen session created for persistence
- [ ] Initial hashrate confirmed within expected range

#### Shutdown Checklist

When stopping mining:
- [ ] Send SIGTERM (graceful shutdown), not SIGKILL
- [ ] Wait 30s for miner to close cleanly
- [ ] Verify process terminated (`ps aux | grep miner`)
- [ ] Check final GPU temp
- [ ] Save logs to experiment log
- [ ] Document total runtime and any issues

---

### 2. Persistent Session Management

**Use tmux or screen to prevent SSH disconnect from killing miner:**

```bash
# Start new tmux session
tmux new -s mining

# Inside tmux, start miner
cd ~/crypto/miners/lolminer
./lolMiner --algo PYRIN --pool <pool> --user <address>

# Detach: Ctrl+b, then d
# Reattach later: tmux attach -t mining
```

**Never:**
- ❌ Run miner directly in SSH session (will die on disconnect)
- ❌ Use `nohup` without proper monitoring
- ❌ Background with `&` and forget

---

### 3. Update and Maintenance Windows

**Before updating mining software:**
1. Stop mining gracefully
2. Backup current configuration
3. Test new version in short (10 min) run first
4. Verify hashrate and stability
5. Monitor for 1 hour before leaving unattended

**During OS/driver updates:**
1. Stop all mining
2. Perform update
3. Reboot and verify GPU detection
4. Re-apply power limits
5. Test mining for 30 minutes before long-term restart

---

## Incident Response Protocols

### 1. Security Incident

**If you suspect compromise (unauthorized access, malware, etc.):**

1. **STOP ALL MINING IMMEDIATELY**
2. **Disconnect affected node from network** (if safe to do so)
3. **Do not delete anything** (preserve evidence)
4. **Document everything:**
   - What was observed?
   - When did it occur?
   - What systems are affected?
5. **Notify:**
   - Repository owner
   - Any relevant stakeholders
6. **Investigate:**
   - Check SSH logs: `/var/log/auth.log`
   - Review process list: `ps aux`
   - Check network connections: `netstat -tuln`
   - Inspect cron jobs: `crontab -l`
7. **Remediate:**
   - Change SSH keys if compromised
   - Re-image node if necessary
   - Review security protocols
8. **Post-mortem:**
   - Document incident in security log
   - Identify how compromise occurred
   - Implement preventive measures
   - Update SAFETY.md if needed

---

### 2. Thermal Incident

**If GPU overheats (>85°C):**

See [Thermal Emergency Procedures](#2-thermal-emergency-procedures) above.

**Additional steps:**
- Check for dust buildup (physical inspection if accessible)
- Verify fan is spinning (not failed)
- Ensure adequate case airflow
- Consider reducing power limit further (e.g., 100W instead of 120W)

---

### 3. Hardware Failure

**If GPU fails, crashes, or shows artifacts:**

1. **STOP MINING IMMEDIATELY**
2. **Do not force-restart** (may worsen damage)
3. **Power down gracefully:**
   ```bash
   sudo shutdown -h now
   ```
4. **Wait 10 minutes for cooling**
5. **Restart and check GPU detection:**
   ```bash
   nvidia-smi
   ```
6. **If GPU not detected or artifacts persist:**
   - Mining experiments paused indefinitely on that GPU
   - GPU removed from production use
   - Hardware diagnostics performed

---

## Audit and Compliance

### 1. Regular Safety Audits

**Daily:**
- [ ] Check max GPU temps from last 24h
- [ ] Verify mining processes running correctly
- [ ] Review any error messages in logs

**Weekly:**
- [ ] Review thermal log trends
- [ ] Check for any unusual power consumption
- [ ] Verify SSH access logs for unauthorized attempts
- [ ] Update experiment log

**Monthly:**
- [ ] Full safety protocol review
- [ ] Test emergency shutdown procedures
- [ ] Review and update this document if needed
- [ ] Verify wallet backups still accessible

---

### 2. Documentation Requirements

Every experiment must document:
- Start time and duration
- Algorithm and miner used
- Average and peak temperatures
- Average and peak power consumption
- Any incidents or anomalies
- Hashrate achieved
- Earnings (if applicable)

Store in `docs/EXPERIMENT_LOG.md`.

---

## Training and Awareness

### Before Starting Any Mining:

**Mandatory reading:**
- [ ] This SAFETY.md document (in full)
- [ ] GOVERNANCE.md (security section)
- [ ] DECISIONS.md (security-related decisions)

**Mandatory knowledge:**
- [ ] How to check GPU temperature
- [ ] How to stop mining immediately (command)
- [ ] Where thermal logs are stored
- [ ] What to do if GPU overheats

---

## Emergency Contacts

**In case of critical issue:**
- Repository Owner: [See main README.md]
- Datacenter/Physical Access: [If applicable]
- Hardware Vendor Support: [If under warranty]

**Non-emergency questions:**
- GitHub Issues on crypto-lab repository
- Review documentation first

---

## Safety Protocol Updates

This document must be reviewed and updated:
- After any security or thermal incident
- After major hardware or software changes
- Quarterly as part of project review
- When new risks are identified

**Update process:**
1. Propose changes via PR
2. Review by repository owner
3. Version number increment
4. All active miners notified of changes

---

## Acceptance

By proceeding with mining experiments, you acknowledge:
- ✅ I have read and understood all safety protocols
- ✅ I will follow thermal limits and monitoring requirements
- ✅ I will not store private keys on mining nodes
- ✅ I will stop mining immediately if safety limits exceeded
- ✅ I will document all incidents and experiments
- ✅ I understand this is experimental and carries risk

**Sign-off:**
- Name: [Repository Owner]
- Date: 2026-02-16
- Version: 1.0

---

**SAFETY FIRST. PROFIT SECOND. SECURITY ALWAYS.**

---

**Last Updated:** 2026-02-16
**Next Review:** 2026-03-16 (monthly)
**Version:** 1.0
