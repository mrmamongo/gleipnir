from multiprocessing import Process
import zmq


class Proxy(Process):
    frontend_url: str
    backend_url: str

    def __init__(self, frontend_url: str, backend_url: str) -> None:
        super().__init__()
        self.frontend_url = frontend_url
        self.backend_url = backend_url

    def run(self) -> None:
        context = zmq.Context()
        frontend = context.socket(zmq.ROUTER)
        frontend.bind(self.frontend_url)

        backend = context.socket(zmq.DEALER)
        backend.bind(self.backend_url)

        zmq.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()
