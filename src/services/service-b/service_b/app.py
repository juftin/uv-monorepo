"""
service-b source code
"""

import datetime
import functools

import fastapi
import pydantic

from service_b import __version__

app = fastapi.FastAPI(version=__version__)


class RootResponse(pydantic.BaseModel):
    """
    Response model for the root path
    """

    service: str
    version: str = __version__
    timestamp: datetime.datetime = pydantic.Field(
        default_factory=functools.partial(
            datetime.datetime.now, tz=datetime.timezone.utc
        )
    )


@app.get("/")
def root() -> RootResponse:
    return RootResponse(service="service-b")
