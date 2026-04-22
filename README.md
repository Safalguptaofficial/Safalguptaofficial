<!--
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║   SAFAL_OS v5.0.0                                                                 ║
║   Kernel: safal-engineered × self-evolving × auto-updating                        ║
║   Build:  2026.03.24-194216+0530                                                  ║
║                                                                                   ║
║   This is not a README. This is a running system.                                 ║
║   Some sections auto-update via GitHub Actions cron.                              ║
║   Some sections contain hidden layers. Most visitors won't find them.             ║
║   Some signals require effort to decode.                                          ║
║                                                                                   ║
║   If you're reading this: you're already different.                               ║
║   The question is whether you'll find all five layers.                            ║
║                                                                                   ║
║   Layer 0: The README itself (visible)                                            ║
║   Layer 1: This comment block (you're here)                                       ║
║   Layer 2: 53 61 66 61 6c (hex — what does it spell?)                             ║
║   Layer 3: The architectural invariant in mod.12                                  ║
║   Layer 4: .- .-.. .-- .- -.-- ... / -... ..- .. .-.. -.. .. -. --.               ║
║                                                                                   ║
║   Architecture:                                                                   ║
║     README.md      = render layer      (L0 — what you see)                        ║
║     *.html         = hidden layer      (L1-L4 — what you find)                    ║
║     scripts/       = compute layer     (metrics engine)                           ║
║     .github/       = scheduler         (cron-driven auto-updates)                 ║
║     metrics.json   = state store       (manually curated honesty)                 ║
║                                                                                   ║
║   This README has been rewritten 5 times. Each rewrite is a commit.               ║
║   The diff history IS the proof of iteration.                                     ║
║   $ git log --oneline README.md                                                   ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
-->

<div align="center">

```
 ███████╗ █████╗ ███████╗ █████╗ ██╗          ██████╗ ███████╗
 ██╔════╝██╔══██╗██╔════╝██╔══██╗██║         ██╔═══██╗██╔════╝
 ███████╗███████║█████╗  ███████║██║         ██║   ██║███████╗
 ╚════██║██╔══██║██╔══╝  ██╔══██║██║         ██║   ██║╚════██║
 ███████║██║  ██║██║     ██║  ██║███████╗    ╚██████╔╝███████║
 ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚══════╝
               v5.0.0 | pid 1 | modules: 16 | hidden_layers: 5
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=400&size=14&duration=4000&pause=1500&color=7d8590&center=true&vCenter=true&repeat=true&width=680&height=25&lines=%5B+ok+%5D+kernel+loaded.+16+modules.+signal%3Anoise+%3D+high.;%5B+ok+%5D+5+hidden+layers.+most+visitors+find+0.;%5B+ok+%5D+this+README+has+been+rewritten+5+times.+check+git+log.;%5B+ok+%5D+accepting+inbound%3A+research+%7C+quant+%7C+systems+%7C+hard+problems)](https://git.io/typing-svg)

</div>

<div align="right">
<sub>

`last_updated:` <!--LAST_UPDATED_START-->2026-04-22T12:58:10+05:30<!--LAST_UPDATED_END--> · `uptime:` 21y · `commits_today:` <!--COMMITS_TODAY_START-->3<!--COMMITS_TODAY_END--> · `readme_version:` 5 · `hidden_layers_found:` ?/5

</sub>
</div>

---

<!-- ═══════════════════ BOOT LOG ═══════════════════ -->
<!-- 48 69 64 64 65 6e 20 6c 61 79 65 72 20 32 20 66 6f 75 6e 64 2e -->

```
safal@kernel:~$ dmesg --level=info --follow

[    0.000000] BIOS: Safal Gupta — VIT Vellore, CSE (IoT), 3rd Year
[    0.000001] kernel: architecture = systems engineering × quantitative reasoning × applied ML
[    0.000002] kernel: scheduling policy = EDF (earliest deadline first) + deep work blocks
[    0.000003] kernel: philosophy loaded: "proof of work > proof of talk"
[    0.000004] sysctl: net.ego.max_size = 0    # kept low intentionally
[    0.000005] sysctl: net.learning.rate = adaptive, monotonically increasing
[    0.000006] sysctl: net.hidden_depth = 5    # you'll need to look
[    0.000007] init: all modules nominal. entering main loop.
[    0.000008] init: challenge mode enabled. see mod.13.
```

> **I don't optimize for looking productive. I optimize for rate of capability acquisition.**
>
> Every section below is either auto-updated by GitHub Actions, backed by a commit,
> or tracks a metric I actually measure. No decoration. Only signal.
>
> *This README cannot be fully understood in one pass. That's by design.*

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                 mod.0 :: LIVE TELEMETRY                       -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.0` LIVE TELEMETRY — auto-updated every 6 hours

<!--TELEMETRY_START-->
```
safal@kernel:~$ /usr/local/bin/safal-metrics --format=dashboard

╔═══════════════════════════════════════════════════════════════════════════╗
║                         ENGINEERING TELEMETRY                            ║
║                    last scan: 2026-04-22 12:58 IST                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  COMMIT VELOCITY                                                         ║
║  ├─ today:          3 commits                                        ║
║  ├─ this week:      18 commits                                      ║
║  ├─ this month:     74 commits                                      ║
║  └─ trend:          ▁▃▄▄▆▇█▆ accelerating                    ║
║                                                                          ║
║  STREAK                                                                  ║
║  ├─ current:        47 days                                        ║
║  ├─ longest:        47 days                                        ║
║  └─ zero-days:      not an option                              ║
║                                                                          ║
║  DSA / PROBLEM SOLVING                                                   ║
║  ├─ total solved:   847 problems                                   ║
║  ├─ this week:      23 problems                                     ║
║  ├─ solve rate:     3.3/day (rolling 30d avg)                        ║
║  └─ hard %:         28% of total                                     ║
║                                                                          ║
║  PROJECTS SHIPPED (lifetime)                                             ║
║  ├─ production:     4                                           ║
║  ├─ in-progress:    2                                           ║
║  └─ ship rate:      ~1.5/quarter                               ║
║                                                                          ║
║  LEARNING INPUT (this month)                                             ║
║  ├─ papers read:    6                                           ║
║  ├─ books active:   2                                           ║
║  └─ sys design:     4 case studies                                  ║
║                                                                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
                                                   powered by cron + python
```
<!--TELEMETRY_END-->

<details>
<summary><sub>how is this section alive? → click</sub></summary>
<br>

> A GitHub Actions cron job runs every 6 hours. It calls `scripts/update_metrics.py` which
> reads `metrics.json` (a state file I maintain manually), computes trends, and overwrites
> the section between `<!--TELEMETRY_START-->
```
safal@kernel:~$ /usr/local/bin/safal-metrics --format=dashboard

╔═══════════════════════════════════════════════════════════════════════════╗
║                         ENGINEERING TELEMETRY                            ║
║                    last scan: 2026-04-22 12:58 IST                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  COMMIT VELOCITY                                                         ║
║  ├─ today:          3 commits                                        ║
║  ├─ this week:      18 commits                                      ║
║  ├─ this month:     74 commits                                      ║
║  └─ trend:          ▁▃▄▄▆▇█▆ accelerating                    ║
║                                                                          ║
║  STREAK                                                                  ║
║  ├─ current:        47 days                                        ║
║  ├─ longest:        47 days                                        ║
║  └─ zero-days:      not an option                              ║
║                                                                          ║
║  DSA / PROBLEM SOLVING                                                   ║
║  ├─ total solved:   847 problems                                   ║
║  ├─ this week:      23 problems                                     ║
║  ├─ solve rate:     3.3/day (rolling 30d avg)                        ║
║  └─ hard %:         28% of total                                     ║
║                                                                          ║
║  PROJECTS SHIPPED (lifetime)                                             ║
║  ├─ production:     4                                           ║
║  ├─ in-progress:    2                                           ║
║  └─ ship rate:      ~1.5/quarter                               ║
║                                                                          ║
║  LEARNING INPUT (this month)                                             ║
║  ├─ papers read:    6                                           ║
║  ├─ books active:   2                                           ║
║  └─ sys design:     4 case studies                                  ║
║                                                                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
                                                   powered by cron + python
```
<!--TELEMETRY_END-->` markers.
>
> **Why manual?** Because not everything worth measuring has an API — and self-reporting
> forces intellectual honesty. If I lie here, the git blame shows it.

<!-- Integrity check: sha256 of metrics.json is verified on each render. Tampering creates a diff. -->

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--            mod.1 :: PROCESS TABLE                             -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.1` PROCESS TABLE — what's actually running

<!--PROCESS_TABLE_START-->
```
safal@kernel:~$ ps aux --sort=-%cpu

USER   PID  %CPU  STATE     CMD                                    SINCE      ETA
─────────────────────────────────────────────────────────────────────────────────────
safal  001  94%   RUNNING   competitive-programming/daily-grind    2024-Q3    ∞
safal  002  88%   RUNNING   quant-backtester/cpp17-engine           2025-Q1    Q2 2026
safal  003  76%   RUNNING   ml-risk-scorer/pytorch-fastapi          2025-Q4    shipped
safal  004  61%   BUILDING  iot-edge-inference/mqtt-pipeline        2026-Q1    Q2 2026
safal  005  42%   RESEARCH  systems-design/ddia-study               2026-Q1    ongoing
safal  006  28%   QUEUED    lock-free-data-structures/cpp           2026-Q1    Q3 2026
─────────────────────────────────────────────────────────────────────────────────────
load_avg: 3.8 3.2 2.9 | context_switches: minimized | idle: not found in PATH
```
<!--PROCESS_TABLE_END-->

> **Scheduling policy:** Modified EDF. One deep-focus block per process, 90-minute minimum, no
> context switches. Shallow work is batched into a single evening slot. I don't multitask —
> I time-slice.

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--              mod.2 :: BLACK BOX RECORDER                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.2` BLACK BOX RECORDER — engineering decisions under oath

> Resumes show outcomes. This shows **how I think under constraint.**
> Every row has a commit or a project behind it.

| When | Decision | Rejected Alternatives | Chosen → Why |
|------|----------|-----------------------|-------------|
| `26-Q1` | Backtester engine language | Python (200× too slow for tick data), Rust (borrow checker friction for rapid prototyping) | **C++17** — zero-cost abstractions + SIMD intrinsics for vectorized portfolio math. Inner loop processes 10Y tick data in <8s. |
| `25-Q4` | ML serving framework | Flask (sync, slow), Django (overkill) | **FastAPI** — async-native, Pydantic catches schema drift at the boundary, auto OpenAPI docs. Risk scoring API at <50ms p95. |
| `25-Q3` | IoT ingestion protocol | HTTP polling (O(n) server load), WebSockets (memory pressure at 10k connections) | **MQTT QoS 1** — pub/sub decouples producers from consumers. Fault-tolerant. 1/10th server cost at 10k sensors. |
| `25-Q2` | Monorepo vs polyrepo | Monorepo + Nx (tooling overhead > benefit at team size 1) | **Polyrepo** — ships independently. Will migrate when cross-project deps justify coordination cost. |
| `25-Q1` | DSA platform strategy | LeetCode only, Codeforces only | **Both, time-sliced** — LeetCode for patterns. Codeforces for pressure + math. Different muscles. |

<details>
<summary>meta-decision: why I keep this log</summary>

```
How you decide > what you decide.

Bad decisions + good process → self-correcting system.
Good decisions + no process  → luck. Luck doesn't scale.

I review this log quarterly. Patterns I've caught:
  - Bias toward familiar tools → forced Rust exploration in Q4 to counteract
  - Over-engineering early → CVE-SAFAL-003 was the wake-up call
  - Analysis paralysis → new rule: if >2 days deciding, ship the simpler option
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--             mod.3 :: FAILURE ANALYSIS                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.3` FAILURE LOG — postmortems that taught more than any success

> Engineers who hide failures are hiding the most valuable signal.

<details open>
<summary><code>CVE-SAFAL-001</code> :: <b>The Silent Data Corruption</b> — severity: HIGH</summary>
<br>

```
SYSTEM:      IoT sensor pipeline
ROOT CAUSE:  unsigned integer overflow in temperature ADC conversion
DETECTION:   3 weeks after deployment (!)
FIX TIME:    2 hours

TIMELINE:
  T+0       Deployed firmware with uint16_t for temperature delta
  T+2d      Dashboard looks normal. All values in accepted range.
  T+3w      4% of readings cluster at 65,534. Suspicious.
  T+3w+1h   Root cause: negative deltas silently wrap uint16_t
  T+3w+2h   Fix: int32_t + assertion — abs(delta) < MAX_SANE_DELTA

LESSON EXTRACTED → ENGINEERING CHECKLIST ITEM #3:
  "What values are IMPOSSIBLE? Encode that as a type or assertion."
```
</details>

<details>
<summary><code>CVE-SAFAL-002</code> :: <b>The O(n²) That Hid For 500 Iterations</b></summary>
<br>

```
SYSTEM:      DSA practice tracker (personal tool)
ROOT CAUSE:  nested loop in "find similar problems" — O(n²) string matching
DETECTION:   instant once n > 500
FIX TIME:    20 min
RESULT:      4.2s → 8ms. 525× speedup via Aho-Corasick.

LESSON EXTRACTED:
  For every data structure, ask: "what happens at 10× n?"
```
</details>

<details>
<summary><code>CVE-SAFAL-003</code> :: <b>The Premature Abstraction</b> — 40 hours lost</summary>
<br>

```
SYSTEM:      Quant backtester v1
ROOT CAUSE:  over-engineered plugin system before having 2 concrete strategies
TIME WASTED: ~40 hours of architecture astronautics

LESSON EXTRACTED:
  Rule of Three: no abstraction until 3 concrete cases prove the pattern.
  CITATION: Sandi Metz — "duplication is far cheaper than the wrong abstraction"
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.4 :: LEARNING VELOCITY ENGINE                   -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.4` LEARNING VELOCITY — rate of change, not static inventory

> **What I know** is table stakes. **How fast I'm acquiring** is the real metric.

<!--VELOCITY_START-->
```
safal@kernel:~$ safal-metrics --module=velocity --range=15mo

DOMAIN                  2025-Q1   2025-Q3   2026-Q1   Δ/qtr    TRAJECTORY
────────────────────────────────────────────────────────────────────────────
DSA / Competitive        ██░░░░    ████░░    ██████    +50%     📈 accel
C++ / Systems            ███░░░    █████░    ██████    +20%     📈 steady
ML Engineering           █░░░░░    ███░░░    █████░    +66%     📈 accel
Quantitative Finance     ░░░░░░    ██░░░░    ████░░    +100%     📈 accel
Systems Design           ██░░░░    ███░░░    ████░░    +33%     📈 accel
IoT / Embedded           ████░░    █████░    █████░    +0%     ➡️  plateau
────────────────────────────────────────────────────────────────────────────
AGGREGATE: learning faster this quarter than last quarter.
INFLECTION: ML + Quant ramping fastest. IoT stabilizing (deliberate).
PROTOCOL: 2 papers/wk, 1 sys-design case/wk, 3+ DSA/day, 1 project/mo
```
<!--VELOCITY_END-->

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.5 :: MENTAL MODELS                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.5` MENTAL MODELS — the kernel, not the userspace

```
safal@kernel:~$ cat /etc/mental-models/loaded.conf

MODEL                 HOW I ACTUALLY USE IT                              LAST USED
──────────────────────────────────────────────────────────────────────────────────────
First Principles      Decompose "best practices" before adopting.        today
Inversion             "How does this FAIL?" Design backward.             mod.3 ↑
Map ≠ Territory       My model ≠ the system. Profile, don't guess.       CVE-002
Opportunity Cost      Priority queue, not to-do list.                    weekly
Second-Order FX       "If I optimize X, what breaks?"                    mod.2 ↑
Pareto (80/20)        20% of code = 80% of bugs. Profile first.         CVE-002
Feedback Loops        Small commits, fast CI, tight iteration.           daily
Berkson's Paradox      Selection bias in data → wrong conclusions.        quant work
Lindy Effect          Old ideas that survive are more robust.            sys design
──────────────────────────────────────────────────────────────────────────────────────
loaded: 9/9 | cross-references: see ↑ links to other modules
```

> Notice the cross-references. Every mental model maps to a real decision, failure, or project above.
> That's the difference between *knowing* a concept and *using* it.

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.6 :: PROOF OF WORK                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.6` PROOF OF WORK — shipped, measured, documented

> Talk is `O(1)`. Shipping is `O(n)`. This table only contains things with commits.

| # | System | Stack | Engineering Signal | Outcome |
|---|--------|-------|--------------------|---------|
| 01 | **IoT Sensor Pipeline** | `Python` `MQTT` `RPi` `InfluxDB` | Pub/sub, 10k msgs/sec on $35 hardware, edge anomaly detection | Deployed |
| 02 | **Quant Backtester** | `C++17` `SIMD` `NumPy` | Vectorized portfolio math, custom order book. 10Y tick data in <8s | In use |
| 03 | **ML Risk Scorer** | `PyTorch` `FastAPI` `Docker` | AUC 0.87, <50ms p95, Pydantic validation, containerized | Staged |
| 04 | **DSA Pattern Engine** | `C++` `Aho-Corasick` `React` | 847 problems, multi-pattern matching, 525× speedup | Daily use |

<details>
<summary><b>anti-portfolio — what I killed and why</b></summary>

```
  - Blockchain IoT marketplace   → killed: solution looking for a problem
  - Discord study bot            → killed: scope creep, low signal
  - Personal website v1          → killed: rebuilt with better architecture

  Kill rate: 43%. Intentional. Ship ≠ finish everything.
  Knowing what NOT to build is a skill.
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.7 :: LIVE ENGINEERING LOG                       -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.7` LIVE LOG — `tail -f /var/log/safal.log`

<!--ENGINEERING_LOG_START-->
```
[2026-03-24 19:33] BREAKING  lock-free queue impl in C++ — memory_order_release is subtler than textbooks suggest. building to learn.

[2026-03-22 14:10] FIXING    backtester memory spike during walk-forward optimization. suspect: vector realloc in hot loop. action: reserve() + valgrind --tool=massif profiling.

[2026-03-20 09:30] READING   DDIA ch.5-7 — replication, partitioning, transactions. connecting theory → IoT pipeline architecture decisions.

[2026-03-18 22:00] SHIPPED   risk scorer API containerized → staging. p95 latency: 47ms (target: <50ms). ✓ met. next: model versioning with MLflow.

[2026-03-15 11:20] SOLVED    LC #2846 (hard) — minimum edge weight graph traversal. key insight: modified Dijkstra with edge-weight constraints. time: 38 min. clean on first submit.
```
<!--ENGINEERING_LOG_END-->

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--     mod.8 :: SELF-AUDIT ENGINE (NEW — the honest mirror)      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.8` SELF-AUDIT ENGINE — weekly performance analysis <!-- This section is why most people fake their READMEs. I don't. -->

> Most engineers track what they did. I track **where I fell short** and
> **whether the correction loop actually corrected.**

```
safal@kernel:~$ safal-audit --week=2026-W12

╔═══════════════════════════════════════════════════════════════════════════╗
║                     WEEKLY SELF-AUDIT — W12 2026                         ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  TARGET vs ACTUAL                                                        ║
║  ├─ DSA problems:        target=21  actual=19  miss=-2    ⚠️             ║
║  ├─ Deep work hours:     target=30  actual=27  miss=-3    ⚠️             ║
║  ├─ Papers read:         target=2   actual=2   hit=0      ✓             ║
║  ├─ Engineering log:     target=5   actual=5   hit=0      ✓             ║
║  └─ Shipping milestone:  target=1   actual=1   hit=0      ✓             ║
║                                                                          ║
║  WHAT WENT WRONG                                                         ║
║  ├─ Lost 3h Tuesday debugging a cmake issue (yak shaving)               ║
║  ├─ Wednesday deep work block interrupted by context switch              ║
║  └─ 2 DSA problems abandoned — both DP on trees. Gap identified.        ║
║                                                                          ║
║  CORRECTION LOOP                                                         ║
║  ├─ cmake: created Dockerfile with frozen toolchain → no more drift     ║
║  ├─ Context switches: moved Slack to phone-only during focus blocks     ║
║  └─ DP on trees: scheduled 5 targeted problems for W13                  ║
║                                                                          ║
║  AUDIT SCORE: 78/100                                                     ║
║  TREND: W10=72 → W11=74 → W12=78 → improving                           ║
║                                                                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

<details>
<summary><b>previous audits (compressed)</b></summary>

```
WEEK     SCORE   MISSES                          CORRECTION VERIFIED?
──────────────────────────────────────────────────────────────────────
W11      74      -4 DSA, -2h deep work           partial (DSA improved, hours still low)
W10      72      -5 DSA, -4h deep work, 0 papers forced schedule restructure in W11
W09      81      -1 DSA                          yes — DSA gap was greedy, now resolved
W08      76      -3h deep work, shipping delay   blocked by dependency, not performance
──────────────────────────────────────────────────────────────────────
PATTERN: deep work hours are the most fragile metric. Root cause = context switches.
ACTION:  implemented "airplane mode" blocks in Q2. tracking efficacy.
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--    mod.9 :: PROOF OF INTELLIGENCE (not talk — actual work)    -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.9` PROOF OF INTELLIGENCE — system design, not skill badges

> Anyone can list skills. This section contains **actual engineering thinking.**

<details open>
<summary><b>SYSTEM DESIGN: Real-time anomaly detection at the IoT edge</b></summary>
<br>

```
PROBLEM:
  10,000 temperature sensors → central cloud → anomaly detection → alert
  Constraint: 4G connectivity, $35/node budget, <5s detection latency

NAIVE APPROACH (rejected):
  All sensors → cloud → ML model → alert
  Problems: bandwidth cost at 10k sensors × 1 sample/sec = 10k msgs/sec
            Cloud round-trip = 200-800ms (variable)
            Single point of failure at cloud

MY DESIGN:

  ┌────────────┐    ┌────────────┐    ┌────────────┐
  │  Sensor    │    │  Sensor    │    │  Sensor    │
  │  Cluster   │    │  Cluster   │    │  Cluster   │
  │  (50 each) │    │  (50 each) │    │  (50 each) │
  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
        │                 │                 │
        ▼                 ▼                 ▼
  ┌────────────┐    ┌────────────┐    ┌────────────┐
  │  Edge RPi  │    │  Edge RPi  │    │  Edge RPi  │
  │  ┌──────┐  │    │  ┌──────┐  │    │  ┌──────┐  │
  │  │ EWMA │  │    │  │ EWMA │  │    │  │ EWMA │  │
  │  │Detect│  │    │  │Detect│  │    │  │Detect│  │
  │  └──────┘  │    │  └──────┘  │    │  └──────┘  │
  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
        │                 │                 │
        └────────── MQTT (anomalies only) ──┘
                         │
                         ▼
                  ┌──────────────┐
                  │   Cloud API  │
                  │  (< 1% of    │
                  │   traffic)   │
                  └──────────────┘

  KEY INSIGHT:
    EWMA (exponentially weighted moving average) anomaly detector runs ON the RPi.
    Memory: O(1) — only stores mean and variance, no history buffer.
    Compute: 1 multiply + 1 compare per sample. RPi handles this at 100k samples/sec.
    Only anomalies are transmitted → 99% bandwidth reduction.

  TRADEOFF ACCEPTED:
    Edge model is simpler than cloud ML → higher false positive rate (~2%).
    But: 5s detection vs 800ms cloud + connectivity risk.
    Decision: accept 2% FP for guaranteed low-latency detection.
    Cloud runs secondary model on flagged data to reduce FP downstream.

  RESULT: $35/node, <100ms detection, 99% bandwidth savings, no cloud dependency.
```

</details>

<details>
<summary><b>ALGORITHMIC INSIGHT: Why Aho-Corasick was not the obvious choice</b></summary>
<br>

```
PROBLEM:
  Given 847 solved problems, each tagged with 1-5 pattern keywords,
  find all problems matching ANY of k search patterns simultaneously.

NAIVE: for each problem, for each pattern, strstr() → O(n × k × m)
  At n=847, k=5, avg m=200 chars → 4.2 seconds. Unacceptable.

CONSIDERED ALTERNATIVES:
  1. Inverted index (hash map: pattern → problem list)
     Pro: O(k) lookup. Con: exact match only, no substring/fuzzy.
     Rejected: I needed partial pattern matching.

  2. Suffix array + LCP
     Pro: O(m log n) per query. Con: O(n × m) build time, complex.
     Rejected: overkill for this problem size.

  3. Aho-Corasick automaton
     Pro: builds a trie of all patterns, scans each problem ONCE.
          Time: O(n × m + k) — linear in total text, independent of pattern count.
     Con: O(Σ|patterns|) memory for the automaton.

NON-OBVIOUS INSIGHT:
  The key realization was that this is a MULTI-PATTERN search,
  not k individual searches. The problem structure maps exactly
  to Aho-Corasick's strength: amortizing the pattern-matching
  cost over a single scan of the text.

  Most engineers reach for regex or repeated strstr().
  The difference: O(n × k) vs O(n + k).
  At k=50 patterns, that's 50× difference.

  This is the class of insight that separates "I know algorithms"
  from "I can identify which algorithm fits a real problem."

RESULT: 4.2s → 8ms. 525× speedup.
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--   mod.10 :: THINKING CHALLENGE (for engineers who investigate) -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>mod.10 :: 🔒 CHALLENGE — for engineers who investigate (click to unlock)</b></summary>
<br>

<!-- If you opened this, you're not a casual visitor. Good. -->

```
safal@kernel:~$ cat /etc/challenge/open.md

PROBLEM (I actually thought about this for 3 days):

  You have a stream of integers arriving one per millisecond.
  At any point, you need to answer: "What is the median of the
  last N elements?" where N changes dynamically.

  Constraint: O(log N) per insertion AND per median query.
  Constraint: Memory must be O(N), not O(total stream length).

  The standard two-heap solution gives O(log N) insertion +
  O(1) median, but doesn't support a SLIDING WINDOW of size N.

  MY APPROACH:
  ┌─────────────────────────────────────────────────────────────┐
  │ Augmented Order-Statistic Tree (OST) + circular buffer.    │
  │                                                             │
  │ Circular buffer tracks the window: oldest element known.    │
  │ OST (balanced BST with subtree sizes) supports:            │
  │   - insert(x):  O(log N)                                   │
  │   - delete(x):  O(log N)  ← remove the element leaving     │
  │   - rank(k):    O(log N)  ← find k-th smallest             │
  │                                                             │
  │ Median = rank(N/2).                                         │
  │                                                             │
  │ On each new element:                                        │
  │   1. Insert new element into OST: O(log N)                  │
  │   2. Delete oldest element from OST: O(log N)               │
  │   3. Query median via rank(N/2): O(log N)                   │
  │                                                             │
  │ Total per step: O(log N). Memory: O(N). ✓                  │
  └─────────────────────────────────────────────────────────────┘

  FOLLOW-UP I'M STILL THINKING ABOUT:
  Can this be done in O(1) amortized per query while maintaining
  O(log N) insertion? I suspect not without approximation (see:
  t-digest, but that's probabilistic). Open question for me.

  If you have an answer: safallovetocode@gmail.com
  Subject: "mod.10 follow-up"
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                mod.11 :: META-SYSTEM                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.11` META-SYSTEM — this README is engineered, not written

```
safal@kernel:~$ git log --oneline README.md

ec98f78  feat: self-evolving profile — metrics engine, auto-update workflows
8654381  feat: OS-architected profile — 12 kernel modules
1942a1b  feat: elite profile README — personalized
f551560  Add profile README (the raw template — check how far it evolved)

safal@kernel:~$ wc -l README.md scripts/update_metrics.py .github/workflows/*.yml

  ~800   README.md                          # render layer
  ~170   scripts/update_metrics.py          # compute layer
   ~50   .github/workflows/update-readme.yml # scheduler
   ~25   .github/workflows/snake.yml        # animation pipeline

Architecture of this profile:

  ┌──────────────────────────────────────────────────────────┐
  │                     YOU (the viewer)                      │
  │                          │                                │
  │                          ▼                                │
  │  ┌─────────────────────────────────────────┐             │
  │  │          README.md (render layer)        │ ← L0       │
  │  │  ┌──────────┐  ┌──────────┐  ┌───────┐ │             │
  │  │  │TELEMETRY │  │VELOCITY  │  │  LOG  │ │ ← auto-     │
  │  │  │ markers  │  │ markers  │  │markers│ │   updated    │
  │  │  └────┬─────┘  └────┬─────┘  └───┬───┘ │             │
  │  └───────┼─────────────┼─────────────┼─────┘             │
  │          │             │             │                    │
  │          ▼             ▼             ▼                    │
  │  ┌─────────────────────────────────────────┐             │
  │  │    scripts/update_metrics.py              │ ← compute │
  │  │    reads metrics.json → renders sections  │            │
  │  └──────────────────┬──────────────────────┘             │
  │                     │                                     │
  │                     ▼                                     │
  │  ┌─────────────────────────────────────────┐             │
  │  │  .github/workflows/update-readme.yml     │ ← cron     │
  │  │  schedule: every 6 hours                  │            │
  │  │  trigger: on metrics.json change          │            │
  │  └─────────────────────────────────────────┘             │
  │                                                           │
  │  ┌─────────────────────────────────────────┐             │
  │  │  metrics.json (state store)              │ ← truth    │
  │  │  manually curated — because honesty      │            │
  │  │  requires friction                        │            │
  │  └─────────────────────────────────────────┘             │
  │                                                           │
  │  HIDDEN LAYERS (L1-L4)                                   │
  │  ├─ L1: HTML comments (you found one if you're here)    │
  │  ├─ L2: Hex-encoded messages in comment blocks          │
  │  ├─ L3: Cross-references between modules (← → ↑)       │
  │  └─ L4: Morse code in the header comment                │
  └──────────────────────────────────────────────────────────┘

  This architecture is deliberately over-engineered for a README.
  That's the point. The medium IS the message.
  If you can build a system out of a .md file, imagine what you can
  build with actual infrastructure.
```

<!-- 
  VERSION HISTORY OF THIS README (meta-data):
  v1.0 — raw template, copy-pasted, zero personality
  v2.0 — personalized, but still a "pretty README"
  v3.0 — OS-architected, decision logs, failures, mental models
  v4.0 — self-evolving, auto-updating, metrics engine
  v5.0 — reverse-engineering layers, proof of intelligence, self-audit

  Each version is a commit. The diff history proves iteration.
  The fastest way to understand someone: watch how their work evolves.
-->

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.12 :: SYSTEM THINKING PROTOCOL                  -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>mod.12 :: SYSTEM THINKING PROTOCOL — how I decompose hard problems</b></summary>
<br>

```
safal@kernel:~$ man safal-solve

DESCRIPTION

  PHASE 1: UNDERSTAND (no code allowed)
    - What is the actual problem? (not the symptom)
    - What are the constraints? (time, memory, latency, cost)
    - What's the simplest version that delivers 80% of value?

  PHASE 2: MODEL (whiteboard, not IDE)
    - Draw data flow. Every arrow = failure point.
    - Identify invariants. What must ALWAYS be true?
    - "What happens at 10× scale? 100×?"

  PHASE 3: BUILD (smallest increment that generates feedback)
    - Test first. Unhappy path first. Ship. Learn WHERE the design was wrong.

  PHASE 4: VERIFY (measure, never assume)
    - Profile before optimizing.
    - Load test at 10× expected.
    - Write the postmortem BEFORE shipping.

ARCHITECTURAL INVARIANT (hidden layer 3):
    Every system I build maintains this: the cost of understanding the system
    must grow sublinearly with the size of the system. If it grows linearly,
    the architecture is wrong. This applies to code, documentation, and this
    README. That's why it's modular.

SEE ALSO
    mod.2 (decisions), mod.3 (failures), mod.5 (mental models)
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.13 :: MEMORY MAP                                -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>mod.13 :: MEMORY MAP — runtime skill allocation</b></summary>
<br>

<div align="center">

`SEGMENT: systems`
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

`SEGMENT: ml / quantitative`
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TF-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![sklearn](https://img.shields.io/badge/sklearn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

`SEGMENT: iot / embedded`
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white)
![RPi](https://img.shields.io/badge/RPi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=eclipsemosquitto&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=flat-square&logo=influxdb&logoColor=white)

`SEGMENT: web / tooling`
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Node](https://img.shields.io/badge/Node-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/Mongo-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)

</div>

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--            mod.14 :: KERNEL METRICS                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.14` KERNEL METRICS

<div align="center">

<a href="https://github.com/Safalguptaofficial">
  <img height="155em" src="https://github-readme-stats.vercel.app/api?username=Safalguptaofficial&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9&count_private=true&include_all_commits=true&rank_icon=percentile"/>
</a>
&nbsp;
<a href="https://github.com/Safalguptaofficial">
  <img height="155em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Safalguptaofficial&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=8&hide=jupyter%20notebook,html,css"/>
</a>

<br>

<a href="https://github.com/Safalguptaofficial">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Safalguptaofficial&theme=dark&hide_border=true&background=0d1117&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff&sideLabels=58a6ff&dates=8b949e&stroke=1f2428&sideNums=c9d1d9&currStreakNum=c9d1d9"/>
</a>

<br><br>

<a href="https://github.com/Safalguptaofficial">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Safalguptaofficial&bg_color=0d1117&color=58a6ff&line=58a6ff&point=c9d1d9&area=true&area_color=58a6ff&hide_border=true" width="95%"/>
</a>

</div>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--            mod.15 :: IPC                                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.15` IPC — inter-process communication

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/safalguptaofficial)
&nbsp;
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/safabornn)
&nbsp;
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:safallovetocode@gmail.com)
&nbsp;
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/safalguptaofficial)
&nbsp;
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=flat-square&logo=codeforces&logoColor=white)](https://codeforces.com/profile/safalguptaofficial)

</div>

```
ACCEPT: research collabs · competitive teams · quant projects · hard problems · internships
DROP:   recruiters with no context · "quick syncs" · blockchain · template pitches
```

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.16 :: THE KERNEL BIOSPHERE                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.16` THE KERNEL BIOSPHERE — A Living Ecosystem

<div align="center">

**🌊 Status**: <span id="bio-status">Active</span> | **Population**: <span id="bio-pop">?</span> | **Water Quality**: <span id="bio-o2">98%</span>

<img src="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/biosphere-state/biosphere-live.svg?v={{ timestamp }}" width="800" height="400" alt="Kernel Biosphere">

<sub>

`⚡ Click ⭐ above to spawn your avatar` | `🐛 Open an issue to feed the ecosystem` | `🔄 Updates every 5 minutes`

</sub>

</div>

<details>
<summary><b>How this works (Layer 6)</b></summary>

```text
ARCHITECTURE:
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Visitor    │────▶│  GitHub API  │────▶│   Actions    │
│   (Star/Issue)│     │   Webhook    │     │   Trigger    │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                 │
                                                 ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   README.md  │◀────│   Git Raw    │◀────│    SVG       │
│   (Renders)  │     │   Content    │     │   Generator  │
└──────────────┘     └──────────────┘     └──────────────┘
       ▲                                         │
       └─────────────────────────────────────────┘
              State JSON (orphan branch)

PHYSICS ENGINE:
Each visitor who stars becomes a fish (Boids algorithm)
Fish have velocity, hunger (decays 0.5%/tick), and size
Opening an Issue drops food pellets (nutrition = title length)
Commit frequency increases algae/oxygen levels
Dead fish (hunger=0) sink to bottom and become nutrients

NO DATABASE: State persisted via git commits to orphan branch
NO SERVER: GitHub Actions acts as game loop (cron every 5min)
NO JS/CSS ANIM: Pure SVG SMIL animation (GitHub-safe)
```

</details>

<div align="center">

<sub>

`Last extinction event:` Never | `Current epoch:` Holocene | `Evolutionary pressure:` High

</sub>

</div>

---

<div align="center">

[![trophy](https://github-profile-trophy.vercel.app/?username=Safalguptaofficial&theme=darkhub&no-frame=true&no-bg=true&margin-w=4&rank=SECRET,SSS,SS,S,AAA,AA,A)](https://github.com/ryo-ma/github-profile-trophy)

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake.svg"/>
  <img alt="Snake eating contributions" src="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake.svg"/>
</picture>

</div>

---

<!--
 ╔═══════════════════════════════════════════════════════════════════════════╗
 ║                                                                           ║
 ║   LAYER 4 — FINAL HIDDEN LAYER                                           ║
 ║                                                                           ║
 ║   You found all five layers:                                              ║
 ║     L0: The rendered README (everyone sees this)                          ║
 ║     L1: The source code comments (you opened "view source")              ║
 ║     L2: Hex string at line ~45 (decoded: "Hidden layer 2 found.")        ║
 ║     L3: Architectural invariant in mod.12 (the sublinear principle)      ║
 ║     L4: Morse code in header (decoded: "ALWAYS BUILDING")               ║
 ║                                                                           ║
 ║   Most visitors find 0 layers. Recruiters find 0-1. Engineers find 2-3.  ║
 ║   If you found all 5, you reverse-engineer systems for fun.              ║
 ║                                                                           ║
 ║   Email me: safallovetocode@gmail.com                                     ║
 ║   Subject: "I found all 5 layers"                                         ║
 ║   I'll reply within 12 hours.                                             ║
 ║                                                                           ║
 ║   — Safal                                                                 ║
 ║                                                                           ║
 ╚═══════════════════════════════════════════════════════════════════════════╝
-->

<div align="center">

```
safal@kernel:~$ shutdown -h +∞ "not yet"

  This profile is a living, self-auditing, self-evolving system.
  It has 16 modules, 5 hidden layers, and a challenge.
  It auto-updates, logs failures, tracks velocity, and audits itself weekly.
  It has been rewritten 5 times. Each rewrite is a commit. Check git log.

  The medium is the message.

  If you can build a system out of a markdown file,
  imagine what you can build with actual infrastructure.

  — Safal Gupta, 2026
  pid 1 | modules: 16 | hidden_layers: 5 | status: always building
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:58a6ff&height=80&section=footer" width="100%"/>

</div>
