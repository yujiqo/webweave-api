import uuid
import json
from typing import List, Literal, TypedDict
from pytube import YouTube, StreamQuery
from redis import Redis


class Resolution(TypedDict):
    resolution: Literal["144p"] | Literal["240p"] \
        | Literal["360p"] | Literal["480p"] | Literal["720p"]
    size: float

class VideoInfo(TypedDict):
    id: str
    url: str
    thumbnail: str
    title: str
    duration_in_secs: int
    resolutions: List[Resolution]


def get_pytube_resolutions(query: StreamQuery) -> List[Resolution]:
    awailable_resolutions = []
    unique_resolutions = set()

    for stream in query:
        if stream.resolution is None:
            continue

        unique_resolutions.add(stream.resolution)

    for resolution in set(unique_resolutions):
        stream = query.get_by_resolution(resolution)

        if stream is not None:
            awailable_resolutions.append({
                "resolution": stream.resolution,
                "size": round(stream.filesize_mb, 1)
            })

    return awailable_resolutions

def get_parsed_video_info(connection: Redis, url: str) -> VideoInfo:
    yt = YouTube(url)

    data: VideoInfo = {
        "id": str(uuid.uuid4()),
        "url": url,
        "thumbnail": yt.thumbnail_url,
        "title": yt.title,
        "duration_in_secs": yt.length,
        "resolutions": get_pytube_resolutions(yt.streams)
    }

    connection.set(data["id"], json.dumps(data))

    return data
