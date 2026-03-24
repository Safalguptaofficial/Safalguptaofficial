<!--
╔══════════════════════════════════════════════════════════════════════════════════╗
║  SAFAL_OS v3.21.0 — Kernel Build 2026.03.24                                    ║
║                                                                                  ║
║  This README is not a profile. It's a system.                                    ║
║  It auto-updates. It logs decisions. It tracks failures.                         ║
║  If you're reading the source, you already think like an engineer.               ║
║                                                                                  ║
║  Architecture: Modular monolith — each section is an independent kernel module.  ║
║  Rendering: Markdown → GitHub's parser → your screen. Zero JS. Pure signal.     ║
║                                                                                  ║
║  pgp: check commits. every one is signed.                                        ║
╚══════════════════════════════════════════════════════════════════════════════════╝
-->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=rect&height=1&color=0d1117"/>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=1&color=f6f8fa"/>
</picture>

```
 ____    _    _____ _    _          ___  ____
/ ___|  / \  |  ___/ \  | |        / _ \/ ___|
\___ \ / _ \ | |_ / _ \ | |       | | | \___ \
 ___) / ___ \|  _/ ___ \| |___    | |_| |___) |
|____/_/   \_\_|/_/   \_\_____|    \___/|____/

                            v3.21.0 — kernel build 2026.03.24
                            uptime: 21 years | pid: 1 | init: curiosity
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=16&duration=3500&pause=1200&color=8b949e&center=true&vCenter=true&multiline=false&repeat=true&width=700&height=30&lines=%24+cat+%2Fetc%2Fmotd+%E2%80%94+%22systems+thinker.+not+a+coder.+an+engineer.%22;%24+uname+-a+%E2%80%94+CSE+(IoT)+%40+VIT+Vellore+%E2%80%A2+Class+of+2027;%24+whoami+%E2%80%94+building+infrastructure+for+problems+that+matter)](https://git.io/typing-svg)

<br>

<a href="https://github.com/Safalguptaofficial">
  <img src="https://komarev.com/ghpvc/?username=Safalguptaofficial&style=flat-square&color=161b22&labelColor=161b22&label=pid.views" alt="Views"/>
</a>
&nbsp;
<a href="https://github.com/Safalguptaofficial?tab=followers">
  <img src="https://img.shields.io/github/followers/Safalguptaofficial?style=flat-square&color=161b22&labelColor=161b22&logo=github&logoColor=8b949e&label=pid.followers" alt="Followers"/>
</a>
&nbsp;
<img src="https://img.shields.io/badge/status-accepting__inbound-238636?style=flat-square&labelColor=161b22"/>

</div>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    MODULE 0: KERNEL IDENTITY                  -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.0 :: KERNEL — identity (click to collapse)</b></summary>
<br>

```
safal@os:~$ dmesg | grep identity

[    0.000001] kernel: loading identity module...
[    0.000002] name:       Safal Gupta
[    0.000003] host:       VIT Vellore — CSE (IoT) — 3rd Year
[    0.000004] arch:       systems engineering × quantitative reasoning × applied ML
[    0.000005] init:       not here to participate. here to outperform.
[    0.000006] kernel: identity module loaded. signal:noise ratio = high.
```

**I don't write code. I build systems that make code unnecessary.**

Three things define how I work:

| Principle | Implication |
|-----------|-------------|
| **Systems over scripts** | I model the problem before touching an editor. If I can't draw it on a whiteboard, I don't understand it yet. |
| **Proof of work > proof of talk** | Every claim below has a commit, a metric, or a failure log. No vanity. |
| **Compound learning** | I track what I learn, how fast I learn it, and where the gaps are. Then I attack the gaps. |

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                MODULE 1: PROCESS TABLE                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.1 :: PROCESS TABLE — what's running right now</b></summary>
<br>

```
safal@os:~$ ps aux --sort=-%cpu | head -12

