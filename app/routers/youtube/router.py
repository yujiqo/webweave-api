from fastapi.routing import APIRouter
from pydantic import BaseModel

from ...connection import connection
from .utils import get_parsed_video_info


router = APIRouter(
    prefix="/youtube",
    tags=["Media by link"]
)


class Link(BaseModel):
    url: str

@router.post("/info")
async def fetch_video_by_link(link: Link):
    return get_parsed_video_info(connection, link.url)
