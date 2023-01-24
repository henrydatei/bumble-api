import dataclasses

@dataclasses.dataclass
class ChatUserInfo:
    foo: str  = dataclasses.field(default = "bar", init = False)