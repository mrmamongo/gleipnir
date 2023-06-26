from typing import Type

import orjson as orjson

from src.serialization.adaptix.retort import retort
from src.serialization.serialiser.base import BaseSerializer, T


class JsonSerializer(BaseSerializer):
    def serialize(self, value: T) -> bytes:
        return orjson.dumps(retort.dump(value))

    def deserialize(self, data: bytes, data_type: Type) -> T:
        return retort.load(orjson.loads(data), T)
