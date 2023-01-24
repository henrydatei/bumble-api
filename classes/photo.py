import dataclasses

from .photoSize import PhotoSize
from .point import Point

@dataclasses.dataclass
class Photo:
    id: str
    preview_url: str
    large_url: str
    preview_url_expiration_ts: int
    large_url_expiration_ts: int
    large_photo_size: PhotoSize = dataclasses.field(init = False, default = None)
    face_top_left: Point = dataclasses.field(init = False, default = None)
    face_bottom_right: Point = dataclasses.field(init = False, default = None)
    can_set_as_profile_photo: bool = dataclasses.field(init = False, default = None)
    is_pending_moderation: bool = dataclasses.field(init = False, default = None)