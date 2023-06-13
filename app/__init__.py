from fastapi import FastAPI
from .server import Server


def server(_=None) -> FastAPI:
    app = Server().server

    return app
