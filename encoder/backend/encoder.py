import urllib.parse
from functools import cache
from typing import List, Dict, Iterable

from pydantic import BaseModel

from classes import Encoder
from decorators import get_instances


class EncodingBody(BaseModel):
    type: str
    message: str

    def __hash__(self):
        return f"{self.type}||{self.message}".__hash__()


_encoders: List[Encoder] = get_instances(Encoder)
_named_encodes: Dict[str, Encoder] = {encoder.name: encoder for encoder in _encoders}
_string_encoder: Encoder = _named_encodes.get("string")


def get_all_encoder_names() -> Iterable[str]:
    return list(_named_encodes.keys())


def get_encoder_from_name(name: str) -> Encoder:
    return _named_encodes[name]


@cache
def encode(body: EncodingBody):
    message = body.message
    if body.type != "string":
        message = get_encoder_from_name(body.type).decode(message)

    encoded = {enc.name: enc.encode(message) for enc in _encoders}
    print(f"encoded {body.message} from type {body.type}")
    return {"messages": encoded}


