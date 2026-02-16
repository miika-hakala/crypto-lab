# Strategy — crypto-lab

**Version:** 1.0
**Last Updated:** 2026-02-16
**Status:** Active

---

## Vision

Determine the **profitability potential** of our GPU cluster through systematic experimentation, automation, and data-driven optimization — with a clear exit strategy if returns are negative.

---

## Non-Goals

This project explicitly **does not** aim to:
- ❌ Replace primary GPU cluster use (Ollama/AI workloads)
- ❌ Become a permanent mining operation
- ❌ Guarantee positive ROI
- ❌ Provide investment advice
- ❌ Compete with industrial mining operations

---

## Core Assumptions

1. **GPU availability is opportunistic** — mining only when GPUs are idle
2. **Electricity cost is fixed** — cluster runs regardless of mining
3. **Solar integration is future possibility** — optimize for excess capacity
4. **Time-to-market matters** — iterate quickly, validate assumptions
5. **Exit if negative** — no sunk cost fallacy, shut down if unprofitable

---

## Strategic Phases

### Phase 1: Discovery ✅ COMPLETE
**Duration:** 1-2 days
**Goal:** Understand baseline profitability and hardware capabilities

**Activities:**
- [x] Hardware inventory and specifications
- [x] Initial profitability analysis (paper ranking)
- [x] Multi-algorithm benchmarking
- [x] Power consumption measurement
- [x] Thermal characterization

**Deliverables:**
- [x] Benchmark report with top algorithms
- [x] Power/thermal profiles per GPU
- [x] Initial ROI estimates

**Key Findings:**
- RTX 3060: Best overall performance (4/5 algorithms)
- GTX 1660 SUPER: Limited by VRAM (6GB constraint)
- Pyrin algorithm: Highest efficiency (27.8 MH/W)
- All temperatures stable (<75°C)

**Exit Criteria Met:** ✅ Positive efficiency indicators justify Phase 2

---

### Phase 2: Automation 🔄 IN PROGRESS
**Duration:** 1-2 weeks
**Goal:** Build automated profitability monitoring and switching logic

**Objectives:**
1. **Profitability Runner:**
   - Automated API data fetching (WhatToMine, CoinWarz, etc.)
   - Real-time profitability calculation
   - Historical trend analysis
   - Daily/weekly reports

2. **Benchmark Engine:**
   - On-demand algorithm benchmarking
   - Hashrate verification vs pool stats
   - Power consumption tracking
   - Thermal monitoring

3. **Algorithm Switcher (MVP):**
   - Manual coin selection
   - Single-GPU deployment
   - Profit tracking vs baseline
   - 72h test runs

**Success Criteria:**
- [ ] Automated daily profitability reports
- [ ] Successful 72h test run on top algorithm
- [ ] Actual earnings data collected
- [ ] ROI calculation framework validated

**Exit Criteria:**
- If 72h test shows **negative ROI** after electricity → abort Phase 3
- If technical complexity exceeds value → simplify or exit

---

### Phase 3: Optimization 📋 PLANNED
**Duration:** 2-4 weeks
**Goal:** Maximize returns through intelligent automation

**Planned Features:**

1. **Dynamic Algorithm Switching:**
   - Auto-detect most profitable algorithm
   - Switch between coins/pools automatically
   - Minimize downtime during switches
   - Track switching overhead

2. **Solar-Aware Scheduling:**
   - Monitor solar production (if available)
   - Mine during excess solar capacity
   - Reduce mining during grid hours
   - Calculate carbon-neutral mining windows

3. **Multi-Pool Management:**
   - Failover to backup pools
   - Compare pool profitability
   - Optimize for payout frequency
   - Minimize pool fees

4. **Performance Dashboard:**
   - Real-time monitoring UI
   - Historical charts (hashrate, earnings, efficiency)
   - Alert system for anomalies
   - Mobile notifications

**Success Criteria:**
- [ ] Automatic switching reduces manual intervention to <1hr/week
- [ ] Solar integration improves net profitability by >20%
- [ ] Dashboard provides actionable insights
- [ ] System runs stable for 30+ days

**Exit Criteria:**
- If automation complexity costs more than gains → revert to manual
- If sustained negative ROI → project termination

---

### Phase 4: Scale (Conditional) ⏸️ ON HOLD
**Prerequisites:** Phase 3 success + sustained positive ROI

