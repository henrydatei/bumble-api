import dataclasses

from .user import User

@dataclasses.dataclass
class SearchResult:
    has_user_voted: bool
    user: User