USER     PID   %CPU  %MEM   STATE     STARTED      COMMAND
safal    001   94.2  high   RUNNING   2024-Q3      competitive-programming/daily-grind
safal    002   88.7  high   RUNNING   2025-Q1      quant-backtester/cpp-engine
safal    003   76.1  med    RUNNING   2025-Q4      ml-risk-scoring/pytorch-pipeline
safal    004   61.3  med    BUILDING  2026-Q1      iot-edge-inference/mqtt-pipeline
safal    005   42.0  low    RESEARCH  2026-Q1      systems-design/distributed-patterns
safal    006   28.5  low    QUEUED    2026-Q2      kernel-bypass-networking/dpdk-study
───────────────────────────────────────────────────────────────────────
load_avg: 3.8 3.2 2.9   | threads: always saturated | idle: not found
```

> **Process scheduling policy:** I don't multitask. I time-slice across high-priority processes using a modified EDF (Earliest Deadline First). One deep focus block per process, minimum 90 minutes, no context switches.

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--              MODULE 2: MEMORY MAP (SKILL ALLOCATION)          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.2 :: MEMORY MAP — skill allocation at runtime</b></summary>
<br>

<div align="center">

#### SEGMENT: core languages
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)
![JavaScript](https://img.shields.io/badge/JS-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

#### SEGMENT: ml / quantitative
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TF-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![sklearn](https://img.shields.io/badge/sklearn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

#### SEGMENT: systems / infrastructure
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white)
![RPi](https://img.shields.io/badge/RPi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=eclipsemosquitto&logoColor=white)

#### SEGMENT: web / tooling
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Node](https://img.shields.io/badge/Node-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/Mongo-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Neovim](https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=neovim&logoColor=white)

</div>

```
safal@os:~$ cat /proc/meminfo | grep -E "skill"

  REGION                 ALLOC    GROWTH_RATE    CONFIDENCE    NEXT MILESTONE
  ─────────────────────────────────────────────────────────────────────────────
  C++ / STL              ████████████████░░░░    +12%/mo      ship a lib
  Python / ML            ███████████████░░░░░    +10%/mo      deploy prod model
  DSA / Competitive      █████████████████░░░    +15%/mo      hit 2000 problems
  Systems Design         ████████████░░░░░░░░    +8%/mo       design a dist system
  IoT / Embedded         ██████████████░░░░░░    +6%/mo       edge ML inference
  Quant / Math           ███████████░░░░░░░░░    +14%/mo      backtest with alpha
  ─────────────────────────────────────────────────────────────────────────────
  total_allocated: [██████████████████████████████░░░░░░] 82% of waking hours
  page_faults: sometimes. that's where the growth is.
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--               MODULE 3: DECISION LOG                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.3 :: DECISION LOG — engineering tradeoffs I've actually made</b></summary>
<br>

> Most profiles show *what* someone built. This section shows *how* they think.

| Date | Decision | Options Considered | Chosen | Why |
|------|----------|-------------------|--------|-----|
| 2026-Q1 | **Backtester engine language** | Python (fast dev), Rust (safety), C++ (raw speed) | **C++** | Backtesting is CPU-bound with tight inner loops. Python was 200x too slow. Rust's borrow checker added friction for rapid prototyping at this stage. C++ gave me zero-cost abstractions + SIMD intrinsics for vectorized portfolio math. |
| 2025-Q4 | **ML serving framework** | Flask, Django, FastAPI | **FastAPI** | Async-native, auto-generates OpenAPI docs, Pydantic validation catches schema drift before production. For a risk scoring pipeline, type safety at the boundary matters more than framework maturity. |
| 2025-Q3 | **IoT protocol choice** | HTTP polling, WebSockets, MQTT | **MQTT** | 10k sensors → polling = O(n) server load. WebSockets = persistent connections = memory pressure. MQTT's pub/sub with QoS 1 + retained messages gave us decoupled, fault-tolerant ingestion at 1/10th the server cost. |
| 2025-Q2 | **Monorepo vs polyrepo** | Monorepo (Nx), polyrepo (separate repos) | **Polyrepo** | At my current team size (1), monorepo tooling overhead > benefit. Polyrepo lets me ship independently. I'll migrate when cross-project dependencies justify the coordination cost. |
| 2025-Q1 | **DSA practice platform** | LeetCode only, Codeforces only, both | **Both, time-sliced** | LeetCode for interview patterns + company tags. Codeforces for speed, pressure tolerance, and mathematical thinking. Different muscles. Train both. |

> **Meta-decision:** I keep this log because *"how you decide" is more important than "what you decide."* Bad decisions with good process self-correct. Good decisions with no process are luck.

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--             MODULE 4: FAILURE ANALYSIS LOG                    -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>&nbsp;mod.4 :: FAILURE LOG — postmortems that taught me more than success</b></summary>
<br>

> Engineers who don't publish failures are hiding the most valuable signal.

#### `INCIDENT-001` :: The Silent Data Corruption

