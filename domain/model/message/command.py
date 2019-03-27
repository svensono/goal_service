from typing import NamedTuple
from datetime import datetime


class SetGoalCommand(NamedTuple):
    name: str
    description: str
    due_date: datetime
