from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cards"
OUT.mkdir(exist_ok=True)

MONO = "Fira Code, Consolas, monospace"
SANS = "Inter, Segoe UI, Helvetica, Arial, sans-serif"

PANEL = "#15151f"
TRACK = "#2a2a3a"
TEXT = "#e4e4e7"
MUTED = "#a1a1aa"
INK = "#0d0d14"
PURPLE = "#8b5cf6"
LILAC = "#a78bfa"
LIME = "#9fef00"
RED = "#ef4444"
BLUE = "#3b82f6"
YELLOW = "#facc15"


def tile(eyebrow, title, lines, accent=PURPLE, solid=False, progress=None, w=440, h=200):
    if solid:
        fg = INK if accent in (LIME, YELLOW) else "#ffffff"
        sub = fg
        bg = accent
        eyebrow_c = fg
        track = "#00000040"
        bar = fg
    else:
        fg = TEXT
        sub = MUTED
        bg = PANEL
        eyebrow_c = accent
        track = TRACK
        bar = accent

    out = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>",
        f"<rect width='{w}' height='{h}' rx='18' fill='{bg}'/>",
    ]
    if not solid:
        out.append(f"<rect width='6' height='{h}' rx='3' fill='{accent}'/>")
    out.append(f"<text x='28' y='46' font-family='{MONO}' font-size='13' letter-spacing='2' fill='{eyebrow_c}'>{escape(eyebrow.upper())}</text>")
    out.append(f"<text x='28' y='86' font-family='{SANS}' font-size='28' font-weight='700' fill='{fg}'>{escape(title)}</text>")
    for i, line in enumerate(lines):
        out.append(f"<text x='28' y='{120 + i * 24}' font-family='{SANS}' font-size='15' fill='{sub}'>{escape(line)}</text>")
    if progress:
        done, total = progress
        bar_w = w - 56
        out.append(f"<rect x='28' y='{h - 40}' width='{bar_w}' height='8' rx='4' fill='{track}'/>")
        out.append(f"<rect x='28' y='{h - 40}' width='{bar_w * done / total:.1f}' height='8' rx='4' fill='{bar}'/>")
        out.append(f"<text x='28' y='{h - 16}' font-family='{MONO}' font-size='12' fill='{sub}'>{done}/{total}</text>")
    out.append("</svg>")
    return "\n".join(out)


def label(text, w=880, h=80):
    return "\n".join([
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>",
        f"<defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='{PURPLE}'/><stop offset='1' stop-color='{LILAC}' stop-opacity='0'/></linearGradient></defs>",
        f"<rect width='{w}' height='{h}' rx='14' fill='{PANEL}'/>",
        f"<rect width='6' height='{h}' rx='3' fill='{PURPLE}'/>",
        f"<text x='30' y='{h // 2 + 10}' font-family='{MONO}' font-size='28' font-weight='700' fill='{TEXT}'><tspan fill='{PURPLE}'>$ </tspan>{escape(text)}</text>",
        f"<rect x='0' y='{h - 3}' width='{w}' height='3' fill='url(#g)'/>",
        "</svg>",
    ])


TILES = [
    ("gtx", dict(eyebrow="GitHub · público", title="GTX Trading API", lines=["Revisión de seguridad de una API", "Repo público"], accent=PURPLE)),
    ("writeups", dict(eyebrow="GitHub · público", title="Writeups", lines=["PortSwigger · CTFs · HackTheBox", "TryHackMe"], accent=PURPLE)),
    ("tailscale", dict(eyebrow="PR · tailscale-android", title="Fix de DNS en Tailscale", lines=["Corrige el DNS roto al cambiar de Wi-Fi", "Tomado como referencia en los foros"], accent=RED)),
    ("natas", dict(eyebrow="GitHub · público", title="Natas auto-solver", lines=["Python: cookies, encoding,", "traversal y fuzzing"], accent=PURPLE)),
    ("pentest-auto", dict(eyebrow="Próximamente en GitHub", title="Scanner web autónomo", lines=["Escáneres lanzados sin intervención", "En curso"], accent=YELLOW)),
    ("ctf-os", dict(eyebrow="Próximamente en GitHub", title="SO para CTF", lines=["Arch + BlackArch · Hyprland", "Cronómetro por fase de cada CTF"], accent=PURPLE)),
    ("web-propia", dict(eyebrow="Próximamente en GitHub", title="Web propia", lines=["Portfolio y writeups en un mismo sitio"], accent=PURPLE, solid=True)),
    ("arsenal", dict(eyebrow="Próximamente en GitHub", title="Arsenal", lines=["MITM proxy · scanner XSS/SQLi", "OSINT wordlist · privesc checker", "payload encoder · reverse shell manager"], accent=LILAC)),
    ("homelab", dict(eyebrow="Homelab · privado", title="Proxmox + 10 sistemas", lines=["OPNsense · Frigate · Vaultwarden", "Caddy · AdGuard Home · Beszel"], accent=BLUE)),
    ("home-assistant", dict(eyebrow="Homelab · privado", title="Casa automatizada", lines=["Cámaras Tapo · persianas LocalTuya", "Dispositivos IoT aislados por firewall"], accent=PURPLE)),
    ("grocy", dict(eyebrow="Homelab · privado", title="Inventario sobre Grocy", lines=["Códigos de barras por ubicación", "Recetas con IA en Home Assistant"], accent=YELLOW)),
    ("ucs-network", dict(eyebrow="Universidad · privado", title="Red corporativa", lines=["Cisco Packet Tracer · VLSM", "Zona DMZ con web, FTP, DNS y correo"], accent=BLUE)),
    ("ml", dict(eyebrow="Universidad · privado", title="Predicción de retrasos", lines=["Clasificación binaria en Python", "Dataset público de e-commerce"], accent=PURPLE)),
    ("htb", dict(eyebrow="HTB · Skilled", title="Nivel 44", lines=["22 máquinas completadas", "12 retos completados"], accent=LIME, solid=True)),
    ("academy", dict(eyebrow="HTB Academy", title="Pentesting web", lines=["Ruta de pentesting de aplicaciones web"], accent=PURPLE, progress=(6, 20))),
    ("ejpt", dict(eyebrow="Siguiente", title="eJPT", lines=["Certificación en preparación", "Objetivo: principios de 2027"], accent=BLUE, solid=True)),
    ("no-hago", dict(eyebrow="No hago", title="Sin autorización, nada", lines=["No pentesteo sin permiso por escrito", "No desarrollo malware"], accent=RED)),
    ("gh-activity", dict(eyebrow="GitHub", title="198 contribuciones", lines=["Último año"], accent=LILAC)),
]

LABELS = [
    ("label-publicos", "ls ./github-publico"),
    ("label-proximamente", "cat ./proximamente-en-github"),
    ("label-homelab", "cat ./homelab-y-uni"),
    ("label-logros", "cat ./logros"),
    ("label-stats", "stats"),
    ("label-footer", "exit 0 · rooted by foxploit"),
]


def main():
    for name, kwargs in TILES:
        (OUT / f"{name}.svg").write_text(tile(**kwargs), encoding="utf-8")
    for name, text in LABELS:
        (OUT / f"{name}.svg").write_text(label(text), encoding="utf-8")


if __name__ == "__main__":
    main()
