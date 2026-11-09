#!/usr/bin/env python3
# generates assets/boot.svg and assets/neofetch.svg
# usage: python3 scripts/gen_svgs.py assets
# no deps. SMIL + css keyframes only, because github serves svgs through <img> (no js).

import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"
MONO = "'JetBrains Mono','Fira Code',Consolas,'DejaVu Sans Mono','Courier New',monospace"
GRAY, WHITE, DIM = "#B8B8C0", "#F2F2F2", "#5C5C6A"
CORAL, TEAL, AMBER = "#FF6B6B", "#4ECDC4", "#FFD866"
BG = "#0A0A0F"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def show_at(t):
    return f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'


# ---------------------------------------------------------------- boot screen
def boot():
    W, H, X, LH, FS = 1000, 400, 34, 25, 15
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="BIOS-style boot screen for Smit Patne, full-stack and GenAI engineer">
<style>
  .cur {{ animation: c 1s steps(1) infinite; }} @keyframes c {{ 50% {{ opacity: 0 }} }}
  text {{ font-family: {MONO}; font-size: {FS}px; white-space: pre; }}
</style>
<defs><pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1" fill="#000" opacity=".35"/></pattern></defs>
<rect width="{W}" height="{H}" rx="6" fill="{BG}"/>''']

    y = 40
    out.append(f'<text x="{X}" y="{y}" fill="{WHITE}" font-weight="700">SMIT BIOS v2.0   Full-Stack / GenAI build</text>')
    out.append(f'<text x="{W-X}" y="{y}" fill="{DIM}" text-anchor="end">Mumbai, IN</text>')
    y += LH
    out.append(f'<text x="{X}" y="{y}" fill="{DIM}">(C) Smit Patne. All bugs reserved.</text>')
    y += LH * 1.6

    out.append(f'<text x="{X}" y="{y}" fill="{GRAY}">CPU         : 1x human, chai-cooled</text>')
    y += LH
    # memory counter: a few frames swapped with discrete visibility
    out.append(f'<text x="{X}" y="{y}" fill="{GRAY}">Memory Test : </text>')
    frames = ["0002048K", "0004096K", "0006144K", "0008192K", "0010240K", "0012288K", "0014336K", "0016384K OK"]
    step, t0 = 0.12, 0.3
    mx = X + 14 * FS * 0.6
    for i, f in enumerate(frames):
        a, b = t0 + i * step, t0 + (i + 1) * step
        last = i == len(frames) - 1
        col = WHITE if last else GRAY
        anim = (f'<set attributeName="opacity" to="1" begin="{a:.2f}s"/>' +
                ("" if last else f'<set attributeName="opacity" to="0" begin="{b:.2f}s"/>'))
        out.append(f'<text x="{mx:.1f}" y="{y}" fill="{col}" opacity="0">{f}{anim}</text>')
    t = t0 + len(frames) * step + 0.25
    y += LH * 1.6

    probes = [
        ("Detecting languages ", "python, typescript, sql, java"),
        ("Detecting frameworks", "fastapi, react, spring boot, langchain"),
        ("Detecting storage   ", "postgres + pgvector, redis, kafka"),
        ("Detecting GPU       ", "kaggle free tier (borrowed)"),
        ("Checking containers ", "all up. one is restarting. it's fine."),
    ]
    for label, val in probes:
        out.append(f'<text x="{X}" y="{y}" fill="{GRAY}" opacity="0">{label} ....... '
                   f'<tspan fill="{WHITE}">{esc(val)}</tspan>{show_at(t)}</text>')
        t += 0.32
        y += LH
    y += LH * 0.6
    out.append(f'<text x="{X}" y="{y}" fill="{GRAY}" opacity="0">Booting from /home/smit ...{show_at(t)}</text>')
    t += 0.6
    y += LH * 1.6
    out.append(f'<text x="{X}" y="{y}" opacity="0"><tspan fill="{TEAL}">smit@mumbai</tspan><tspan fill="{GRAY}">:</tspan>'
               f'<tspan fill="{CORAL}">~</tspan><tspan fill="{GRAY}">$ </tspan>{show_at(t)}</text>')
    cx = X + len("smit@mumbai:~$ ") * FS * 0.6
    out.append(f'<g opacity="0">{show_at(t)}<rect class="cur" x="{cx:.1f}" y="{y-FS+2}" width="{FS*0.6:.1f}" height="{FS+2}" fill="{GRAY}"/></g>')

    out.append(f'<text x="{X}" y="{H-18}" fill="{DIM}">Press DEL to enter SETUP, F12 to scroll down</text>')
    out.append(f'<rect width="{W}" height="{H}" rx="6" fill="url(#scan)"/></svg>')
    return "\n".join(out)


# ---------------------------------------------------------------- neofetch
AVATAR = [
    "....HHHHHHHH....",
    "...HHHHHHHHHH...",
    "..HHHHHHHHHHHH..",
    ".PHHSSSSSSSSHHP.",
    ".PHSSSSSSSSSSHP.",
    ".PSGGGGSSGGGGSP.",
    ".PSGEWGSSGEWGSP.",
    ".PSGGGGSSGGGGSP.",
    "..SSSSSSSSSSSS..",
    "..SSSSMMMMSSSS..",
    "...SSSSSSSSSS...",
    "....SSSSSSSS....",
    "...CCCCSSCCCC...",
    "..CCCCCCCCCCCC..",
    ".CCCcCCTTCCcCCC.",
    ".CCCcCCTTCCcCCC.",
]
PAL = {"H": "#22160F", "S": "#C68642", "G": TEAL, "E": "#111", "W": "#fff", "M": "#6B2E22",
       "P": AMBER, "C": CORAL, "c": "#C94848", "T": "#fff"}

INFO = [
    ("OS", "Homo sapiens (Mumbai build)"),
    ("Uptime", "2+ years in production"),
    ("Role", "Full-Stack Engineer, GenAI"),
    ("Kernel", "python 3 / typescript"),
    ("Packages", "fastapi, react, langchain, pgvector, docker"),
    ("Projects", "dataforge (active), pharma-lms (active)"),
    ("Debugger", "print(), then the real debugger"),
    ("Theme", "dark. obviously."),
    ("Status", "open to genai / full-stack / ml roles"),
]


def neofetch():
    W, H, FS, LH = 1000, 330, 15, 24
    px = 15
    ax, ay = 40, 42
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="neofetch-style summary for Smit Patne">
<style>
  text {{ font-family: {MONO}; font-size: {FS}px; white-space: pre; }}
  .blink {{ animation: be 5s steps(1) infinite; }} @keyframes be {{ 0%,95% {{ opacity: 1 }} 96%,99% {{ opacity: 0 }} }}
</style>
<rect width="{W}" height="{H}" rx="6" fill="{BG}"/>''']
    eyes = []
    for r, row in enumerate(AVATAR):
        assert len(row) == 16
        for c, ch in enumerate(row):
            if ch == ".":
                continue
            rect = f'<rect x="{ax+c*px}" y="{ay+r*px}" width="{px}" height="{px}" fill="{PAL[ch]}"/>'
            (eyes if ch in "EW" else out).append(rect)
    out.append(f'<g class="blink">{"".join(eyes)}</g>')

    tx, y = ax + 16 * px + 50, 52
    out.append(f'<text x="{tx}" y="{y}"><tspan fill="{TEAL}" font-weight="700">smit</tspan><tspan fill="{GRAY}">@</tspan>'
               f'<tspan fill="{TEAL}" font-weight="700">mumbai</tspan></text>')
    y += LH * 0.8
    out.append(f'<text x="{tx}" y="{y}" fill="{DIM}">-----------</text>')
    y += LH
    for k, v in INFO:
        out.append(f'<text x="{tx}" y="{y}"><tspan fill="{CORAL}" font-weight="700">{k}</tspan>'
                   f'<tspan fill="{GRAY}">: {esc(v)}</tspan></text>')
        y += LH
    y += 6
    cols = ["#1a1a1a", CORAL, "#7EE787", AMBER, "#58A6FF", "#D2A8FF", TEAL, "#E6E6E6"]
    for i, c in enumerate(cols):
        out.append(f'<rect x="{tx + i*30}" y="{y}" width="30" height="16" fill="{c}"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in [("boot.svg", boot), ("neofetch.svg", neofetch)]:
        with open(os.path.join(OUT, name), "w") as f:
            f.write(fn())
        print("wrote", os.path.join(OUT, name))
