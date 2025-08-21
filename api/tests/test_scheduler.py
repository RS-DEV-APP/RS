from app.services.scheduler import suggest_day_grid

def test_suggest_day_grid_length():
    eps = [{"content_ref":"episode:1","duration":1200,"channel_id":1},
           {"content_ref":"episode:2","duration":1800,"channel_id":1}]
    grid = suggest_day_grid(eps, "2025-09-01")
    assert len(grid) == 2
    assert grid[0]["status"] == "AI_SUGGESTED"
