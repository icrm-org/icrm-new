import yaml
from datetime import datetime
from pathlib import Path

# Paths
DATA_FILE = Path("calendar/events.yaml")
OUTPUT_FILE = Path("calendar/view-yaml.html")

# Load events.yaml
with open(DATA_FILE, "r", encoding="utf-8") as f:
    events = yaml.safe_load(f)

# Filter: only keep events with end-date >= today
today = datetime.today().date()
upcoming = []
for ev in events:
    try:
        end = datetime.strptime(ev["end-date"], "%Y-%m-%d").date()
        if end >= today:
            upcoming.append(ev)
    except Exception:
        # If no valid end-date, keep the entry
        upcoming.append(ev)

# Sort by start-date
upcoming.sort(key=lambda e: e.get("start-date", ""))

# Generate HTML table rows
rows = []
for ev in upcoming:
    title = ev.get("title", "")
    url = ev.get("url", "")
    if url:
        title = f'<a href="{url}" target="_blank">{title}</a>'
    rows.append(
        f"<tr><td>{ev.get('start-date','')}</td>"
        f"<td>{ev.get('end-date','')}</td>"
        f"<td>{title}</td>"
        f"<td>{ev.get('description','')}</td></tr>"
    )

# Wrap in HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ICRM Calendar</title>
  <style>
    body {{ font-family: sans-serif; max-width: 900px; margin: auto; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
    th {{ background: #f0f0f0; }}
  </style>
</head>
<body>
  <h1>ICRM Calendar</h1>
  <p><a href="events.yaml">📄 Download the events.yaml file</a></p>
  <table>
    <thead>
      <tr><th>Start Date</th><th>End Date</th><th>Title</th><th>Description</th></tr>
    </thead>
    <tbody>
      {"".join(rows)}
    </tbody>
  </table>
</body>
</html>
"""

# Write output
OUTPUT_FILE.write_text(html, encoding="utf-8")
print(f"✅ Wrote {OUTPUT_FILE} with {len(upcoming)} events")
