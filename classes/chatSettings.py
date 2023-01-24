import dataclasses
from typing import List

from .multimediaSettings import MultimediaSettings
from .inputSettings import InputSettings

@dataclasses.dataclass
class ChatSettings:
    chat_instance_id: str
    multimedia_settings: MultimediaSettings
    feature_order: List[int]
    input_settings: InputSettings
    allow_disabling_private_detector: bool
    allow_questions_game: bool