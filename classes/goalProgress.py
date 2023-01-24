import dataclasses

@dataclasses.dataclass
class GoalProgress:
    goal: int
    progress: int
    start_ts: int