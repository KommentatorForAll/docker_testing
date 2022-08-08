import abc
import base64
import urllib.parse

from decorators import notice_me


class Encoder(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def encode(self, plain_text: str) -> str:
        pass

    @abc.abstractmethod
    def decode(self, code: str) -> str:
        pass


@notice_me
class StringEncoder(Encoder):
    def __init__(self):
        super().__init__("string")

    def encode(self, plain_text: str) -> str:
        return plain_text

    def decode(self, code: str) -> str:
        return code


@notice_me
class HexEncoder(Encoder):
    def __init__(self):
        super().__init__("hex")

    def encode(self, plain_text: str) -> str:
        return bytes(plain_text, "utf8").hex(" ")

    def decode(self, code: str) -> str:
        return bytes.fromhex(code.replace(" ", "")).decode("utf8")


@notice_me
class Base64Encoder(Encoder):
    def __init__(self):
        super().__init__("base64")

    def encode(self, plain_text: str) -> str:
        return base64.b64encode(bytes(plain_text, "utf8")).decode("utf8")

    def decode(self, code: str) -> str:
        return base64.b64decode(bytes(code, "utf8")).decode("utf8")


@notice_me
class HTMLEscapedEncoder(Encoder):
    def __init__(self):
        super().__init__("html escaped")

    def encode(self, plain_text: str) -> str:
        return urllib.parse.quote(plain_text)

    def decode(self, code: str) -> str:
        return urllib.parse.unquote(code)


@notice_me
class BinaryEncoder(Encoder):
    def __init__(self):
        super().__init__("binary")

    def encode(self, plain_text: str) -> str:
        return ' '.join(format(ord(x), 'b') for x in plain_text)

    def decode(self, code: str) -> str:
        return ''.join([chr(int(i, 2)) for i in code.split(" ")])
