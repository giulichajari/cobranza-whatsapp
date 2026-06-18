from fastapi import APIRouter, Depends, Request

from src.app.auth.dependencies import get_current_user
from src.app.middleware.rate_limit import limiter

router = APIRouter(
    prefix="/configuracion",
    tags=["Configuracion"]
)


@router.get("/")
@limiter.limit("30/minute")
def obtener_configuracion(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    pass


@router.put("/")
@limiter.limit("10/minute")
def actualizar_configuracion(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    pass