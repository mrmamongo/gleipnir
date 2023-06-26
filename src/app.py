from collections.abc import MutableSequence
from typing import Type, MutableMapping

from src.handler.handler import Handler, HandlerCallable
from src.log.log import setup_logging
from src.proxy_process.proxy import Proxy
from src.serialization.serialiser.base import BaseSerializer
from src.serialization.serialiser.json import JsonSerializer


class ZeroMessenger:
    __serializer: Type[BaseSerializer]
    __proxy_process: Proxy
    __handlers: MutableMapping[str, Handler]

    def __init__(
        self,
        name: str,
        frontend_url: str = "tcp://*:5570",
        backend_url: str = "ipc://backend",
        serializer: Type[BaseSerializer] = JsonSerializer,
    ) -> None:
        setup_logging()
        self.__proxy_process = Proxy(backend_url, frontend_url)
        self.__serializer = serializer
        self.__handlers = {}

    def run(self) -> None:
        # self.__proxy_process.run()
        self.__run()

    def __run(self) -> None:
        pass

    def register_handler(self, route_name: str, handler: HandlerCallable) -> None:
        self.__handlers[route_name] = Handler(serializer=self.__serializer(), handler=handler)
