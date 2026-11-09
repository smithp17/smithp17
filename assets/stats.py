#!/usr/bin/env python3
"""Draws neon-themed GitHub stat cards for a profile README.

Runs inside GitHub Actions (uses the built-in GITHUB_TOKEN), no extra packages.
  python3 scripts/stats.py <username> <out_dir>
  python3 scripts/stats.py --mock <out_dir>      # sample data, for local testing
Writes: overview.svg, activity.svg, languages.svg
"""
import json
import os
import random
import sys
import urllib.request
from datetime import date, timedelta

CY, VI, PK, GR, OR = "#22D3EE", "#A78BFA", "#F472B6", "#34D399", "#FB923C"
TX, MU, LINE = "#E2E8F0", "#94A3B8", "#334155"
FONT = "'Inter','Segoe UI',system-ui,-apple-system,sans-serif"
MONO = "'JetBrains Mono','Fira Code',Consolas,monospace"
LANG_COLORS = [CY, VI, PK, GR, OR, "#60A5FA", "#FACC15", "#F87171"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    pullRequests { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""


# ------------------------------------------------------------------ data
def fetch(login):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if "errors" in body:
        raise SystemExit(f"GraphQL error: {body['errors']}")
    return body["data"]["user"]


def mock():
    random.seed(4)
    start = date.today() - timedelta(days=364)
    weeks, d = [], start
    while d <= date.today():
        wk = []
        for _ in range(7):
            if d > date.today():
                break
            burst = 3 if 120 < (d - start).days < 170 else 1
            wk.append({"date": d.isoformat(), "contributionCount": max(0, int(random.gauss(2, 3) * burst))})
            d += timedelta(days=1)
        weeks.append({"contributionDays": wk})
    langs = [("Python", 900), ("TypeScript", 520), ("JavaScript", 300), ("C#", 180), ("HTML", 90), ("CSS", 60), ("Go", 40)]
    return {
        "followers": {"totalCount": 42},
        "pullRequests": {"totalCount": 31},
        "repositories": {"totalCount": 38, "nodes": [
            {"stargazerCount": 3, "languages": {"edges": [{"size": s * 1000, "node": {"name": n}} for n, s in langs]}}]},
        "contributionsCollection": {"totalCommitContributions": 640, "restrictedContributionsCount": 120,
                                    "contributionCalendar": {"totalContributions": 812, "weeks": weeks}},
    }


def summarise(u):
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    # streaks (today with 0 doesn't break the current streak yet)
    cur = 0
    for i, d in enumerate(reversed(days)):
        if d["contributionCount"] > 0:
            cur += 1
        elif i == 0:
            continue
        else:
            break
    best = run = 0
    for d in days:
        run = run + 1 if d["contributionCount"] > 0 else 0
        best = max(best, run)
    langs = {}
    for r in u["repositories"]["nodes"]:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    stars = sum(r["stargazerCount"] for r in u["repositories"]["nodes"])
    return {
        "total": cal["totalContributions"],
        "commits": u["contributionsCollection"]["totalCommitContributions"]
                   + u["contributionsCollection"]["restrictedContributionsCount"],
        "repos": u["repositories"]["totalCount"],
        "prs": u["pullRequests"]["totalCount"],
        "stars": stars,
        "cur": cur,
        "best": best,
        "days": days,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


# ------------------------------------------------------------------ svg helpers
def head(w, h, label, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">
<style>
 .in{{animation:in .8s cubic-bezier(.16,1,.3,1) both}} @keyframes in{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
 .pulse{{animation:p 1.8s ease-in-out infinite}} @keyframes p{{50%{{opacity:.3}}}}
</style>
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0F172A"/><stop offset="1" stop-color="#1E1B4B"/></linearGradient>
 <filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 {extra_defs}
</defs>'''


def panel(x, y, w, h, title=None, sub=None):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="url(#bg)"/>'
         f'<rect x="{x+.75}" y="{y+.75}" width="{w-1.5}" height="{h-1.5}" rx="17.5" fill="none" stroke="{LINE}" stroke-opacity=".8" stroke-width="1.5"/>')
    if title:
        s += f'<text x="{x+26}" y="{y+40}" font-family="{FONT}" font-size="17" font-weight="700" fill="{TX}">{title}</text>'
    if sub:
        s += f'<text x="{x+w-26}" y="{y+40}" font-family="{MONO}" font-size="11.5" fill="{MU}" text-anchor="end">{sub}</text>'
    return s


def fmt(n):
    return f"{n/1000:.1f}k" if n >= 10000 else f"{n:,}"


# ------------------------------------------------------------------ cards
def overview(s):
    W, H = 1000, 150
    tiles = [("Contributions", s["total"], "last 12 months", CY),
             ("Current streak", s["cur"], f"best: {s['best']} days", PK),
             ("Commits", s["commits"], "last 12 months", VI),
             ("Repositories", s["repos"], f"{s['prs']} pull requests", GR)]
    tw, gap = 230, 20
    o = [head(W, H, "GitHub overview")]
    for i, (lab, val, sub, c) in enumerate(tiles):
        x = i * (tw + gap) + 10
        o.append(f'<g class="in" style="animation-delay:{i*.1:.1f}s">{panel(x, 5, tw, H-10)}')
        o.append(f'<circle class="pulse" cx="{x+28}" cy="38" r="4.5" fill="{c}" filter="url(#glow)"/>')
        o.append(f'<text x="{x+42}" y="43" font-family="{FONT}" font-size="13" font-weight="600" fill="{MU}">{lab}</text>')
        o.append(f'<text x="{x+24}" y="96" font-family="{FONT}" font-size="40" font-weight="800" fill="{TX}">{fmt(val)}'
                 f'{"<tspan font-size=\"16\" font-weight=\"600\" fill=\"" + MU + "\"> days</tspan>" if "streak" in lab else ""}</text>')
        o.append(f'<text x="{x+24}" y="122" font-family="{MONO}" font-size="11.5" fill="{c}">{sub}</text></g>')
    o.append("</svg>")
    return "\n".join(o)


def activity(s):
    W, H = 1000, 300
    days = s["days"]
    # weekly totals give a smoother, more readable curve than 365 daily spikes
    full = len(days) - len(days) % 7  # drop the unfinished current week
    days = days[len(days) - full:]
    weeks = [sum(d["contributionCount"] for d in days[i:i+7]) for i in range(0, full, 7)]
    labels = [days[i]["date"] for i in range(0, full, 7)]
    px0, px1, py0, py1 = 70, W - 40, 80, H - 50
    mx = max(max(weeks), 1)
    n = len(weeks)
    pts = [(px0 + (px1 - px0) * i / (n - 1), py1 - (py1 - py0) * v / mx) for i, v in enumerate(weeks)]

    def smooth(p):
        d = f"M{p[0][0]:.1f},{p[0][1]:.1f}"
        for i in range(1, len(p)):
            x0, y0 = p[i-1]; x1, y1 = p[i]; cx = (x0 + x1) / 2
            d += f" C{cx:.1f},{y0:.1f} {cx:.1f},{y1:.1f} {x1:.1f},{y1:.1f}"
        return d
    line = smooth(pts)
    area = line + f" L{px1},{py1} L{px0},{py1} Z"
    defs = f'''<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset=".55" stop-color="{VI}"/><stop offset="1" stop-color="{PK}"/></linearGradient>
 <linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{VI}" stop-opacity=".45"/><stop offset="1" stop-color="{CY}" stop-opacity="0"/></linearGradient>
 <clipPath id="rev"><rect x="0" y="0" width="0" height="{H}"><animate attributeName="width" from="0" to="{W}" dur="1.8s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect></clipPath>'''
    o = [head(W, H, "Contribution activity, last 12 months", defs), panel(5, 5, W-10, H-10, "Contribution activity", "weekly · last 12 months")]
    for k in range(5):  # grid
        y = py1 - (py1 - py0) * k / 4
        o.append(f'<line x1="{px0}" y1="{y:.1f}" x2="{px1}" y2="{y:.1f}" stroke="{LINE}" stroke-opacity=".5" stroke-dasharray="3 5"/>')
        o.append(f'<text x="{px0-12}" y="{y+4:.1f}" font-family="{MONO}" font-size="10.5" fill="{MU}" text-anchor="end">{round(mx*k/4)}</text>')
    seen = set()
    for i, lab in enumerate(labels):
        m = lab[:7]
        if m not in seen and i % 4 == 0:
            seen.add(m)
            mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(lab[5:7]) - 1]
            o.append(f'<text x="{pts[i][0]:.1f}" y="{py1+24}" font-family="{MONO}" font-size="10.5" fill="{MU}" text-anchor="middle">{mon}</text>')
    o.append(f'<g clip-path="url(#rev)"><path d="{area}" fill="url(#ar)"/>'
             f'<path d="{line}" fill="none" stroke="url(#ln)" stroke-width="3" stroke-linecap="round" filter="url(#glow)"/></g>')
    pk = max(range(n), key=lambda i: weeks[i])
    x, y = pts[pk]
    o.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="1.6s" fill="freeze"/>'
             f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{PK}" filter="url(#glow)"/>'
             f'<rect x="{x-46:.1f}" y="{y-38:.1f}" width="92" height="24" rx="12" fill="#0B1020" stroke="{PK}" stroke-opacity=".6"/>'
             f'<text x="{x:.1f}" y="{y-22:.1f}" font-family="{MONO}" font-size="11" fill="{TX}" text-anchor="middle">peak · {weeks[pk]}</text></g>')
    lx, ly = pts[-1]
    o.append(f'<circle class="pulse" cx="{lx:.1f}" cy="{ly:.1f}" r="4" fill="{CY}" filter="url(#glow)"/>')
    o.append("</svg>")
    return "\n".join(o)


def languages(s):
    W, H = 1000, 210
    top = s["langs"][:7]
    other = sum(v for _, v in s["langs"][7:])
    if other:
        top.append(("Other", other))
    tot = sum(v for _, v in top) or 1
    o = [head(W, H, "Most used languages"), panel(5, 5, W-10, H-10, "Languages", "by code size across repos")]
    bx, by, bw, bh = 31, 66, W - 72, 14
    o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="7" fill="#1E293B"/>')
    o.append(f'<clipPath id="bar"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="7"/></clipPath><g clip-path="url(#bar)">')
    x = bx
    for i, (name, v) in enumerate(top):
        w = bw * v / tot
        c = LANG_COLORS[i % len(LANG_COLORS)]
        o.append(f'<rect x="{x:.1f}" y="{by}" width="0" height="{bh}" fill="{c}">'
                 f'<animate attributeName="width" from="0" to="{max(w-2,0):.1f}" dur=".9s" begin="{.15+i*.08:.2f}s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect>')
        x += w
    o.append("</g>")
    cols = 4
    for i, (name, v) in enumerate(top):
        c = LANG_COLORS[i % len(LANG_COLORS)]
        cx = bx + (i % cols) * (bw / cols)
        cy = 122 + (i // cols) * 38
        o.append(f'<g class="in" style="animation-delay:{.3+i*.06:.2f}s"><circle cx="{cx+6}" cy="{cy-4}" r="6" fill="{c}"/>'
                 f'<text x="{cx+20}" y="{cy}" font-family="{FONT}" font-size="14" font-weight="600" fill="{TX}">{name}</text>'
                 f'<text x="{cx+bw/cols-40:.0f}" y="{cy}" font-family="{MONO}" font-size="12" fill="{MU}" text-anchor="end">{100*v/tot:.1f}%</text></g>')
    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    if sys.argv[1] == "--mock":
        user, out = mock(), sys.argv[2]
    else:
        user, out = fetch(sys.argv[1]), sys.argv[2]
    s = summarise(user)
    os.makedirs(out, exist_ok=True)
    for name, fn in [("overview.svg", overview), ("activity.svg", activity), ("languages.svg", languages)]:
        with open(os.path.join(out, name), "w") as f:
            f.write(fn(s))
        print("wrote", name)
