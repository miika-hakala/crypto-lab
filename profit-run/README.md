# profit-run — Profitability Analysis Scripts

**Purpose:** Automated cryptocurrency mining profitability analysis tools.

---

## Overview

This directory contains scripts for:
- Fetching real-time profitability data from APIs (WhatToMine, CoinWarz, etc.)
- Paper ranking of algorithms based on market conditions
- Real benchmark data analysis (combining API data + actual GPU performance)
- Historical trend analysis
- ROI calculation

---

## Current Status

**Phase:** Migration from `~/crypto/profit-run/` to crypto-lab repository

### Completed:
- ✅ Initial profitability analysis (manual)
- ✅ Benchmark data collection
- ✅ Algorithm ranking scripts

### Pending:
- [ ] Move scripts to this directory
- [ ] Automate data fetching (daily cron)
- [ ] Real-time monitoring dashboard
- [ ] Integration with mining operations

---

## Scripts (To Be Added)

### Core Scripts:
- `rank_paper.py` — Paper ranking from API data
- `rank_real.py` — Real ranking combining benchmarks + API
- `fetch_data.py` — Automated API data fetching
- `analyze_profit.py` — ROI and profitability calculation
- `monitor.py` — Real-time monitoring during mining

### Data Files:
- `coins_top.json` — Latest coin data (gitignored, regenerated)
- `whattomine_coins.json` — WhatToMine API cache
- `benchmarks.json` — Hardware benchmark results

---

## Usage (Future)

```bash
# Fetch latest profitability data
python3 fetch_data.py

# Generate paper ranking
python3 rank_paper.py

# Analyze real profitability (requires benchmark data)
python3 rank_real.py

# Calculate ROI for specific algorithm
python3 analyze_profit.py --algo pyrin --duration 30d
```

---

## Dependencies

```bash
# Python 3.8+
pip install requests beautifulsoup4 pandas

# Optional for visualization
pip install matplotlib seaborn
```

---

## Configuration

Configuration will use environment variables or config file (not committed):
```bash
# .env (gitignored)
WHATTOMINE_API_KEY=optional
COINWARZ_API_KEY=optional
UPDATE_INTERVAL=3600  # seconds
```

---

## Data Sources

### Primary:
- **WhatToMine API:** `https://whattomine.com/coins.json`
- **CoinWarz API:** (if available)

### Backup:
- **Manual pool stats** if APIs unavailable
- **Historical data** from experiment log

---

## Output Formats

### Paper Ranking:
- Markdown table (for docs)
- JSON (for automation)
- CSV (for spreadsheet analysis)

### Real Ranking:
- Markdown report
- JSON with full metrics
- Charts (PNG) if visualization enabled

---

## Integration Points

- **Experiment Log:** Reads from `docs/EXPERIMENT_LOG.md`
- **Status:** Updates `docs/STATUS.md`
- **Decisions:** May update `docs/DECISIONS.md` with recommendations

---

## Automation (Planned)

```bash
# Cron job example (daily profitability check)
0 6 * * * cd ~/crypto/crypto-lab/profit-run && python3 fetch_data.py && python3 rank_paper.py
```

---

## Notes

- All API data is cached and refreshed periodically
- No secrets stored in this directory (API keys in .env, gitignored)
- Profitability estimates are just that — estimates
- Real earnings tracked in EXPERIMENT_LOG.md

---

**Status:** 🚧 Under Construction
**Last Updated:** 2026-02-16
