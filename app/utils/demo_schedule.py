from ..db import SessionLocal, init_db
from ..models.episode import Episode
from ..models.schedule import ScheduleItem
from ..services.scheduler import suggest_day_grid

def run():
    init_db()
    db = SessionLocal()
    eps = db.query(Episode).limit(5).all()
    episodes = [{"content_ref": f"episode:{e.id}", "duration": e.duration, "channel_id": 1} for e in eps]
    grid = suggest_day_grid(episodes, "2025-09-01")
    for row in grid:
        item = ScheduleItem(channel_id=row["channel_id"], start=row["start"], end=row["end"],
                            content_ref=row["content_ref"], status=row["status"])
        db.add(item)
    db.commit()
    print("Demo schedule created for Channel One on 2025-09-01.")

if __name__ == "__main__":
    run()
