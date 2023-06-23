from typing import Self, Optional, Any, Tuple
from fastapi import FastAPI
from fastapi.routing import APIRouter


class Server:
    __instance: Optional[Self] = None
    _server: FastAPI

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super(Server, cls).__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        self._server = FastAPI()

    def __getattr__(self, name: str) -> Any:
        return self.__dict__[f"_{name}"]

    def register_routers(self, routers: Tuple[APIRouter]) -> None:
        for router in routers:
            self._server.include_router(router)
