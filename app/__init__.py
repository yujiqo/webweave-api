from fastapi import FastAPI

from .server import Server
from .config import setup_app, routers


def server(_=None) -> FastAPI:
    app = Server()

    setup_app(env=app.env)
    app.register_routers(routers)

    return app.server
