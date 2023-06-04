from pydantic import BaseModel


class FeatureBase(BaseModel):
    name: str


class FeatureCreate(FeatureBase):
    pass


class ResponseFeature(FeatureBase):
    id: int

    class Config:
        orm_mode = True
