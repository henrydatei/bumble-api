import dataclasses
from typing import List

from .externalProvider import ExternalProvider
from .musicArtist import MusicArtist

@dataclasses.dataclass
class MusicService:
    status: int
    external_provider: ExternalProvider
    status_comment: str = dataclasses.field(init = False, default = None)
    top_artists: List[MusicArtist] = dataclasses.field(init = False, default = None)