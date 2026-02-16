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

**Phase:** Phase 2 (Automation) — Scripts imported

### Completed:
- ✅ Scripts imported to crypto-lab repository
- ✅ Initial profitability analysis (manual)
- ✅ Benchmark data collection
- ✅ Algorithm ranking scripts

### Pending:
- [ ] Automate data fetching (daily cron)
- [ ] Real-time monitoring dashboard
- [ ] Integration with mining operations

---

## Available Scripts

### Core Scripts:
- ✅ `rank_paper.py` — Paper ranking from API data
- ✅ `rank_real.py` — Real ranking combining benchmarks + API
- ✅ `INSTALL_NOTES.md` — Mining software installation guide
- 📋 `fetch_data.py` — Automated API data fetching (planned)
- 📋 `analyze_profit.py` — ROI and profitability calculation (planned)
- 📋 `monitor.py` — Real-time monitoring during mining (planned)

### Data Files:
- `coins_top.json` — Latest coin data (gitignored, regenerated)
- `whattomine_coins.json` — WhatToMine API cache
- `benchmarks.json` — Hardware benchmark results

---

## Usage

### Fetch Profitability Data

```bash
cd profit-run

# Fetch WhatToMine data
curl -fsSL 'https://whattomine.com/coins.json' -o whattomine_coins.json
```

### Generate Paper Ranking

Analyzes API data to rank algorithms by profitability:

```bash
python3 rank_paper.py
# Outputs markdown table to stdout
# Redirect to save: python3 rank_paper.py > paper_ranking.md
```

**Input:** `whattomine_coins.json` (must exist in same directory)
**Output:** Markdown table with top 10 coin/algorithm combinations

### Generate Real Ranking

Combines API data with actual GPU benchmark results:

```bash
python3 rank_real.py
# Outputs markdown table to stdout
# Redirect to save: python3 rank_real.py > real_ranking.md
```

**Input:**
- `whattomine_coins.json` (API data)
- Hardcoded benchmark results from testing

**Output:** Three rankings:
1. Top by estimated profit
2. Top by profit per watt
3. Most stable (low temp)

### Example Workflow

```bash
# 1. Fetch latest data
curl -fsSL 'https://whattomine.com/coins.json' -o whattomine_coins.json

# 2. Generate paper ranking
python3 rank_paper.py | tee paper_ranking.md

# 3. After benchmarks, generate real ranking
python3 rank_real.py | tee real_ranking.md

# 4. Review examples
ls examples/*.example.md
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

## Example Reports

See `examples/` directory for sample outputs:
- `paper_ranking.example.md` — Paper ranking output
- `real_ranking.example.md` — Real ranking with benchmarks
- `FINAL_REPORT.example.md` — Complete profitability analysis report

**Note:** Examples have been sanitized (node names, addresses replaced with placeholders)

---

## Data Management

### What Gets Committed:
- ✅ Python scripts
- ✅ Documentation
- ✅ Example reports (sanitized)

### What Gets Ignored:
- ❌ API cache files (`*.json` except examples)
- ❌ Benchmark raw data (`bench_results/`, `*.csv`)
- ❌ Miner binaries (`miners/`, `*.tar.gz`)
- ❌ Output files (`output/`, `cache/`)
- ❌ Secrets (`.env`, `wallet*`)

See `.gitignore` for complete list.

---

## Notes

- All API data is cached and refreshed periodically
- No secrets stored in this directory (API keys in .env, gitignored)
- Profitability estimates are just that — estimates
- Real earnings tracked in `../docs/EXPERIMENT_LOG.md`
- Node names sanitized: gpu-node-1, gpu-node-2 (not actual hostnames)

---

**Status:** ✅ Imported (PR #2)
**Last Updated:** 2026-02-16
