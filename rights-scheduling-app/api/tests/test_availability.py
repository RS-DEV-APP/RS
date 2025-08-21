from app.services.availability import _overlap

def test_overlap_true():
    assert _overlap("2025-01-01T00:00:00","2025-01-02T00:00:00",
                    "2025-01-01T12:00:00","2025-01-03T00:00:00")

def test_overlap_false():
    assert not _overlap("2025-01-01T00:00:00","2025-01-01T10:00:00",
                        "2025-01-01T10:00:00","2025-01-01T12:00:00")
