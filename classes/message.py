import dataclasses

from .chatUserInfo import ChatUserInfo
from .sticker import Sticker
from .purchasedGift import PurchasedGift
from .verificationAccessObject import VerificationAccessObject
from .videoCallMsgInfo import VideoCallMsgInfo
from .story import Story
from .experimentalGift import ExperimentalGift

@dataclasses.dataclass
class Message:
    uid: str
    date_modified: int
    from_person_id: str
    to_person_id: str
    mssg: str
    message_type: int
    read: bool
    album_id: str
    total_unread: int
    unread_from_user: int
    image_url: str
    frame_url: str
    can_delete: bool
    deleted: bool
    section_title: str = dataclasses.field(init = False, default = None)
    from_person_info: ChatUserInfo
    sticker: Sticker
    gift: PurchasedGift
    offensive: bool
    display_message: str
    verification_method: VerificationAccessObject
    date_created: int
    access_response_type: int
    is_liked: bool
    reply_to_uid: str
    first_response: bool
    video_call_msg_info: VideoCallMsgInfo
    is_masked: bool
    allow_report: bool
    emojis_count: int
    has_emoji_characters_only: bool
    user_substitute_id: str
    allow_reply: bool
    allow_edit_until_timestamp: int
    is_edited: bool
    allow_forwarding: bool
    clear_chat_version: int
    story: Story
    is_declined: bool
    has_lewd_photo: bool
    is_reported: bool
    allow_like: bool
    is_legacy: bool
    is_likely_offensive: bool
    game_id: str
    experimental_gift: ExperimentalGift