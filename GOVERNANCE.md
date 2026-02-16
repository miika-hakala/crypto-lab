# Governance Model — crypto-lab

**Version:** 1.0
**Last Updated:** 2026-02-16
**Status:** Active

---

## Core Principles

### 1. Single Source of Truth (SSOT)

The `main` branch is the **only** authoritative source for:
- All documentation
- All scripts and code
- All configuration templates
- All experiment data

**Rules:**
- ✅ `main` branch is protected
- ✅ All changes require Pull Request
- ✅ No direct commits to `main`
- ✅ PR must pass scope gate before merge

---

## 2. Pull Request Protocol

### Every Change Must:
1. **Branch from main:**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/descriptive-name
   ```

2. **Commit with clear messages:**
   ```bash
   git commit -m "category: brief description"
   ```

3. **Create PR with scope gate:**
   - List all files changed
   - Declare scope boundaries
   - Confirm no out-of-scope modifications

4. **Mandatory PR Report:**
   - PR link
   - Branch name
   - Latest commit hash
   - Files changed
   - Scope gate result: PASS/FAIL

---

## 3. Scope Gate

**Purpose:** Prevent scope creep and maintain audit trail

**Requirements:**
- Every PR must declare intended scope
- All file changes must be within declared scope
- Out-of-scope changes → PR fails → must be removed or re-scoped

**Example Scope Declaration:**
```markdown
## Scope

**Intended Changes:**
- Add profit-run/analyze.py
- Update docs/EXPERIMENT_LOG.md

**Out of Scope:**
- Any infra/ changes
- Any modifications to mining binaries
- Any secrets or credentials
```

---

## 4. Security Boundaries

### Forbidden in Version Control:
- ❌ Private keys
- ❌ Seed phrases
- ❌ Wallet private keys
- ❌ API keys with write permissions
- ❌ SSH private keys
- ❌ Passwords

### Allowed (with caution):
- ✅ Public wallet receiving addresses
- ✅ Public pool URLs
- ✅ API read-only keys (if necessary)
- ✅ Configuration templates with placeholders

### Mandatory .gitignore:
```gitignore
# Secrets
.env
secrets*
wallet*
*.key
*.pem

# Miner binaries
miners/
*.tar.gz
*.zip

# Logs and data
*.log
*.csv
output/
cache/

# JSON except documentation
*.json
!docs/**/*.json
```

---

## 5. AI Agent Protocol (Työnjohtaja)

This repository uses the **Työnjohtaja protocol** for AI-assisted development:

### Agent Responsibilities:
1. **Read task specification** from provided file
2. **Execute within declared scope**
3. **Create PR with mandatory report**
4. **Wait for human approval** before merge

### Agent Constraints:
- ❌ No direct main branch commits
- ❌ No out-of-scope changes
- ❌ No secrets in commits
- ❌ No infrastructure modifications
- ✅ Always use PR workflow
- ✅ Always provide scope gate report

See [tyonjohtaja.md](tyonjohtaja.md) for full protocol.

---

## 6. Repository Boundaries

### In Scope:
- GPU mining experiments
- Profitability analysis
- Benchmark automation
- Algorithm research

### Out of Scope:
- Infrastructure changes (use infra repo)
- Production deployments
- System daemon modifications
- Root-level installations

---

## 7. Experiment Data Management

### Experiment Logs:
- Store results in `docs/EXPERIMENT_LOG.md`
- Include: date, algorithm, hashrate, power, temperature, earnings
- Update after each significant test run

### Benchmark Data:
- Raw CSV/JSON data → local storage only (gitignored)
- Summary statistics → committed to `docs/`
- Large datasets → not in version control

---

## 8. Decision Records

All architectural and strategic decisions are logged in `docs/DECISIONS.md` following ADR format:

```markdown
## DEC-XXX: Decision Title

**Date:** YYYY-MM-DD
**Status:** Accepted | Superseded | Deprecated

**Context:**
[Why this decision was needed]

**Decision:**
[What was decided]

**Consequences:**
[Positive and negative outcomes]
```

---

## 9. Branch Naming Convention

Use clear, descriptive branch names:

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/short-name` | `feature/auto-switcher` |
| Bugfix | `bugfix/issue-description` | `bugfix/temp-monitoring` |
| Docs | `docs/topic` | `docs/add-safety-guide` |
| Experiment | `experiment/test-name` | `experiment/kawpow-72h` |
| Refactor | `refactor/component` | `refactor/profitability-calc` |

---

## 10. Merge Policy

### Requirements Before Merge:
1. ✅ Scope gate passed
2. ✅ No merge conflicts
3. ✅ All files within declared scope
4. ✅ Mandatory PR report provided
5. ✅ Human review and approval

### After Merge:
1. Delete feature branch (keep git history clean)
2. Update `docs/STATUS.md` if project phase changed
3. Tag releases when reaching milestones

---

## 11. Exit Criteria

This project will be **terminated** if:
- ROI analysis shows sustained negative returns
- Security breach occurs
- Hardware failures make mining unviable
- Regulatory changes prohibit operation

Exit process:
1. Document findings in `docs/FINAL_REPORT.md`
2. Archive repository (read-only)
3. Clean up all GPU nodes
4. Remove all mining software

---

## 12. Enforcement

**Human Oversight:**
- All PR merges require human approval
- Strategic decisions require human validation
- Security violations → immediate PR rejection

**Automated Checks (Future):**
- Pre-commit hooks for secrets detection
- Scope gate validation scripts
- Automated PR report formatting

---

## Governance Updates

This governance model may be updated via PR with:
- Clear rationale for changes
- Version bump in header
- Update date recorded
- Previous version archived in git history

---

**Maintained by:** Repository Owner
**Contact:** See main README.md
**Last Review:** 2026-02-16
