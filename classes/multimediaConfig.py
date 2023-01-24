import dataclasses
from typing import List

from .multimediaVisibility import MultimediaVisibility

@dataclasses.dataclass
class MultimediaConfig:
    visiblity: List[MultimediaVisibility] = dataclasses.field(init = False, default = None)
    format: int
    min_length: int = dataclasses.field(init = False, default = None)
    max_length: int = dataclasses.field(init = False, default = None)