**Potential Expansions:**
- Additional GPU nodes
- Dedicated mining hardware evaluation
- Pool hosting exploration
- Community mining coordination

**Note:** Phase 4 only proceeds if:
1. Phases 1-3 demonstrate clear profitability
2. Infrastructure capacity allows expansion
3. Regulatory environment remains favorable
4. Human resources available for maintenance

---

## Strategic Priorities

### Priority 1: Data-Driven Decisions
- Collect objective metrics at every phase
- Compare estimates vs actuals rigorously
- Pivot based on evidence, not assumptions
- Document all findings for future reference

### Priority 2: Minimize Complexity
- Start simple, add features only when proven necessary
- Avoid over-engineering
- Prefer manual steps over buggy automation
- Technical debt is acceptable if project is exploratory

### Priority 3: Security First
- Never compromise cluster security for mining
- Wallet management stays off-cluster
- No root-level modifications
- All changes reversible

### Priority 4: Respect Primary Mission
- GPU cluster's primary purpose: AI/ML workloads (Ollama)
- Mining is opportunistic secondary use
- If mining interferes with primary use → mining stops
- Thermal/power budgets must not degrade primary performance

---

## Key Metrics (KPIs)

### Financial:
- **Daily Revenue (USD):** Actual earnings from mining
- **Electricity Cost (USD/day):** Power consumption cost
- **Net Profit (USD/day):** Revenue - Electricity
- **ROI Percentage:** (Net Profit / Initial Investment) × 100
- **Break-Even Timeline:** Days until cumulative profit > 0

### Technical:
- **Average Hashrate:** Per algorithm, per GPU
- **Uptime Percentage:** Mining time / available time
- **Efficiency (MH/W):** Hashrate per watt consumed
- **Temperature (°C):** Average and peak per GPU
- **Rejected Shares (%):** Network communication quality

### Operational:
- **Manual Intervention Hours:** Time spent managing mining
- **Incidents Count:** Crashes, thermal events, errors
- **Algorithm Switches:** Frequency and reasons
- **Experiment Velocity:** Tests completed per week

---

## Decision Framework

### Go/No-Go Criteria

**Continue if:**
- ✅ Net profit > $0/day (after electricity)
- ✅ System stability >95% uptime
- ✅ No security incidents
- ✅ Manual effort <2 hours/week
- ✅ Primary workloads unaffected

**Pause/Re-evaluate if:**
- ⚠️ Net profit marginal ($0-2/day)
- ⚠️ Frequent technical issues
- ⚠️ High manual intervention needed
- ⚠️ Uncertainty about regulatory changes

**Terminate if:**
- ❌ Sustained negative ROI (>7 days)
- ❌ Security breach or risk
- ❌ Primary GPU use compromised
- ❌ Regulatory prohibition
- ❌ Hardware damage risk

---

## Risk Management

### Technical Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| GPU overheating | Low | High | Power limits + monitoring |
| Software crashes | Medium | Low | Watchdogs + auto-restart |
| Network issues | Medium | Medium | Pool failover |
| Hardware failure | Low | High | Thermal monitoring + limits |

### Financial Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Crypto price crash | High | High | Exit strategy + diversification |
| Difficulty increase | High | Medium | Algorithm switching |
| Electricity cost rise | Low | Medium | Solar awareness |
| Negative ROI | Medium | High | Continuous monitoring + exit plan |

### Security Risks:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Wallet theft | Low | High | No private keys on cluster |
| Mining malware | Low | Medium | Binary verification |
| Pool compromise | Low | Low | Use established pools only |
| SSH breach | Very Low | High | Key-based auth only |

---

## Success Definition

**Phase 2 Success:**
- 72h test completes without incidents
- Actual earnings match estimates within ±20%
- ROI calculation framework validated
- Decision to proceed to Phase 3 is data-backed

**Project Success:**
- Net positive earnings sustained >30 days
- Automation reduces manual work to <1hr/week
- Primary GPU use unaffected
- Replicable methodology documented

**Exit with Success:**
- If negative ROI confirmed → document findings thoroughly
- If positive ROI but too marginal → shut down cleanly
- If regulatory issues → compliance documented
- All learnings captured for future reference

---

## Strategic Constraints

