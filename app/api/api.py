from fastapi import APIRouter

from app.api import custom, feature, user

api_router = APIRouter()
api_router.include_router(custom.router, tags=["Requirement"])
api_router.include_router(user.router, prefix="/admin", tags=["user"])
api_router.include_router(feature.router, prefix="/admin", tags=["feature"])
