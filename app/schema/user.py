from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class ResponseUser(UserBase):
    id: int

    class Config:
        orm_mode = True
