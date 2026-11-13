"""Genera las tarjetas SVG del README en ./cards (junto a este script).

Uso: python gen_cards.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent / "cards"
OUT.mkdir(exist_ok=True)

MONO = "Fira Code, Consolas, monospace"
SANS = "Inter, Segoe UI, Helvetica, Arial, sans-serif"

PANEL = "#15151f"
TRACK = "#2a2a3a"
TEXT = "#e4e4e7"
MUTED = "#c4c4cc"
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
        out.append(f"<text x='28' y='{120 + i * 26}' font-family='{SANS}' font-size='16' fill='{sub}'>{escape(line)}</text>")
    if progress:
        done, total = progress
        bar_w = w - 56
        out.append(f"<rect x='28' y='{h - 40}' width='{bar_w}' height='8' rx='4' fill='{track}'/>")
        out.append(f"<rect x='28' y='{h - 40}' width='{bar_w * done / total:.1f}' height='8' rx='4' fill='{bar}'/>")
        out.append(f"<text x='28' y='{h - 16}' font-family='{MONO}' font-size='12' fill='{sub}'>{done}/{total}</text>")
    out.append("</svg>")
    return "\n".join(out)


TILES = [
    # Repos públicos (clicables en el README)
    ("gtx", dict(eyebrow="GitHub · público", title="GTX Trading API",
                 lines=["Revisión de seguridad de una API de trading"], accent=PURPLE)),
    ("writeups", dict(eyebrow="GitHub · público", title="Writeups",
                      lines=["PortSwigger · picoCTF · Spooky CTF", "HackTheBox · TryHackMe"], accent=PURPLE)),
    ("natas", dict(eyebrow="GitHub · público", title="Natas auto-solver",
                   lines=["Python: cookies, encoding,", "traversal y fuzzing"], accent=PURPLE)),
    ("tailscale", dict(eyebrow="PR · tailscale-android", title="Fix de DNS en Tailscale",
                       lines=["Corrige el DNS roto al cambiar de Wi-Fi", "Un usuario lo usa como referencia"], accent=BLUE)),

    # Proyectos privados (no clicables)
    ("pentest-auto", dict(eyebrow="En curso · privado", title="Scanner web autónomo",
                          lines=["Lanza escáneres de seguridad sin intervención", "Repositorio privado en desarrollo"], accent=YELLOW)),
    ("ctf-os", dict(eyebrow="Proyecto · privado", title="SO para CTF",
                    lines=["Arch + BlackArch · Hyprland · pwntools", "Cronómetro propio por fase de cada CTF"], accent=LILAC)),
    ("otros", dict(eyebrow="Homelab y universidad · privado", title="Otros proyectos", w=880, h=240,
                   lines=[
                       "Homelab: Proxmox, OPNsense, Frigate, Vaultwarden, Caddy · 10 sistemas",
                       "Casa automatizada: cámaras Tapo, persianas LocalTuya, IoT aislado por firewall",
                       "Inventario sobre Grocy: códigos de barras por ubicación y recetas con IA",
                       "Red corporativa: Cisco Packet Tracer, VLSM y zona DMZ",
                   ], accent=BLUE)),

    # Logros
    ("htb", dict(eyebrow="HTB · Skilled", title="Nivel 44",
                 lines=["22 máquinas completadas", "12 retos completados"], accent=LIME, solid=True)),
    ("academy", dict(eyebrow="HTB Academy", title="Pentesting web",
                     lines=["Ruta de pentesting de aplicaciones web"], accent=PURPLE, progress=(6, 20))),
    ("ejpt", dict(eyebrow="Siguiente", title="eJPT",
                  lines=["Certificación en preparación", "Objetivo: principios de 2027"], accent=BLUE, solid=True)),
]


def main():
    for name, kwargs in TILES:
        (OUT / f"{name}.svg").write_text(tile(**kwargs), encoding="utf-8")
    print(f"{len(TILES)} tarjetas escritas en {OUT}")


if __name__ == "__main__":
    main()
