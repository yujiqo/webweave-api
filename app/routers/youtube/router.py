import uuid
from fastapi.routing import APIRouter
from pydantic import BaseModel
from pytube import YouTube

from .utils import get_pytube_resolutions


router = APIRouter(
    prefix="/youtube",
    tags=["Media by link"]
)


class Link(BaseModel):
    url: str

@router.post("/info")
async def fetch_video_by_link(link: Link):
    yt = YouTube(link.url)

    data = {
        "id": uuid.uuid4(),
        "url": link.url,
        "thumbnail": yt.thumbnail_url,
        "title": yt.title,
        "duration_in_secs": yt.length,
        "resolutions": get_pytube_resolutions(yt.streams)
    }

    return data
