import dataclasses
import logging

from src.app import ZeroMessenger


@dataclasses.dataclass
class SimpleMessage:
    data: str


async def handle(message: SimpleMessage):
    logging.error(message.data)


def main():
    messenger = ZeroMessenger(name="test")

    messenger.register_handler("base", handle)
    messenger.run()


if __name__ == "__main__":
    main()