```
severity:    HIGH
system:      IoT sensor pipeline
root cause:  unsigned integer overflow in temperature sensor ADC conversion
time to detect:  3 weeks (!)
time to fix:     2 hours

TIMELINE:
  [T+0]       Deployed sensor firmware with uint16_t for temperature delta
  [T+2d]      Dashboard showing "normal" — all values in range
  [T+3w]      Noticed 4% of readings cluster suspiciously at 65,534
  [T+3w+1h]   Root cause: negative deltas wrapping unsigned int → silent corruption
  [T+3w+2h]   Fix: switched to int32_t, added assertion: abs(delta) < MAX_SANE_DELTA

LESSON:  Type systems are documentation. If the type doesn't encode the constraint,
         the constraint doesn't exist. I now start every data pipeline with:
         "What values are IMPOSSIBLE? Encode that as a type."
```

#### `INCIDENT-002` :: The O(n²) That Hid in Production

```
severity:    MEDIUM
system:      Competitive programming practice tracker (personal tool)
root cause:  nested loop in "find similar problems" — O(n²) string matching
time to detect:  instant once n > 500
time to fix:     20 min (trie-based solution)

WHAT HAPPENED:
  Built a tool to tag & search solved problems by pattern.
  Worked fine for 200 problems. At 500+, search took 4 seconds.
  Profiled with perf: 89% time in strstr() inside a nested loop.

FIX:  Replaced with Aho-Corasick multi-pattern matching.
      Search went from 4.2s → 8ms. 525x speedup.

LESSON:  Always ask: "What happens when n grows 10x?"
         If the answer is "it gets 100x slower," you have O(n²).
         Big-O isn't academic — it's the difference between "works" and "works at scale."
```

#### `INCIDENT-003` :: The Premature Abstraction

```
severity:    LOW (but expensive in time)
system:      Quant backtester v1
root cause:  over-engineered plugin system before having 2 strategies
time wasted: ~40 hours on architecture astronautics

WHAT HAPPENED:
  Before writing a single strategy, I built:
  - Abstract StrategyBase class with 12 virtual methods
  - Plugin loader with dynamic registration
  - Config-driven strategy selection via YAML

  Then I wrote my first strategy. It needed 3 of the 12 methods.
  Second strategy needed different methods. Rewrote the interface.

LESSON:  "Make it work. Make it right. Make it fast." — in that order.
         I now follow the Rule of Three: no abstraction until three concrete cases
         prove the pattern exists. Premature abstraction is negative productivity.
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--             MODULE 5: MENTAL MODELS                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.5 :: MENTAL MODELS — the operating system behind the engineer</b></summary>
<br>

These aren't buzzwords. These are the actual thinking tools I apply daily:

```
safal@os:~$ cat /usr/share/mental-models/active.conf

MODEL                    APPLICATION IN MY WORK                           FREQUENCY
─────────────────────────────────────────────────────────────────────────────────────
First Principles         Decompose every "best practice" before adopting  daily
Inversion                "How would this system FAIL?" — design from     every design
                         the failure mode backward
Map vs Territory         My mental model != the system. Test assumptions  every debug
                         with data, not intuition
Opportunity Cost         Every hour on X is an hour NOT on Y. I maintain  weekly review
                         a priority queue, not a to-do list
Second-Order Effects     "If I optimize for latency, what breaks?"        every tradeoff
                         Most bugs live in 2nd-order consequences
Pareto (80/20)           20% of the codebase causes 80% of bugs. Profile  every refactor
                         before rewriting. Never optimize uniformly
Feedback Loops           Tight loops = fast learning. I push code in      daily
                         small increments with fast CI, not big PRs
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--            MODULE 6: LEARNING VELOCITY TRACKER                -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.6 :: LEARNING VELOCITY — not what I know, but how fast I'm acquiring</b></summary>
<br>

> Static skill lists are vanity metrics. **Rate of change** is the real signal.

```
safal@os:~$ sar -u --learning-rate 2025-01 2026-03

DOMAIN                  2025-Q1   2025-Q3   2026-Q1   Δ/quarter   TRAJECTORY
────────────────────────────────────────────────────────────────────────────────
DSA Problem Solving      ██░░░░    ████░░    ██████    +33%        📈 accelerating
C++ / Systems            ███░░░    █████░    ██████    +25%        📈 accelerating
ML Engineering           █░░░░░    ███░░░    █████░    +40%        📈 steep ramp
Quantitative Finance     ░░░░░░    ██░░░░    ████░░    +50%        📈 steep ramp
Systems Design           ██░░░░    ███░░░    ████░░    +20%        📈 steady
IoT / Embedded           ████░░    █████░    █████░    +8%         ➡️ plateau (refocus Q2)
────────────────────────────────────────────────────────────────────────────────
aggregate velocity: INCREASING — learning faster than I was learning last quarter
```

