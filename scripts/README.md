# scripts — Operational and Utility Scripts

**Purpose:** Collection of utility scripts for mining operations, monitoring, and maintenance.

---

## Overview

This directory contains operational scripts for:
- Mining process management (start, stop, restart)
- Monitoring and alerting
- Log collection and analysis
- Safety checks (thermal, power)
- Backup and maintenance utilities

---

## Current Status

**Phase:** Bootstrap — Empty, will be populated during Phase 2 (Automation)

### Planned Scripts:

#### Mining Control:
- `start_mining.sh` — Launch miner with proper configuration
- `stop_mining.sh` — Graceful shutdown of mining process
- `switch_algo.sh` — Switch to different algorithm
- `restart_mining.sh` — Restart with health checks

#### Monitoring:
- `monitor_gpu.sh` — Real-time GPU monitoring dashboard
- `check_health.sh` — System health checks
- `alert_thermal.sh` — Temperature alert system
- `log_metrics.sh` — Collect and save metrics

#### Safety:
- `thermal_check.sh` — Verify temperatures safe
- `power_check.sh` — Verify power limits applied
- `emergency_stop.sh` — Immediate shutdown if unsafe

#### Maintenance:
- `backup_logs.sh` — Archive mining logs
- `cleanup_old_data.sh` — Remove old temporary files
- `update_miners.sh` — Update mining software
- `verify_config.sh` — Validate configuration files

---

## Script Standards

All scripts must follow:
- ✅ Shebang line (`#!/bin/bash`)
- ✅ Clear description at top
- ✅ Exit on error (`set -e`)
- ✅ Parameter validation
- ✅ Logging to file and stdout
- ✅ Proper error handling
- ✅ Security checks (no hardcoded secrets)

### Template:
```bash
#!/bin/bash
# Script Name: example.sh
# Purpose: Brief description
# Usage: ./example.sh [args]
# Author: crypto-lab
# Date: YYYY-MM-DD

set -e  # Exit on error
set -u  # Error on undefined variable

# Configuration
LOG_FILE="$HOME/crypto-lab/logs/example.log"

# Functions
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Main logic
log "Starting example script"
# ... script content ...
log "Example script completed successfully"
```

---

## Directory Structure (Future)

```
scripts/
├── README.md              (this file)
├── mining/
│   ├── start_mining.sh
│   ├── stop_mining.sh
│   └── switch_algo.sh
├── monitoring/
│   ├── monitor_gpu.sh
│   ├── check_health.sh
│   └── log_metrics.sh
├── safety/
│   ├── thermal_check.sh
│   ├── power_check.sh
│   └── emergency_stop.sh
└── maintenance/
    ├── backup_logs.sh
    ├── cleanup_old_data.sh
    └── update_miners.sh
```

---

## Usage Examples (Planned)

```bash
# Start mining Pyrin on ai-1
./scripts/mining/start_mining.sh --gpu ai-1 --algo pyrin

# Monitor GPU temperatures in real-time
./scripts/monitoring/monitor_gpu.sh --node ai-1 --refresh 10

# Run safety checks
./scripts/safety/thermal_check.sh --threshold 75

# Emergency stop all mining
./scripts/safety/emergency_stop.sh --all

# Backup all logs
./scripts/maintenance/backup_logs.sh --days 7
```

---

## Configuration

Scripts will read configuration from:
1. **Environment variables** (highest priority)
2. **Config file:** `~/.crypto-lab/config` (if exists)
3. **Defaults** (hardcoded fallback)

Example config file:
```bash
# ~/.crypto-lab/config
GPU_AI1="ai-1"
GPU_AI2="ai-2"
THERMAL_LIMIT=75
POWER_LIMIT_AI1=120
POWER_LIMIT_AI2=80
LOG_DIR="$HOME/crypto-lab/logs"
```

---

## Safety Features

All mining control scripts must:
- ✅ Check GPU temperature before starting
- ✅ Verify power limits applied
- ✅ Validate pool connectivity
- ✅ Use tmux/screen for persistence
- ✅ Log all actions

---

## Integration

Scripts integrate with:
- **profit-run/**: Use profitability data for algorithm selection
- **docs/EXPERIMENT_LOG.md**: Append experiment data
- **docs/STATUS.md**: Update mining status
- **Monitoring**: Send metrics to central location

---

## Testing

Before committing new scripts:
- [ ] Dry-run mode works (`--dry-run` flag)
- [ ] Error handling tested
- [ ] Logging verified
- [ ] No hardcoded secrets
- [ ] Safety checks pass
- [ ] Documentation updated

---

## Automation (Future)

```bash
# Crontab examples

# Hourly health check
0 * * * * ~/crypto-lab/scripts/monitoring/check_health.sh

# Daily log backup
0 2 * * * ~/crypto-lab/scripts/maintenance/backup_logs.sh

# Thermal monitoring (every 10 min while mining)
*/10 * * * * ~/crypto-lab/scripts/safety/thermal_check.sh
```

---

## Notes

- All scripts are user-space (no sudo required except nvidia-smi power limits)
- Scripts should be idempotent (safe to run multiple times)
- Always test in dry-run mode first
- Keep scripts simple and focused (single responsibility)

---

**Status:** 📋 Planned — Will be populated during Phase 2
**Last Updated:** 2026-02-16
