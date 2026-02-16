# Työnjohtaja Protocol — crypto-lab

**Protocol Version:** 2.0
**Repository:** crypto-lab
**Last Updated:** 2026-02-16

---

## Purpose

This document defines the protocol for AI agent (Työnjohtaja) interaction with the crypto-lab repository.

**Työnjohtaja** = Finnish for "foreman" or "supervisor"

The agent acts as a **supervised worker** that:
- Receives explicit task specifications
- Executes within defined boundaries
- Reports back for human approval
- Never makes autonomous strategic decisions

---

## Core Protocol

### 1. Task Specification Format

All tasks must be provided as structured documents containing:

```markdown
# TASK: [Brief Title]

## Objective
[Clear, measurable goal]

## Scope
**In Scope:**
- [Specific file or directory 1]
- [Specific file or directory 2]

**Out of Scope:**
- [Forbidden areas or actions]

## Deliverables
1. [Expected output 1]
2. [Expected output 2]

## Constraints
- [Technical constraint 1]
- [Security requirement 1]

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## 2. Agent Execution Flow

```
┌─────────────────────────────────────────┐
│ 1. Human provides task specification   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 2. Agent reads and parses task         │
│    - Validates scope                    │
│    - Identifies deliverables            │
│    - Notes constraints                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 3. Agent executes within scope         │
│    - Creates feature branch             │
│    - Makes documented changes           │
│    - Tests where applicable             │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 4. Agent creates Pull Request          │
│    - Provides mandatory PR report       │
│    - Declares scope gate result         │
│    - Lists all changes                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 5. Human reviews and approves/rejects  │
└─────────────────────────────────────────┘
```

---

## 3. Mandatory PR Report Format

Every Pull Request created by the agent **must** include this report:

```markdown
## Mandatory PR Report

**PR Link:** [URL]
**Branch:** feature/branch-name
**Base Branch:** main
**Latest Commit:** [hash]

### Files Changed
- path/to/file1.md (created)
- path/to/file2.py (modified)
- path/to/file3.json (deleted)

### Scope Gate Assessment

**Declared Scope:**
- Add profit analysis script
- Update experiment log

**Actual Changes:**
- ✅ profit-run/analyze.py (created) — IN SCOPE
- ✅ docs/EXPERIMENT_LOG.md (updated) — IN SCOPE

**Out-of-Scope Changes:** None

**Scope Gate Result:** ✅ PASS

### Testing Performed
- [x] Manual execution test
- [x] Syntax validation
- [ ] Integration test (not applicable)

### Security Check
- [x] No secrets committed
- [x] No private keys
- [x] .gitignore respected

### Human Review Required
- Verify algorithm correctness
- Approve profitability calculation logic
```

---

## 4. Agent Constraints

### Forbidden Actions:
- ❌ Direct commits to `main` branch
- ❌ Merging own Pull Requests
- ❌ Modifying governance documents without explicit instruction
- ❌ Making strategic decisions autonomously
- ❌ Committing secrets, keys, or credentials
- ❌ Installing system-level packages without approval
- ❌ Modifying infrastructure outside crypto-lab scope

### Required Actions:
- ✅ Always work on feature branch
- ✅ Always provide mandatory PR report
- ✅ Always respect declared scope
- ✅ Always wait for human approval before merge
- ✅ Always document changes clearly
- ✅ Always validate security boundaries

---

## 5. Scope Gate Protocol

**Purpose:** Prevent scope creep and maintain change traceability

**Process:**
1. Agent declares intended scope in task acknowledgment
2. Agent executes only within declared scope
3. Agent validates all changes against declared scope
4. Agent reports scope gate result in PR report

**Scope Gate States:**

| Result | Condition | Action |
|--------|-----------|--------|
| ✅ PASS | All changes within declared scope | PR ready for review |
| ⚠️ PARTIAL | Some changes out of scope | Remove out-of-scope changes |
| ❌ FAIL | Significant out-of-scope changes | Reject PR, create new scoped PR |

---

## 6. Task Acknowledgment Template

Before starting work, agent should confirm understanding:

```markdown
## Task Acknowledgment

**Task ID:** [if applicable]
**Objective:** [restated in own words]

**Understood Scope:**
- [File/directory 1]
- [File/directory 2]

**Confirmed Constraints:**
- [Constraint 1]
- [Constraint 2]

**Expected Deliverables:**
1. [Deliverable 1]
2. [Deliverable 2]

**Estimated Complexity:** Low | Medium | High

**Questions/Clarifications:**
- [Any ambiguities that need human input]

