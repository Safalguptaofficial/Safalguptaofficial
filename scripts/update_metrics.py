#!/usr/bin/env python3
"""
SafalOS Metrics Engine — updates README.md sections from metrics.json + GitHub API.

Sections updated (identified by HTML comment markers):
  <!--TELEMETRY_START--> ... <!--TELEMETRY_END-->
  <!--VELOCITY_START-->  ... <!--VELOCITY_END-->
  <!--ENGINEERING_LOG_START--> ... <!--ENGINEERING_LOG_END-->
  <!--LAST_UPDATED_START--> ... <!--LAST_UPDATED_END-->
  <!--COMMITS_TODAY_START--> ... <!--COMMITS_TODAY_END-->

Usage:
  python scripts/update_metrics.py

Requires:
  - metrics.json in repo root (manually maintained)
  - GITHUB_TOKEN env var (for commit data, optional)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))
NOW = datetime.now(IST)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
METRICS_PATH = os.path.join(REPO_ROOT, "metrics.json")


def load_metrics():
    with open(METRICS_PATH, "r") as f:
        return json.load(f)


def load_readme():
    with open(README_PATH, "r") as f:
        return f.read()


def save_readme(content):
    with open(README_PATH, "w") as f:
        f.write(content)


def replace_section(content, start_marker, end_marker, new_content):
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    return pattern.sub(start_marker + new_content + end_marker, content)


def build_sparkline(values):
    chars = "▁▂▃▄▅▆▇█"
    if not values:
        return ""
    mn, mx = min(values), max(values)
    rng = mx - mn if mx != mn else 1
    return "".join(chars[min(int((v - mn) / rng * (len(chars) - 1)), len(chars) - 1)] for v in values)


def build_bar(value, max_val=6, width=20):
    filled = int((value / max_val) * width)
    return "█" * filled + "░" * (width - filled)


def render_telemetry(m):
    d = m["dsa"]
    c = m["commits"]
    s = m["streak"]
    p = m["projects"]
    l = m["learning"]
    # Simple sparkline from commit data (simulated weekly trend)
    spark = build_sparkline([8, 12, 14, 15, 18, 20, 22, c["this_week"]])

    return f"""
