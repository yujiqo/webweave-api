from fastapi import FastAPI

from .server import Server
from .config import ROUTERS


def server(_=None) -> FastAPI:
    app = Server()

    app.register_routers(ROUTERS)

    return app.server