**Q1 2026 learning protocol:**
- **Input:** 2 technical papers/week, 1 system design case/week, 3+ DSA problems/day
- **Output:** 1 project shipped/month, decision log updated weekly
- **Feedback:** Every project has a written postmortem, win or fail

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--         MODULE 7: SYSTEM THINKING BOARD                       -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details>
<summary><b>&nbsp;mod.7 :: SYSTEM THINKING BOARD — how I approach hard problems</b></summary>
<br>

```
safal@os:~$ cat /var/log/system-thinking/approach.md

┌─────────────────────────────────────────────────────────────────────────────┐
│                     SAFAL'S PROBLEM DECOMPOSITION PROTOCOL                  │
│                                                                             │
│  PHASE 1: UNDERSTAND (don't touch code)                                     │
│  ├─ What is the actual problem? (not the symptom)                           │
│  ├─ Who are the users? What breaks their workflow?                          │
│  ├─ What are the constraints? (time, memory, latency, cost)                 │
│  └─ What's the simplest version that delivers 80% of the value?            │
│                                                                             │
│  PHASE 2: MODEL (whiteboard, not IDE)                                       │
│  ├─ Draw the data flow. Every arrow is a potential failure point.            │
│  ├─ Identify the invariants. What must ALWAYS be true?                      │
│  ├─ Find the bottleneck. Systems are only as fast as their slowest path.    │
│  └─ Ask: "What happens at 10x scale? 100x? Does the architecture hold?"    │
│                                                                             │
│  PHASE 3: BUILD (smallest possible increment)                               │
│  ├─ Write the test first. If I can't test it, I don't understand it.        │
│  ├─ Build the unhappy path first. Errors are more common than success.      │
│  ├─ Ship. Get feedback. The design will be wrong — learn where.             │
│  └─ Iterate with data, not opinions.                                        │
│                                                                             │
│  PHASE 4: VERIFY (measure, don't assume)                                    │
│  ├─ Profile before optimizing. Intuition is a hypothesis.                   │
│  ├─ Load test at 10x expected traffic. Prod will surprise you.              │
│  └─ Write the postmortem BEFORE shipping. What could go wrong?              │
│                                                                             │
│  APPLIED EXAMPLE:                                                           │
│  "Design a rate limiter for 50M users at 10M req/sec"                       │
│  → Token bucket > leaky bucket (burst tolerance)                            │
│  → Shard by user_id % N across 64 Redis nodes → O(1) per check             │
│  → Local cache handles 95% without network hop                              │
│  → Fail open under partition (Netflix philosophy)                           │
│  → First code written: the rejection path                                   │
│  → Last code written: the config layer                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--         MODULE 8: PROOF OF WORK                               -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.8 :: PROOF OF WORK — shipped, not planned</b></summary>
<br>

> Talk is O(1). Shipping is O(n). This section only contains things with commits.

| # | Project | Stack | What I Actually Built | Signal |
|---|---------|-------|-----------------------|--------|
| 01 | **IoT Sensor Pipeline** | `Python` `MQTT` `RPi` `InfluxDB` | End-to-end sensor data ingestion from 50+ devices, MQTT broker, time-series storage, anomaly detection dashboard. Handles 10k msgs/sec on a $35 Raspberry Pi. | Systems thinking at the edge |
| 02 | **Quant Backtester** | `C++17` `NumPy` `Pandas` | Vectorized portfolio simulation engine. Custom order book, slippage model, walk-forward optimization. Processes 10 years of tick data in <8 seconds. | Performance engineering |
| 03 | **ML Risk Scorer** | `PyTorch` `FastAPI` `Docker` | Binary classification model (AUC 0.87) for health telemetry risk scoring. FastAPI serving layer with <50ms p95 latency. Containerized, CI/CD ready. | Full-stack ML engineering |
| 04 | **DSA Pattern Engine** | `C++` `React` | Solved 800+ problems across LeetCode & Codeforces. Built a personal pattern-matching tool using Aho-Corasick to tag and retrieve problems by algorithmic pattern. | Meta-learning infrastructure |

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--         MODULE 9: CURRENTLY BREAKING / FIXING                 -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.9 :: CURRENTLY BREAKING / FIXING — live engineering journal</b></summary>
<br>

```
safal@os:~$ tail -f /var/log/engineering.log

