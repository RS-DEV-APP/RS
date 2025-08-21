from datetime import datetime
from typing import List

def _overlap(a_start: str, a_end: str, b_start: str, b_end: str) -> bool:
    a1, a2 = datetime.fromisoformat(a_start), datetime.fromisoformat(a_end)
    b1, b2 = datetime.fromisoformat(b_start), datetime.fromisoformat(b_end)
    latest_start = max(a1, b1)
    earliest_end = min(a2, b2)
    return latest_start < earliest_end

def validate_against_rights(schedule_start: str, schedule_end: str, right_row) -> List[str]:
    issues: List[str] = []
    if not _overlap(schedule_start, schedule_end, right_row.start, right_row.end):
        issues.append("Outside licensed window")
    # add territory/platform/language checks as needed
    return issues
