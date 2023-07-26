from pydantic import BaseModel


class GroupResponse(BaseModel):
    id: int
    name: str
    description: str


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
