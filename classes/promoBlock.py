import dataclasses
from typing import List

from .callToAction import CallToAction

@dataclasses.dataclass
class PromoBlock:
    mssg: str = dataclasses.field(init = False, default = None)
    promo_block_type: int
    promo_block_position: int
    buttons = List[CallToAction]
    context: int
    stats_variation_id: int = dataclasses.field(init = False, default = None)