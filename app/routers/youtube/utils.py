from typing import List, Dict, Literal
from pytube import StreamQuery


Resolution = Literal["144p"] | Literal["240p"] \
        | Literal["360p"] | Literal["480p"] | Literal["720p"]


def get_pytube_resolutions(query: StreamQuery) -> List[Dict[Resolution, int]]:
    awailable_resolutions = []
    unique_resolutions = []

    for stream in query:
        if stream.resolution is None:
            continue

        unique_resolutions.append(stream.resolution)

    for resolution in set(unique_resolutions):
        stream = query.get_by_resolution(resolution)

        if stream is not None:
            awailable_resolutions.append({
                "resolution": stream.resolution,
                "size": round(stream.filesize_mb, 1)
            })

    return awailable_resolutions
