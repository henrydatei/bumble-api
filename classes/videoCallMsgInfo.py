import dataclasses

@dataclasses.dataclass
class VideoCallMsgInfo:
    foo: str  = dataclasses.field(default = "bar", init = False)