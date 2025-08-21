from datetime import datetime, timedelta
from typing import List, Dict

def suggest_day_grid(episodes: List[Dict], day: str, tz: str = "Europe/Berlin") -> List[Dict]:
    # naive example: schedule consecutively starting 18:00 local
    start = datetime.fromisoformat(day + "T18:00:00")
    grid = []
    for ep in episodes:
        end = start + timedelta(seconds=ep.get("duration", 1800))
        grid.append({**ep, "start": start.isoformat(), "end": end.isoformat(), "status": "AI_SUGGESTED"})
        start = end
    return grid
