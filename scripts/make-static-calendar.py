import yaml
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "calendar" / "events.yaml"
OUTPUT_FILE = ROOT / "calendar" / "index.md"

def parse_iso(d):
    try:
        return date.fromisoformat(d)
    except Exception:
        return None

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing {DATA_FILE}")

    with DATA_FILE.open("r", encoding="utf-8") as f:
        events = yaml.safe_load(f) or []

    # Sort by start-date
    def sort_key(ev):
        sd = parse_iso(str(ev.get("start-date", "")).strip())
        return (sd is None, sd or date.max)
    events.sort(key=sort_key)

    # Build HTML table rows
    rows = []
    for ev in events:
        start = ev.get("start-date", "")
        end = ev.get("end-date", "")
        title = ev.get("title", "")
        url = (ev.get("url") or "").strip()
        if url:
            title = f'<a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>'
        desc = ev.get("description", "")
        rows.append(
            f"<tr><td>{start}</td><td>{end}</td><td>{title}</td><td>{desc}</td></tr>"
        )

    # Markdown + embedded HTML table
    md = f"""---
title: Calendar
layout: default
nav_order: 9
---

# Radionuclide Metrology Calendar


<table>
  <thead>
    <tr>
      <th>Start Date</th>
      <th>End Date</th>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {"".join(rows)}
  </tbody>
</table>
"""

    OUTPUT_FILE.write_text(md, encoding="utf-8")
    print(f"✅ Wrote {OUTPUT_FILE} with {len(events)} events.")

if __name__ == "__main__":
    main()
