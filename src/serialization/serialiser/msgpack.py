from typing import Type

import ormsgpack

from src.serialization.adaptix.retort import retort
from src.serialization.serialiser.base import BaseSerializer, T


class MsgpackSerializer(BaseSerializer):
    def serialize(self, value: T) -> bytes:
        return ormsgpack.packb(retort.dump(value))

    def deserialize(self, data: bytes, data_type: Type) -> T:
        return retort.load(ormsgpack.unpackb(data), data_type)
