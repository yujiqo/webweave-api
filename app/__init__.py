from fastapi import FastAPI

from .server import Server
from .config import setup_app


def server(_=None) -> FastAPI:
    app = Server()

    setup_app(env=app.env)

    return app.server
