import dataclasses
from typing import List

from .chatInstance import ChatInstance
from .chatSettings import ChatSettings
from .message import Message
from .user import User

@dataclasses.dataclass
class Chat:
    chat_instance: ChatInstance
    is_chat_available: bool
    user_originated_message: bool
    title: str
    chat_settings: ChatSettings
    chat_messages: List[Message]
    chat_user: User
    encrypted_im_writing: str
    encrypted_comet_url: str
    read_messages_timestamp: int
    is_not_interested: bool

    def printChat(self):
        print("=== Chat with " + self.chat_user.name + " ===")
        for message in self.chat_messages:
            if self.chat_user.user_id == message.from_person_id:
                print(self.chat_user.name + ": " + message.mssg)
            else:
                print("Me: " + message.mssg)