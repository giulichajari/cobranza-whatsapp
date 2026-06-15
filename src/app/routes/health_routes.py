from fastapi import APIRouter
from app.controllers.health_controller import HealthController

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("")
def health_check():
    return HealthController.check()