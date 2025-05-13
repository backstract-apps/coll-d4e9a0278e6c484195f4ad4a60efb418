from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: Any
    name: str
    contact_information: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_information: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int
    name: str
    contact_information: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: int
    name: str
    contact_information: str

    class Config:
        from_attributes = True

