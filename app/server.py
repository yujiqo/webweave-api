from typing import Self, Optional, Any, Dict
from fastapi import FastAPI

from .config import read_env


class Server:
    __instanse: Optional[Self] = None
    _server: FastAPI
    _env: Dict[str, str | None]

    def __new__(cls) -> Self:
        if cls.__instanse is None:
            cls.__instanse = super(Server, cls).__new__(cls)

        return cls.__instanse

    def __init__(self) -> None:
        self._server = FastAPI()
        self._env = read_env()

    def __getattr__(self, name: str) -> Any:
        return self.__dict__[f"_{name}"]
