import dataclasses
from typing import List

from .applicationFeature import ApplicationFeature
from .multimediaConfig import MultimediaConfig

@dataclasses.dataclass
class MultimediaSettings:
    feature: ApplicationFeature
    multimedia_config: MultimediaConfig
    multimedia_configs: List[MultimediaConfig]