[2026-03-24 19:23:52 IST] BREAKING: trying to implement lock-free queue in C++
                          atomic<> + memory_order_release is subtle
                          goal: understand acquire-release semantics by building, not reading

[2026-03-22 14:10:00 IST] FIXING:   backtester memory usage spikes during walk-forward
                          suspect: vector reallocation in inner loop
                          action: reserve() + profile with valgrind massif

[2026-03-20 09:30:00 IST] LEARNING: reading "Designing Data-Intensive Applications" ch.5-7
                          replication, partitioning, transactions
                          connecting theory → IoT pipeline architecture decisions

[2026-03-18 22:00:00 IST] SHIPPED:  risk scorer API containerized + deployed to staging
                          p95 latency: 47ms (target was <50ms) ✓
                          next: add model versioning with MLflow
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--               MODULE 10: KERNEL METRICS                       -->
<!-- ═══════════════════════════════════════════════════════════════ -->

## &nbsp;mod.10 :: KERNEL METRICS

<div align="center">

<a href="https://github.com/Safalguptaofficial">
  <img height="160em" src="https://github-readme-stats.vercel.app/api?username=Safalguptaofficial&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9&count_private=true&include_all_commits=true&rank_icon=percentile"/>
</a>
&nbsp;&nbsp;
<a href="https://github.com/Safalguptaofficial">
  <img height="160em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Safalguptaofficial&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=8&hide=jupyter%20notebook,html,css"/>
</a>

<br><br>

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
<!--              MODULE 11: IPC (INTER-PROCESS COMMUNICATION)     -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<details open>
<summary><b>&nbsp;mod.11 :: IPC — reach me</b></summary>
<br>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/safalguptaofficial)
&nbsp;&nbsp;
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/safabornn)
&nbsp;&nbsp;
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:safallovetocode@gmail.com)
&nbsp;&nbsp;
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/safalguptaofficial)
&nbsp;&nbsp;
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=flat-square&logo=codeforces&logoColor=white)](https://codeforces.com/profile/safalguptaofficial)

</div>

```
PROTOCOL     LATENCY     AVAILABILITY    USE CASE
──────────────────────────────────────────────────────────────────
LinkedIn     < 24h       async           professional, collabs, research
Twitter      < 12h       async           technical discussion, hot takes
Email        < 48h       async           formal, detailed proposals
GitHub       immediate   always          code speaks louder
──────────────────────────────────────────────────────────────────
accepting: research collaborations, competitive programming teams,
           quant projects, high-signal internships, interesting problems
rejecting: recruiters without context, "quick syncs", blockchain pitches
```

</details>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                   TROPHIES                                    -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

[![trophy](https://github-profile-trophy.vercel.app/?username=Safalguptaofficial&theme=darkhub&no-frame=true&no-bg=true&margin-w=4&rank=SECRET,SSS,SS,S,AAA,AA,A)](https://github.com/ryo-ma/github-profile-trophy)

</div>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                   CONTRIBUTION SNAKE                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake.svg"/>
  <img alt="Snake eating contributions" src="https://raw.githubusercontent.com/Safalguptaofficial/Safalguptaofficial/output/github-snake.svg"/>
</picture>

</div>

---

<div align="center">

```
safal@os:~$ cat /etc/motd

 ┌───────────────────────────────────────────────────────────────────┐
 │                                                                   │
 │  "The most important property of a program is whether it          │
 │   accomplishes the intention of its user."                        │
 │                                          — C.A.R. Hoare           │
 │                                                                   │
 │   This profile is a living system. It updates. It logs.           │
 │   It breaks. It recovers. Just like good software.                │
 │                                                                   │
 │   If you read this far, you think in systems too.                 │
 │   Let's build something.                                          │
 │                                                                   │
 │   — Safal Gupta, 2026                                             │
 │   pid 1 | signal: SIGCONT | status: always building               │
 │                                                                   │
 └───────────────────────────────────────────────────────────────────┘
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:58a6ff&height=80&section=footer&reversal=false" width="100%"/>

</div>

<!--
═══════════════════════════════════════════════════════════════
GITHUB ACTIONS FOR AUTO-UPDATING SECTIONS

FILE: .github/workflows/snake.yml
───────────────────────────────────────────
name: Generate Contribution Snake
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

FILE: .github/workflows/metrics.yml
───────────────────────────────────────────
name: Profile Metrics
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.METRICS_TOKEN }}
          user: Safalguptaofficial
          template: classic
          config_timezone: Asia/Kolkata
-->
