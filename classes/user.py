import dataclasses
from typing import List

from .photo import Photo
from .location import Location
from .album import Album
from .musicService import MusicService
from .profileField import ProfileField
from .profileSummary import ProfileSummary
from .experience import Experience
from .goalProgress import GoalProgress

@dataclasses.dataclass
class User:
    user_id: str
    projection: List[int]
    client_source: int = dataclasses.field(init = False, default = None)
    access_level: int
    name: str
    age: int
    gender: int
    verification_status: int = dataclasses.field(init = False, default = None)
    photo_count: int = dataclasses.field(init = False, default = None)
    profile_photo: Photo = dataclasses.field(init = False, default = None)
    albums: List[Album] = dataclasses.field(init = False, default = None)
    music_services: List[MusicService] = dataclasses.field(init = False, default = None)
    profile_fields: List[ProfileField] = dataclasses.field(init = False, default = None)
    profile_summary: ProfileSummary = dataclasses.field(init = False, default = None)
    distance_long: str = dataclasses.field(init = False, default = None)
    distance_short: str = dataclasses.field(init = False, default = None)
    is_inapp_promo_partner: bool = dataclasses.field(init = False, default = None)
    game_mode: int = dataclasses.field(init = False, default = None)
    hometown: Location = dataclasses.field(init = False, default = None)
    residence: Location = dataclasses.field(init = False, default = None)
    is_in_private_mode: bool = dataclasses.field(init = False, default = None)
    their_vote: int = dataclasses.field(init = False, default = None)
    match_message: str = dataclasses.field(init = False, default = None)
    allow_chat_from_match_screen: bool = dataclasses.field(init = False, default = None)
    allow_crush: bool = dataclasses.field(init = False, default = None)
    type: int = dataclasses.field(init = False, default = None)
    jobs: List[Experience] = dataclasses.field(init = False, default = None)
    educations: List[Experience] = dataclasses.field(init = False, default = None)
    is_deleted: bool = dataclasses.field(init = False, default = None)
    is_extended_match: bool = dataclasses.field(init = False, default = None)
    online_status: int = dataclasses.field(init = False, default = None)
    is_match: bool = dataclasses.field(init = False, default = None)
    match_mode: int = dataclasses.field(init = False, default = None)
    is_crush: bool = dataclasses.field(init = False, default = None)
    their_vote_mode: int = dataclasses.field(init = False, default = None)
    reply_time_left: GoalProgress = dataclasses.field(init = False, default = None)
    unread_messages_count: int = dataclasses.field(init = False, default = None)
    display_message: str = dataclasses.field(init = False, default = None)
    is_locked: bool = dataclasses.field(init = False, default = None)
    connection_status_indicator: int = dataclasses.field(init = False, default = None)