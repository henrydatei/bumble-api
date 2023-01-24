import dataclasses
from typing import List
import inspect

from .photo import Photo
from .promoBlock import PromoBlock

@dataclasses.dataclass
class Album:
    uid: str
    name: str
    owner_id: str
    access_type: int = dataclasses.field(init = False, default = None)
    accessable: bool
    adult: bool
    requires_moderation: bool = dataclasses.field(init = False, default = None)
    count_of_photos: int
    instruction: str = dataclasses.field(init = False, default = None)
    is_upload_forbidden: bool = dataclasses.field(init = False, default = None)
    photos: List[Photo] = dataclasses.field(init = False, default = None)
    album_type: int
    game_mode: int = dataclasses.field(init = False, default = None)
    caption: str = dataclasses.field(init = False, default = None)
    access_level: int = dataclasses.field(init = False, default = None)
    external_provider: int = dataclasses.field(init = False, default = None)
    album_blocker: PromoBlock = dataclasses.field(init = False, default = None)