### Time Constraints:
- No more than 2 hours/week manual management (Phase 3 target)
- Major decisions reviewed within 48 hours
- Experiments run 72h minimum for statistical validity

### Budget Constraints:
- Zero additional hardware purchases (use existing cluster)
- Minimal software costs (prefer open source)
- Electricity cost already incurred (not incremental)

### Resource Constraints:
- Limited to 2 GPU nodes (ai-1, ai-2)
- SSH access required (no physical access)
- Development time is opportunity cost

---

## CPU Utilization Alternatives (Beyond Mining)

### Context: CPU Mining Baseline

**Current State:**
- CPU mining profitability: **Negligible to negative** on modern consumer CPUs
- Even efficient algorithms (RandomX/Monero): $0.10-0.50/day per CPU (12-16 cores)
- Electricity cost typically exceeds earnings
- GPU mining 50-100x more profitable per watt

**Baseline Comparison:**
CPU mining represents the **lowest ROI compute workload** in cryptocurrency. The following alternatives are evaluated against this baseline.

---

### Alternative 1: CPU-Bound AI Inference / Batch Scoring

**Description:**
Deploy CPU nodes for high-throughput AI inference tasks (sentiment analysis, classification, entity extraction) where latency tolerance is high but volume is massive. Complement existing GPU-based inference with CPU overflow capacity.

**Required Resources:**
- CPU: 8-16 cores minimum (existing ai-1, ai-2 CPUs)
- RAM: 16-32GB (already available)
- Storage: Minimal (model weights <5GB)
- Network: Standard bandwidth

**Technical Complexity:** Medium
- Requires: Model quantization (ONNX/INT8), job queue system, API integration
- Existing alignment: High (Ollama infrastructure already present)
- Development time: 1-2 weeks for MVP

**Risk Profile:** Low-Medium
- Technical risk: Low (proven inference stacks available)
- Market risk: Medium (requires customer/workload source)
- Operational risk: Low (CPU thermal limits safer than GPU)

**Potential ROI vs CPU Mining:**
- **10-50x higher** if monetized via API credits (e.g., $0.001-0.01 per inference)
- Break-even at ~1,000 inferences/day/CPU
- Synergy with existing AI workloads

**Strategic Fit:**
✅ **High alignment** — Leverages existing Ollama/AI infrastructure
✅ Idle CPU capacity utilization (when GPUs handle primary workload)
✅ Scales with existing cluster architecture

---

### Alternative 2: Data Extraction & Enrichment Pipeline

**Description:**
CPU-optimized pipeline for web scraping, data parsing, NLP enrichment, and structured data transformation. Complements existing crawler infrastructure with high-volume batch processing.

**Required Resources:**
- CPU: 4-8 cores per pipeline worker
- RAM: 8-16GB (parsing + caching)
- Storage: 100GB-1TB (crawled data cache)
- Network: High bandwidth (scraping workload)

**Technical Complexity:** Medium-High
- Requires: Distributed task queue, anti-ban infrastructure, data quality validation
- Existing alignment: **Very high** (crawler infrastructure already operational)
- Development time: 2-3 weeks for production pipeline

**Risk Profile:** Medium
- Technical risk: Medium (rate limiting, anti-scraping detection)
- Legal risk: Medium (must comply with ToS, robots.txt)
- Operational risk: Low (CPU-bound, predictable load)

**Potential ROI vs CPU Mining:**
- **20-100x higher** if sold as enriched datasets or API service
- Data enrichment: $0.01-0.10 per record (depending on complexity)
- Break-even at ~100-500 records/day/CPU

**Strategic Fit:**
✅ **Very high alignment** — Natural extension of existing crawler
✅ CPU-optimal workload (parsing, regex, NLP)
✅ Monetization-ready infrastructure (data assets)

---

### Alternative 3: Arbitrage / Trading Bot Engine

**Description:**
CPU-based algorithmic trading engine monitoring price spreads across exchanges, executing low-latency arbitrage trades. Requires real-time market data processing and order execution logic.

**Required Resources:**
- CPU: 4-8 cores (low latency critical)
- RAM: 16-32GB (market data streams)
- Network: **Low latency required** (<10ms to exchanges)
- Storage: Minimal (trade logs, state)

**Technical Complexity:** High
- Requires: Exchange API integration, risk management, backtesting framework
- Existing alignment: Low (no trading infrastructure)
- Development time: 4-6 weeks minimum + extensive testing