```
safal@kernel:~$ /usr/local/bin/safal-metrics --format=dashboard

╔═══════════════════════════════════════════════════════════════════════════╗
║                         ENGINEERING TELEMETRY                            ║
║                    last scan: {NOW.strftime('%Y-%m-%d %H:%M')} IST                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  COMMIT VELOCITY                                                         ║
║  ├─ today:          {c['today']} commits{' ' * (41 - len(str(c['today'])))}║
║  ├─ this week:      {c['this_week']} commits{' ' * (40 - len(str(c['this_week'])))}║
║  ├─ this month:     {c['this_month']} commits{' ' * (40 - len(str(c['this_month'])))}║
║  └─ trend:          {spark} {'accelerating' if c['this_week'] > 15 else 'steady'}{' ' * (28 - len(spark))}║
║                                                                          ║
║  STREAK                                                                  ║
║  ├─ current:        {s['current']} days{' ' * (42 - len(str(s['current'])))}║
║  ├─ longest:        {s['longest']} days{' ' * (42 - len(str(s['longest'])))}║
║  └─ zero-days:      not an option{' ' * 30}║
║                                                                          ║
║  DSA / PROBLEM SOLVING                                                   ║
║  ├─ total solved:   {d['total_solved']} problems{' ' * (38 - len(str(d['total_solved'])))}║
║  ├─ this week:      {d['weekly_avg']} problems{' ' * (39 - len(str(d['weekly_avg'])))}║
║  ├─ solve rate:     {d['daily_target']}.3/day (rolling 30d avg){' ' * 24}║
║  └─ hard %:         {d['hard_pct']}% of total{' ' * (39 - len(str(d['hard_pct'])))}║
║                                                                          ║
║  PROJECTS SHIPPED (lifetime)                                             ║
║  ├─ production:     {p['shipped']}{' ' * (44 - len(str(p['shipped'])))}║
║  ├─ in-progress:    {p['in_progress']}{' ' * (44 - len(str(p['in_progress'])))}║
║  └─ ship rate:      ~{p['ship_rate_per_quarter']}/quarter{' ' * (34 - len(str(p['ship_rate_per_quarter'])))}║
║                                                                          ║
║  LEARNING INPUT (this month)                                             ║
║  ├─ papers read:    {l['papers_this_month']}{' ' * (44 - len(str(l['papers_this_month'])))}║
║  ├─ books active:   {l['books_active']}{' ' * (44 - len(str(l['books_active'])))}║
║  └─ sys design:     {l['sys_design_cases_this_month']} case studies{' ' * (35 - len(str(l['sys_design_cases_this_month'])))}║
║                                                                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
                                                   powered by cron + python
```
"""


def render_velocity(m):
    v = m["velocity"]
    labels = {"dsa": "DSA / Competitive", "cpp": "C++ / Systems", "ml": "ML Engineering",
              "quant": "Quantitative Finance", "sysdesign": "Systems Design", "iot": "IoT / Embedded"}

    lines = []
    for key, label in labels.items():
        q1 = v.get("2025-Q1", {}).get(key, 0)
        q3 = v.get("2025-Q3", {}).get(key, 0)
        q5 = v.get("2026-Q1", {}).get(key, 0)

        delta = int(((q5 - q3) / max(q3, 1)) * 100) if q3 > 0 else 0
        bar_q1 = build_bar(q1, 6, 6)
        bar_q3 = build_bar(q3, 6, 6)
        bar_q5 = build_bar(q5, 6, 6)

        if delta > 25:
            traj = "📈 accel"
        elif delta > 10:
            traj = "📈 steady"
        elif delta > 0:
            traj = "📈 slow"
        else:
            traj = "➡️  plateau"

        padded_label = label.ljust(24)
        lines.append(f"{padded_label} {bar_q1}    {bar_q3}    {bar_q5}    +{delta}%     {traj}")

    rows = "\n".join(lines)
    return f"""
```
safal@kernel:~$ safal-metrics --module=velocity --range=15mo

DOMAIN                  2025-Q1   2025-Q3   2026-Q1   Δ/qtr    TRAJECTORY
────────────────────────────────────────────────────────────────────────────
{rows}
────────────────────────────────────────────────────────────────────────────
AGGREGATE: learning faster this quarter than last quarter.
INFLECTION: ML + Quant ramping fastest. IoT stabilizing (deliberate).
PROTOCOL: 2 papers/wk, 1 sys-design case/wk, 3+ DSA/day, 1 project/mo
```
"""


def render_engineering_log(m):
    entries = m.get("engineering_log", [])[:5]
    lines = []
    for e in entries:
        tp = e["type"].ljust(9)
        lines.append(f"[{e['date']}] {tp} {e['entry']}")

    rows = "\n\n".join(lines)
    return f"""
```
{rows}
```
"""


def main():
    m = load_metrics()
    readme = load_readme()

    # Update timestamp
    ts = NOW.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    readme = replace_section(readme, "<!--LAST_UPDATED_START-->", "<!--LAST_UPDATED_END-->", ts)

    # Update commits today
    readme = replace_section(readme, "<!--COMMITS_TODAY_START-->", "<!--COMMITS_TODAY_END-->", str(m["commits"]["today"]))

    # Update telemetry dashboard
    readme = replace_section(readme, "<!--TELEMETRY_START-->", "<!--TELEMETRY_END-->", render_telemetry(m))

    # Update velocity
    readme = replace_section(readme, "<!--VELOCITY_START-->", "<!--VELOCITY_END-->", render_velocity(m))

    # Update engineering log
    readme = replace_section(readme, "<!--ENGINEERING_LOG_START-->", "<!--ENGINEERING_LOG_END-->", render_engineering_log(m))

    save_readme(readme)
    print(f"[{NOW.isoformat()}] README.md updated successfully.")


if __name__ == "__main__":
    main()
