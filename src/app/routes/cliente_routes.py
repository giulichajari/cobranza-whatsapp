from fastapi import APIRouter, Depends, Request

from src.app.auth.dependencies import get_current_user
from src.app.controllers.cliente_controller import ClienteController
from src.app.middleware.rate_limit import limiter
from src.app.schemas.client_schema import (
    ClienteCreate,
    ClienteResponse
)

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get(
    "/",
    response_model=list[ClienteResponse]
)
@limiter.limit("60/minute")
def listar_clientes(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    return ClienteController.listar()


@router.get(
    "/{cliente_id}",
    response_model=ClienteResponse
)
@limiter.limit("60/minute")
def obtener_cliente(
    request: Request,
    cliente_id: int,
    current_user: dict = Depends(get_current_user)
):
    return ClienteController.obtener(cliente_id)


@router.post(
    "/",
    response_model=ClienteResponse,
    status_code=201
)
@limiter.limit("20/minute")
def crear_cliente(
    request: Request,
    cliente: ClienteCreate,
    current_user: dict = Depends(get_current_user)
):
    return ClienteController.crear(cliente)


@router.put(
    "/{cliente_id}",
    response_model=ClienteResponse
)
@limiter.limit("20/minute")
def actualizar_cliente(
    request: Request,
    cliente_id: int,
    cliente: ClienteCreate,
    current_user: dict = Depends(get_current_user)
):
    return ClienteController.actualizar(
        cliente_id,
        cliente
    )


@router.delete("/{cliente_id}")
@limiter.limit("10/minute")
def eliminar_cliente(
    request: Request,
    cliente_id: int,
    current_user: dict = Depends(get_current_user)
):
    return ClienteController.eliminar(cliente_id)