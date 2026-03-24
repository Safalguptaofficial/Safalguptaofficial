<!--
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║   SAFAL_OS v4.0.0-rc1                                                             ║
║   Kernel: safal-engineered × self-evolving × auto-updating                        ║
║   Build:  2026.03.24-193305+0530                                                  ║
║                                                                                   ║
║   This is not a README. This is a running system.                                 ║
║   Some sections auto-update via GitHub Actions cron.                              ║
║   Some sections contain hidden signals. You'll find them if you look.             ║
║                                                                                   ║
║   Design philosophy:                                                              ║
║     README.md      = render layer (what you see)                                  ║
║     scripts/       = compute layer (metrics engine)                               ║
║     .github/       = scheduler (cron-driven auto-updates)                         ║
║     you            = if you're reading this comment, you think like I do          ║
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
                      v4.0.0 | pid 1 | init: curiosity
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=400&size=14&duration=4000&pause=1500&color=7d8590&center=true&vCenter=true&repeat=true&width=680&height=25&lines=%5B+ok+%5D+kernel+loaded.+all+modules+nominal.+signal%3Anoise+%3D+high.;%5B+ok+%5D+systems+thinker.+not+a+coder.+an+engineer.;%5B+ok+%5D+CSE+(IoT)+%40+VIT+Vellore+%E2%80%A2+Class+of+2027;%5B+ok+%5D+accepting+inbound%3A+research+%7C+quant+%7C+systems+%7C+hard+problems)](https://git.io/typing-svg)

</div>

<div align="right">
<sub>

`last_updated:` <!--LAST_UPDATED_START-->2026-03-24T19:39:23+05:30<!--LAST_UPDATED_END--> · `uptime:` 21y · `commits_today:` <!--COMMITS_TODAY_START-->3<!--COMMITS_TODAY_END-->

</sub>
</div>

---

<!-- ═══════════════════ BOOT LOG ═══════════════════ -->

```
safal@kernel:~$ dmesg --level=info --follow

[    0.000000] BIOS: Safal Gupta — VIT Vellore, CSE (IoT), 3rd Year
[    0.000001] kernel: architecture = systems engineering × quantitative reasoning × applied ML
[    0.000002] kernel: scheduling policy = EDF (earliest deadline first) + deep work blocks
[    0.000003] kernel: philosophy loaded: "proof of work > proof of talk"
[    0.000004] sysctl: net.ego.max_size = 0    # kept low intentionally
[    0.000005] sysctl: net.learning.rate = adaptive, monotonically increasing
[    0.000006] init: all modules nominal. entering main loop.
```

> **I don't optimize for looking productive. I optimize for rate of capability acquisition.**
>
> Every section below is either auto-updated by GitHub Actions, backed by a commit,
> or tracks a metric I actually measure. No decoration. Only signal.

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
║                    last scan: 2026-03-24 19:39 IST                       ║
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
<summary><sub>how is this updated? → click</sub></summary>
<br>

> A GitHub Actions cron job runs every 6 hours. It calls a Python script that
> queries the GitHub API for my commit data, reads a `metrics.json` config I maintain
> manually for DSA/learning stats, computes the dashboard, and overwrites this section
> via sed. The workflow is in `.github/workflows/update-readme.yml`. The script is in
> `scripts/update_metrics.py`. You can audit both.

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--            mod.1 :: PROCESS TABLE (currently running)         -->
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
| `25-Q1` | DSA platform strategy | LeetCode only (misses speed training), Codeforces only (misses interview patterns) | **Both, time-sliced** — LeetCode for pattern/company tags. Codeforces for pressure tolerance + math. Different muscles. |

<details>
<summary><b>meta-decision: why I keep this log</b></summary>
<br>

```
How you decide > what you decide.

Bad decisions + good process → self-correcting system.
Good decisions + no process  → luck. Luck doesn't scale.

I review this log quarterly. Patterns emerge:
- Am I biased toward familiar tools? (yes, watch for it)
- Am I over-engineering early? (incident-003 says yes)
- Am I making decisions fast enough? (if >2 days of analysis paralysis, ship the simpler one)
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--             mod.3 :: FAILURE ANALYSIS                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.3` FAILURE LOG — postmortems that taught more than any success

> Engineers who hide failures are hiding the most valuable signal.
> These are real. Each one changed how I build.

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

LESSON EXTRACTED:
  If the type doesn't encode the constraint, the constraint doesn't exist.
  I now start every data pipeline by answering:
  "What values are IMPOSSIBLE? Encode that as a type or an assertion."

STATUS: integrated into personal engineering checklist, item #3
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

FORENSICS:
  Built a tool to tag problems by algorithmic pattern.
  Worked fine at n=200. At n=500, search = 4.2 seconds.
  Profiled with perf: 89% of time in strstr() inside nested loop.
  Replaced with Aho-Corasick multi-pattern matching.
  Result: 4.2s → 8ms. 525× speedup.

LESSON EXTRACTED:
  For every data structure, ask: "what happens at 10× n?"
  If the answer is "100× slower," you have O(n²). Find it before prod does.
```
</details>

<details>
<summary><code>CVE-SAFAL-003</code> :: <b>The Premature Abstraction</b> — 40 hours lost</summary>
<br>

```
SYSTEM:      Quant backtester v1
ROOT CAUSE:  over-engineered plugin system before having 2 concrete strategies
TIME WASTED: ~40 hours of architecture astronautics

WHAT HAPPENED:
  Before writing strategy #1, I built:
    - Abstract StrategyBase with 12 virtual methods
    - Plugin loader with dynamic registration
    - Config-driven strategy selection via YAML
  Strategy #1 needed 3 of 12 methods.
  Strategy #2 needed different methods entirely.
  Rewrote the interface. Then rewrote it again.

LESSON EXTRACTED:
  Rule of Three: no abstraction until three concrete cases prove
  the pattern exists. Premature abstraction is negative productivity.
  Now I ask: "Do I have 3 examples of this pattern? No? Then inline it."

CITATION: Sandi Metz — "duplication is far cheaper than the wrong abstraction"
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.4 :: LEARNING VELOCITY ENGINE                   -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.4` LEARNING VELOCITY — rate of change, not static inventory

> **What I know** is table stakes. **How fast I'm acquiring** is the real metric.
> This section is updated monthly from `metrics.json`.

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

<details>
<summary><b>how I track this</b></summary>

```
I maintain a private metrics.json with weekly snapshots:
{
  "dsa": { "total": 847, "hard_pct": 28, "weekly_avg": 23 },
  "commits": { "this_week": 18, "this_month": 74 },
  "learning": { "papers": 6, "books_active": 2, "sys_design_cases": 4 },
  "velocity": { ... quarterly snapshots ... }
}

A GitHub Action reads this file, computes trends, and renders the dashboard
above. I update the JSON manually because not everything worth measuring
has an API — and the act of manual tracking forces honest self-assessment.
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.5 :: MENTAL MODELS                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.5` MENTAL MODELS — the kernel, not the userspace

> These aren't concepts I've *read about*. They're thinking tools I *apply daily*.
> Each one has changed at least one engineering decision above.

```
safal@kernel:~$ cat /etc/mental-models/loaded.conf

MODEL                 APPLICATION                                         FREQ
──────────────────────────────────────────────────────────────────────────────────
First Principles      Decompose "best practices" before adopting.          daily
                      Most are cargo-culted. Derive from constraints.

Inversion             "How does this system FAIL?" Design backward         every
                      from failure modes. See: CVE-SAFAL-001.              design

Map ≠ Territory       My mental model ≠ the system. Test with data,        every
                      not intuition. Profiling > guessing.                 debug

Opportunity Cost      Every hour on X ≠ spent on Y. I maintain a          weekly
                      priority queue, not a to-do list.

Second-Order FX       "If I optimize for latency, what breaks?"            every
                      Most bugs live in 2nd-order consequences.            tradeoff

Pareto (80/20)        20% of code causes 80% of bugs. Profile before      every
                      rewriting. Never optimize uniformly.                 refactor

Feedback Loops        Tight loops = fast learning. Small commits, fast     daily
                      CI, rapid iteration. Big PRs are learning debt.
──────────────────────────────────────────────────────────────────────────────────
loaded: 7/7 | page_faults: 0 | last_reviewed: 2026-Q1
```

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.6 :: PROOF OF WORK                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.6` PROOF OF WORK — shipped, measured, documented

> Talk is `O(1)`. Shipping is `O(n)`. This table only contains things with commits.

| # | System | Stack | Engineering Signal | Outcome |
|---|--------|-------|--------------------|---------|
| 01 | **IoT Sensor Pipeline** | `Python` `MQTT` `RPi` `InfluxDB` | Pub/sub architecture, 10k msgs/sec on $35 hardware, anomaly detection at the edge | Deployed, running |
| 02 | **Quant Backtester** | `C++17` `SIMD` `NumPy` | Vectorized portfolio math, custom order book, walk-forward optimization. 10Y tick data in <8s | In production use |
| 03 | **ML Risk Scorer** | `PyTorch` `FastAPI` `Docker` | AUC 0.87, <50ms p95 serving latency, Pydantic schema validation, containerized | Shipped to staging |
| 04 | **DSA Pattern Engine** | `C++` `Aho-Corasick` `React` | 847 problems indexed, multi-pattern matching, 525× speedup over naive search | Daily driver |

<details>
<summary><b>what's NOT on this list</b></summary>

```
Projects I started and killed:
  - A blockchain-based IoT data marketplace (killed: solution looking for a problem)
  - A Discord bot for study groups (killed: scope creep, low signal)
  - A personal website v1 (killed: rebuilt from scratch with better architecture)

I keep this anti-portfolio because knowing what NOT to build is as
important as knowing what to build. Kill rate: ~40%. That's healthy.
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.7 :: CURRENTLY BREAKING                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.7` LIVE ENGINEERING LOG — `tail -f /var/log/safal.log`

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
<!--           mod.8 :: SYSTEM THINKING PROTOCOL                   -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>mod.8 :: SYSTEM THINKING PROTOCOL — how I decompose hard problems</b></summary>
<br>

```
safal@kernel:~$ man safal-solve

NAME
    safal-solve — four-phase problem decomposition protocol

SYNOPSIS
    safal-solve [--depth=deep] [--ego=0] <problem>

DESCRIPTION

  PHASE 1: UNDERSTAND (no code allowed)
    - What is the actual problem? (not the symptom)
    - What are the constraints? (time, memory, latency, cost, team size)
    - What's the simplest version that delivers 80% of value?
    - Who are the users? What breaks their workflow?

  PHASE 2: MODEL (whiteboard only, IDE stays closed)
    - Draw the data flow. Every arrow = potential failure point.
    - Identify invariants. What must ALWAYS be true?
    - Find the bottleneck. System speed = slowest path.
    - Ask: "What happens at 10× scale? 100×? Does the design hold?"

  PHASE 3: BUILD (smallest increment that generates feedback)
    - Write the test first. If you can't test it, you don't understand it.
    - Build the unhappy path first. Errors > success paths in production.
    - Ship. Get data. The design WILL be wrong — learn WHERE.

  PHASE 4: VERIFY (measure, never assume)
    - Profile before optimizing. Intuition = unvalidated hypothesis.
    - Load test at 10× expected traffic.
    - Write the postmortem BEFORE shipping: "what could go wrong?"

EXAMPLES
    "Rate limiter for 50M users, 10M req/sec"
    → Token bucket > leaky bucket (burst tolerance)
    → Shard by user_id % 64 across Redis nodes → O(1) per check
    → Local cache absorbs 95% — Redis for cross-instance only
    → Fail open under partition (Netflix philosophy)
    → First code: rejection path. Last code: config layer.

SEE ALSO
    mod.2 (decision log), mod.3 (failure log), mod.5 (mental models)
```
</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--           mod.9 :: MEMORY MAP (SKILLS)                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>mod.9 :: MEMORY MAP — runtime skill allocation</b></summary>
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
<!--            mod.10 :: KERNEL METRICS                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.10` KERNEL METRICS

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
<!--            mod.11 :: IPC                                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## `mod.11` IPC — inter-process communication

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
CHANNEL      LATENCY    AVAILABILITY   ROUTE TO
─────────────────────────────────────────────────────────────────────
LinkedIn     < 24h      async          professional, research, collabs
Twitter      < 12h      async          technical takes, hot problems
Email        < 48h      async          formal, proposals, detailed
GitHub       immediate  always         code > all other channels
─────────────────────────────────────────────────────────────────────
ACCEPT: research collabs · competitive teams · quant projects · hard problems · internships
DROP:   recruiters with no context · "quick syncs" · blockchain · template pitches
```

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
 If you've read this far in the source, you're in the top 1% of people
 who visit GitHub profiles. Most people scroll. You investigate.

 That tells me something about you.

 Build something together? → safallovetocode@gmail.com
 Subject line: "I read your source"
 I'll reply within 24 hours. No exceptions.
-->

<div align="center">

```
safal@kernel:~$ shutdown -h +∞ "not yet"

  This profile is a living system.
  It auto-updates. It logs failures. It tracks velocity.
  It breaks, recovers, and ships. Like good software.

  If you're still reading, you think in systems too.
  That's rare. Let's build something.

  — Safal Gupta, 2026
  pid 1 | signal: SIGCONT | status: always building
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:58a6ff&height=80&section=footer" width="100%"/>

</div>
