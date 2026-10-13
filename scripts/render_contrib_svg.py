#!/usr/bin/env python3
"""
Genera contrib-heatmap.svg a partir de los datos reales de contribuciones
de GitHub (GraphQL), con una animación de revelado celda a celda.

Requiere una variable de entorno GH_TOKEN con un Personal Access Token
(classic) con scope `read:user`. El GITHUB_TOKEN automático de Actions
no basta para leer contributionsCollection de forma fiable, así que
se usa un PAT guardado como secret.

Uso:
    GH_TOKEN=ghp_xxx GH_USERNAME=foxploit python3 render_contrib_svg.py
"""

import os
import sys
import requests

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"

QUERY = """
query($userName: String!) {
  user(login: $userName) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
            color
          }
        }
      }
    }
  }
}
"""

CELL_SIZE = 11
CELL_GAP = 3
BG_COLOR = "#0d1117"
TEXT_COLOR = "#c9d1d9"


def fetch_contributions(username: str, token: str) -> dict:
    headers = {"Authorization": f"bearer {token}"}
    resp = requests.post(
        GITHUB_GRAPHQL_URL,
        json={"query": QUERY, "variables": {"userName": username}},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "errors" in data:
        raise RuntimeError(f"GitHub GraphQL error: {data['errors']}")
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def build_svg(calendar: dict, username: str) -> str:
    weeks = calendar["weeks"]
    total = calendar["totalContributions"]

    num_weeks = len(weeks)
    width = num_weeks * (CELL_SIZE + CELL_GAP) + 40
    height = 7 * (CELL_SIZE + CELL_GAP) + 50

    cells = []
    delay_index = 0
    max_delay_index = num_weeks * 7

    for week_i, week in enumerate(weeks):
        for day in week["contributionDays"]:
            x = 20 + week_i * (CELL_SIZE + CELL_GAP)
            # day["date"] weekday is implicit in order (Sun..Sat per GitHub API)
            day_i = week["contributionDays"].index(day)
            y = 35 + day_i * (CELL_SIZE + CELL_GAP)
            color = day["color"]
            delay = round((delay_index / max_delay_index) * 2.2, 3)
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" '
                f'rx="2" ry="2" fill="{color}" class="cell" '
                f'style="animation-delay:{delay}s">'
                f"<title>{day['date']}: {day['contributionCount']} contributions</title>"
                f"</rect>"
            )
            delay_index += 1

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: {BG_COLOR}; }}
    .label {{ font: 600 13px 'Segoe UI', Ubuntu, Sans-Serif; fill: {TEXT_COLOR}; }}
    .cell {{
      opacity: 0;
      transform-origin: center;
      animation: reveal 0.4s ease-out forwards;
    }}
    @keyframes reveal {{
      0%   {{ opacity: 0; transform: scale(0.3); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}
  </style>
  <rect class="bg" x="0" y="0" width="{width}" height="{height}" rx="6" ry="6" />
  <text x="20" y="20" class="label">{username} · {total} contributions in the last year</text>
  {''.join(cells)}
</svg>'''
    return svg


def main():
    username = os.environ.get("GH_USERNAME")
    token = os.environ.get("GH_TOKEN")

    if not username or not token:
        print("Faltan GH_USERNAME o GH_TOKEN en el entorno.", file=sys.stderr)
        sys.exit(1)

    calendar = fetch_contributions(username, token)
    svg = build_svg(calendar, username)

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"contrib-heatmap.svg generado ({calendar['totalContributions']} contributions).")


if __name__ == "__main__":
    main()
