from ..db import SessionLocal, init_db
from ..models.title import Title
from ..models.episode import Episode
from ..models.channel import Channel
from ..models.right import Right

def run():
    init_db()
    db = SessionLocal()
    # Titles
    t1 = Title(type="SERIES", name="Cooking Stars", production_year=2024)
    t2 = Title(type="MOVIE", name="Deep Space", production_year=2023)
    db.add_all([t1, t2])
    db.commit()
    db.refresh(t1); db.refresh(t2)

    # Episodes
    eps = [Episode(title_id=t1.id, season_number=1, episode_number=i, duration=1800) for i in range(1,6)]
    db.add_all(eps)

    # Channel
    ch = Channel(name="Channel One", timezone="Europe/Berlin", country="DE")
    db.add(ch)

    # Rights for t1
    r1 = Right(contract_id=1, title_id=t1.id, right_type="EXHIBITION",
               territories="DE,AT,CH", languages="de,en", platforms="LINEAR",
               start="2025-08-01T00:00:00", end="2025-12-31T23:59:59",
               exclusivity="NON-EXCLUSIVE")
    db.add(r1)
    db.commit()
    db.close()
    print("Seed done.")

if __name__ == "__main__":
    run()