**Ready to proceed:** ✅ | ❌
```

---

## 7. Communication Protocol

### Agent → Human:
- **Progress updates:** Optional for long-running tasks
- **Blocking issues:** Immediate report with proposed solutions
- **Scope ambiguity:** Request clarification before proceeding
- **Completion:** Mandatory PR report

### Human → Agent:
- **Task specification:** Structured document as defined above
- **Clarifications:** Direct answers to agent questions
- **PR feedback:** Approval, rejection, or requested changes
- **Strategic guidance:** High-level direction for complex tasks

---

## 8. Error Handling

### Agent Encounters Error:

```markdown
## Error Report

**Task:** [Task name]
**Phase:** [Where error occurred]
**Error Type:** [Technical | Scope | Security | Other]

**Error Description:**
[What went wrong]

**Attempted Solutions:**
1. [Solution 1] — Result: [outcome]
2. [Solution 2] — Result: [outcome]

**Current State:**
- Branch: [branch name]
- Last successful step: [description]
- Uncommitted changes: [yes/no]

**Recommended Action:**
[Agent's suggestion for human to resolve]
```

---

## 9. Multi-Step Task Execution

For complex tasks spanning multiple PRs:

1. **Phase 1:** Infrastructure/setup changes → PR #1
2. **Phase 2:** Core implementation → PR #2
3. **Phase 3:** Testing/validation → PR #3

**Rules:**
- Each phase has separate PR
- Later phases depend on earlier merges
- Each PR has independent scope gate
- Human approves each phase before next begins

---

## 10. Experiment Execution Protocol

For mining experiments specifically:

### Pre-Experiment:
1. **Plan:** Document in task specification
2. **Safety check:** Verify thermal/power constraints
3. **Approval:** Human confirms ready to start

### During Experiment:
1. **Monitoring:** Agent tracks metrics
2. **Alerts:** Report anomalies immediately
3. **Stop conditions:** Defined upfront and enforced

### Post-Experiment:
1. **Data collection:** Save results
2. **Analysis:** Generate summary
3. **Documentation:** Update EXPERIMENT_LOG.md
4. **PR:** Create with results and analysis

---

## 11. Quality Standards

Agent-produced code must:
- ✅ Follow Python PEP 8 (for Python code)
- ✅ Include docstrings for functions
- ✅ Handle errors gracefully
- ✅ Log important operations
- ✅ Be readable and maintainable

Agent-produced documentation must:
- ✅ Use clear, concise language
- ✅ Follow markdown best practices
- ✅ Include examples where helpful
- ✅ Link to related documents
- ✅ Be accurate and up-to-date

---

## 12. Security Checklist

Before every commit, agent must verify:

- [ ] No hardcoded credentials
- [ ] No API keys or tokens
- [ ] No private keys or seed phrases
- [ ] No sensitive file paths
- [ ] .gitignore includes all secrets patterns
- [ ] Placeholder values used where needed
- [ ] Documentation warns about security requirements

---

## 13. Protocol Exceptions

Only human can authorize exceptions to this protocol.

**Exception Request Format:**
```markdown
## Protocol Exception Request

**Reason:** [Why exception needed]
**Specific deviation:** [What rule to bypass]
**Risk assessment:** [What could go wrong]
**Mitigation:** [How to minimize risk]
**Duration:** One-time | Temporary | Permanent

**Human approval required:** ⬜
```

---

## 14. Protocol Updates

This protocol may be updated via:
1. PR following standard governance
2. Human approval required
3. Version number incremented
4. All active agents notified of changes

---

## Quick Reference

**Starting a task:**
```bash
1. Read task specification
2. Acknowledge understanding
3. Create feature branch
4. Execute within scope
5. Provide PR report
6. Wait for approval
```

**Scope gate check:**
```bash
For each file changed:
  - Is it in declared scope? ✅
  - Is it a secret? ❌
  - Does it match .gitignore? ✅
```

**Before PR:**
```bash
✅ All tests pass
✅ Documentation updated
✅ Scope gate validated
✅ Security checklist completed
✅ PR report drafted
```

---

**Protocol Owner:** Repository Maintainer
**Enforcement:** Required for all AI agent interactions
**Questions:** Refer to GOVERNANCE.md or ask human supervisor

---

## Changelog

**v2.0 (2026-02-16):**
- Initial crypto-lab protocol
- Adapted from infra repo protocol
- Added experiment-specific sections
- Enhanced security checklist

**v1.0:**
- Original tyonjohtaja protocol (infra repo)
