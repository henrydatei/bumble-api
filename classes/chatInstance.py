import dataclasses

@dataclasses.dataclass
class ChatInstance:
    uid: str
    date_modified: int
    counter: int
    their_icon_id: str
    my_icon_id: str
    other_account_deleted: bool
    is_new: bool
    feels_like_chatting: bool
    my_unread_messages: int
    their_unread_messages: int
    chat_icebreaker_ask: str
    chat_suggestion_prompt: str
    is_match: bool
    open_stickers: bool
