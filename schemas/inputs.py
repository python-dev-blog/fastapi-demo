from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str
    description: str


class GroupCreate(GroupBase):
    pass