import datetime as dt
from pydantic import BaseModel


class Payload(BaseModel):
    data: str = ""


class Resource(BaseModel):
    timestamp: dt.datetime
    message: str