from pydantic import BaseModel


class ResponseCanAccess(BaseModel):
    canAccess: bool


class RequestUpdateFeatureAccess(BaseModel):
    featureName: str
    email: str
    enable: bool
