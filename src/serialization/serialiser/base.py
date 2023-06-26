from typing import TypeVar, Protocol, Type

T = TypeVar("T")


class BaseSerializer(Protocol):
    def serialize(self, value: T) -> bytes:
        pass

    def deserialize(self, data: bytes, data_type: Type) -> T:
        pass
