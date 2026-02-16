# crypto-lab

**GPU Cluster Experimentation Laboratory**

[![Status](https://img.shields.io/badge/status-bootstrap-yellow)](docs/STATUS.md)
[![Phase](https://img.shields.io/badge/phase-research-blue)](docs/STRATEGY.md)

---

## Purpose

This repository is a **research and experimentation lab** for analyzing GPU cluster profitability through cryptocurrency mining benchmarks and automated optimization logic.

**What this is:**
- ✅ Profitability analysis framework
- ✅ GPU benchmark automation
- ✅ Algorithm switching research
- ✅ Performance data collection

**What this is NOT:**
- ❌ Not a production mining operation
- ❌ Not investment advice
- ❌ Not a key/wallet management system
- ❌ Not integrated with infra repository

---

## Architecture

### Hardware
- **ai-1:** NVIDIA RTX 3060 (12GB VRAM)
- **ai-2:** NVIDIA GTX 1660 SUPER (6GB VRAM)
- **dev-main:** Control node

### Scope
- Isolated from production infrastructure
- User-space installations only
- No system daemon modifications
- Strict security boundaries

---

## Documentation

📚 **Strategy & Planning:**
- [STRATEGY.md](docs/STRATEGY.md) — Project goals and phases
- [DECISIONS.md](docs/DECISIONS.md) — Architecture decision records (ADRs)

🔒 **Security & Safety:**
- [SAFETY.md](docs/SAFETY.md) — Security protocols and constraints

📊 **Operations:**
- [STATUS.md](docs/STATUS.md) — Current project status
- [EXPERIMENT_LOG.md](docs/EXPERIMENT_LOG.md) — Benchmark results log

🏛️ **Governance:**
- [GOVERNANCE.md](GOVERNANCE.md) — Repository management rules
- [tyonjohtaja.md](tyonjohtaja.md) — AI agent task protocol

---

## Quick Start

**Prerequisites:**
- SSH access to ai-1 and ai-2 nodes
- Python 3.8+
- Git configured with SSH keys

**Current Status:**
```bash
# Check project status
cat docs/STATUS.md

# View latest experiments
cat docs/EXPERIMENT_LOG.md
```

---

## Project Phases

### Phase 1: Discovery ✅
- [x] Hardware inventory
- [x] Initial profitability analysis
- [x] Algorithm benchmarks

### Phase 2: Automation (In Progress)
- [ ] Automated profitability runner
- [ ] Dynamic algorithm switching
- [ ] Real-time monitoring

### Phase 3: Optimization (Planned)
- [ ] Solar-aware scheduling
- [ ] Multi-pool management
- [ ] ROI analysis dashboard

---

## Important Disclaimers

⚠️ **Security Notice:**
- No private keys or seed phrases are stored in this repository
- Wallet addresses are public receiving addresses only
- All secrets must be managed outside version control

⚠️ **Financial Disclaimer:**
- This is research code for educational purposes
- Cryptocurrency mining involves financial risk
- No guarantees of profitability are made
- Not financial or investment advice

⚠️ **Experimental Status:**
- Active development and research
- Breaking changes may occur
- Exit criteria: negative ROI → project termination

---

## Contributing

This repository follows strict governance protocols:

1. **All changes via Pull Request** (no direct commits to main)
2. **Scope gate required** for every PR
3. **SSOT principle:** main branch is the single source of truth
4. See [GOVERNANCE.md](GOVERNANCE.md) for full rules

---

## License

MIT License - See LICENSE file for details

---

## Contact

For questions about this project, refer to the documentation in `docs/` directory.

**Repository Owner:** Miika Hakala
**Created:** 2026-02-16
