"""
service-b source code
"""

import datetime
import functools

import fastapi
import pydantic

from package_b.package_b import package_b
from service_a import __version__

app = fastapi.FastAPI(version=__version__)


class RootResponse(pydantic.BaseModel):
    """
    Response model for the root path
    """

    service: str
    integer: int
    version: str = __version__
    timestamp: datetime.datetime = pydantic.Field(
        default_factory=functools.partial(
            datetime.datetime.now, tz=datetime.timezone.utc
        )
    )


@app.get("/")
def root() -> RootResponse:
    integer = package_b()
    return RootResponse(service="service-a", integer=integer)
