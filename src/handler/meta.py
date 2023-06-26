import inspect


class HandlerMeta(type):
    def __new__(cls, *args, **kwargs):
        call = getattr(cls, "__call__", None)
        signature = inspect.signature(call)

        print(signature)
