import inspect
import logging
from typing import Callable, TypeVar, Type

from src.handler.meta import HandlerMeta
from src.serialization.serialiser.base import BaseSerializer

T = TypeVar("T")

HandlerCallable = Callable


class Handler(metaclass=HandlerMeta):
    __logger: logging.Logger
    __handler: HandlerCallable
    __serializer: BaseSerializer
    __in_type: Type
    __out_type: Type

    def __init__(self, serializer: BaseSerializer, handler: HandlerCallable):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__serializer = serializer

        signature = inspect.signature(handler)
        print(signature.parameters)
        print(signature.return_annotation)

    async def __call__(self, data: bytes):
        return \
            self.__serializer.serialize(await self.__handler(self.__serializer.deserialize(data, self.__in_type)))
