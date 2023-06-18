from typing import Dict, Tuple
from dotenv import dotenv_values
from fastapi import APIRouter

from .routers import youtube


def read_env() -> Dict[str, str | None]:
    env = dotenv_values()

    return env

def setup_app(env: Dict[str, str | None]) -> None:
    pass


routers: Tuple[APIRouter] = (youtube.router, )
