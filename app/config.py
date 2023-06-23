from typing import Tuple
from fastapi import APIRouter

from .routers import youtube


ROUTERS: Tuple[APIRouter] = (youtube.router, )
