import dataclasses
from typing import List

from .applicationFeature import ApplicationFeature

@dataclasses.dataclass
class InputSettings:
    input_features: List[ApplicationFeature]