**Risk Profile:** High
- Technical risk: High (bugs = financial loss)
- Market risk: Very high (volatility, exchange failures)
- Regulatory risk: Medium (trading regulations, tax implications)
- Operational risk: High (24/7 monitoring required)

**Potential ROI vs CPU Mining:**
- **Highly variable** — Potential 100-1000x if successful, but also risk of loss
- Arbitrage margins: 0.1-2% per trade (narrowing over time)
- Requires significant capital exposure (>$10k minimum)

**Strategic Fit:**
⚠️ **Low alignment** — No existing trading infrastructure or expertise
❌ Highest risk profile of all alternatives
⚠️ Capital requirements beyond compute resources

---

### Alternative 4: AI Image Generation Orchestration (GPU+CPU Hybrid)

**Description:**
CPU handles prompt engineering, queue management, post-processing (upscaling, metadata), while GPU runs Stable Diffusion/FLUX inference. CPU maximizes GPU utilization through intelligent batching.

**Required Resources:**
- CPU: 8-16 cores (orchestration, post-processing)
- GPU: Required (primary inference workload)
- RAM: 32GB+ (image buffers)
- Storage: 500GB-2TB (generated images, model cache)

**Technical Complexity:** Medium
- Requires: Queue system, prompt optimization, image processing pipeline
- Existing alignment: High (GPU inference already operational)
- Development time: 2-3 weeks

**Risk Profile:** Low-Medium
- Technical risk: Low (stable tooling exists)
- Market risk: Medium (competitive image generation market)
- Content risk: Medium (requires content moderation for NSFW filtering)

**Potential ROI vs CPU Mining:**
- **30-80x higher** if monetized via API or marketplace sales
- Image generation pricing: $0.01-0.10 per image (depending on resolution)
- CPU contributes 20-30% of value chain (GPU does heavy lifting)

**Strategic Fit:**
✅ **High alignment** — Extends existing GPU AI capabilities
✅ CPU role is force multiplier for GPU utilization
✅ Synergy with image generation trends (2024-2026)

---

### Alternative 5: Transcription Farm (Whisper / Speech-to-Text)

**Description:**
CPU-optimized speech-to-text transcription using OpenAI Whisper models. Batch processing of audio files (podcasts, meetings, videos) with high accuracy and language support.

**Required Resources:**
- CPU: 8-16 cores (Whisper medium/large models)
- RAM: 16-32GB (audio buffers, model weights)
- Storage: 500GB-1TB (audio file queue)
- Network: Medium bandwidth (audio uploads/downloads)

**Technical Complexity:** Low-Medium
- Requires: Whisper deployment, job queue, audio preprocessing
- Existing alignment: Medium (AI inference expertise)
- Development time: 1-2 weeks for MVP

**Risk Profile:** Low
- Technical risk: Low (Whisper is production-ready)
- Market risk: Medium (competitive transcription market)
- Operational risk: Low (CPU-only workload, predictable)

**Potential ROI vs CPU Mining:**
- **40-120x higher** if sold as transcription service
- Transcription pricing: $0.10-0.50 per audio minute
- CPU can process 1-3x realtime (1 hour audio = 20-60 min processing)
- Break-even at ~10-20 hours audio/day

**Strategic Fit:**
✅ **Medium-high alignment** — Leverages AI inference experience
✅ Pure CPU workload (GPU optional for acceleration)
✅ Clear monetization path (API, marketplace)

---

### Alternative 6: CPU Render / Encoding Farm

**Description:**
CPU-based video encoding (H.264/H.265/AV1) and 3D rendering (Blender CPU rendering). High-volume batch processing for video platforms, content creators, or render marketplaces.

**Required Resources:**
- CPU: 16+ cores recommended (render/encode scales linearly)
- RAM: 32-64GB (4K/8K video buffers)
- Storage: 1-5TB (raw footage, render cache)
- Network: High bandwidth (video uploads/downloads)

**Technical Complexity:** Medium
- Requires: FFmpeg/HandBrake for encoding, Blender for rendering, job distribution
- Existing alignment: Low (no existing video infrastructure)
- Development time: 2-3 weeks

**Risk Profile:** Medium
- Technical risk: Low (mature encoding tools)
- Market risk: Medium (competitive render farm market)
- Operational risk: Medium (high storage and bandwidth demands)

