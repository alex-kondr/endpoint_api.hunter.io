from pydantic import BaseModel


class DBModel(BaseModel):
    data: dict = {}


class DBModelUpdate(BaseModel):
    status: str = ""