**Potential ROI vs CPU Mining:**
- **25-60x higher** if sold on render marketplaces (SheepIt, Flamenco)
- Video encoding: $0.05-0.20 per minute (1080p/4K)
- 3D rendering: $0.01-0.10 per frame (depending on complexity)
- CPU render speed: Highly variable (2-10 min per frame for complex scenes)

**Strategic Fit:**
⚠️ **Low-medium alignment** — No existing video/rendering infrastructure
✅ Pure CPU workload (GPU rendering separate consideration)
⚠️ Storage and bandwidth intensive

---

## CPU Alternatives: Summary Ranking

### By Strategic Fit (Alignment with Existing Infrastructure):
1. **Data Extraction & Enrichment** — Very high (crawler synergy)
2. **AI Inference / Batch Scoring** — High (Ollama synergy)
3. **AI Image Orchestration** — High (GPU AI synergy)
4. **Transcription Farm** — Medium-high (AI expertise)
5. **CPU Render / Encoding** — Low-medium (new domain)
6. **Arbitrage / Trading Bots** — Low (new domain, high risk)

### By ROI Potential vs CPU Mining:
1. **Arbitrage Bots** — Highest potential (100-1000x), **highest risk**
2. **Transcription Farm** — 40-120x (clear pricing model)
3. **Data Enrichment** — 20-100x (existing demand)
4. **AI Image Orchestration** — 30-80x (GPU-dependent)
5. **AI Inference** — 10-50x (proven market)
6. **CPU Rendering** — 25-60x (competitive market)

### By Risk-Adjusted ROI:
1. **Transcription Farm** — High ROI, low risk, clear monetization
2. **Data Enrichment** — Very high synergy, proven demand
3. **AI Inference** — Safe bet, existing infrastructure
4. **AI Image Orchestration** — GPU synergy, growing market
5. **CPU Rendering** — Proven market, infrastructure gap
6. **Arbitrage Bots** — Highest risk, requires capital + expertise

---

## Recommendation

**Short-term exploration priority:**
1. **Data Enrichment Pipeline** (highest existing synergy)
2. **Transcription Farm** (lowest barrier to entry, clear ROI)
3. **AI Inference Overflow** (natural extension of current workloads)

**Not recommended (at this time):**
- Arbitrage/trading bots (risk profile too high, no existing expertise)
- CPU rendering (infrastructure gap, lower synergy)

**Next steps:**
- Formalize decision in DECISIONS.md (DEC-011)
- No immediate implementation (documentation-only for now)
- Further analysis required before resource commitment

---

## Communication Plan

### Internal Documentation:
- Update STATUS.md after each phase completion
- Log all experiments in EXPERIMENT_LOG.md
- Record decisions in DECISIONS.md (ADR format)
- Maintain this STRATEGY.md as living document

### Stakeholder Updates:
- Weekly summary (if project active)
- Immediate alert on critical issues
- Phase completion reports
- Exit decision documentation

---

## Roadmap Timeline

```
Week 1: ✅ Phase 1 Complete (Discovery)
Week 2: 🔄 Phase 2 Start (Automation)
Week 3-4: Phase 2 Continued (72h tests)
Week 5: Phase 2 Decision (Go/No-Go)
Week 6-9: Phase 3 (if approved)
Week 10+: Phase 4 (conditional)
```

---

## Open Questions

1. **Solar Integration:**
   - How to detect excess solar capacity programmatically?
   - What's the carbon footprint comparison?

2. **Regulatory:**
   - What are tax implications of mining income?
   - Any local regulations on residential mining?

3. **Optimization:**
   - Is dual-mining (ETH+ALEPH) more profitable than single?
   - What's the optimal algorithm switch frequency?

4. **Long-Term:**
   - Will GPU cluster scale beyond current 2 nodes?
   - Should we consider ASIC evaluation?

---

## Strategy Review Schedule

- **Weekly:** Review KPIs and immediate decisions
- **End of Phase:** Comprehensive phase retrospective
- **Monthly:** Strategic direction reassessment
- **Quarterly:** Long-term viability evaluation

---

**Next Review:** End of Phase 2 (estimated Week 4-5)
**Owner:** Repository Maintainer
**Last Updated:** 2026-02-16
