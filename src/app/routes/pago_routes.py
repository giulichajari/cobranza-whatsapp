from fastapi import APIRouter, Depends, Request

from src.app.auth.dependencies import get_current_user
from src.app.controllers.pago_controller import PagoController
from src.app.middleware.rate_limit import limiter
from src.app.schemas.pago_schema import (
    PagoCreate,
    PagoResponse,
    PagoUpdate
)

router = APIRouter(
    prefix="/pagos",
    tags=["Pagos"],
    dependencies=[Depends(get_current_user)]
)


@router.get(
    "/",
    response_model=list[PagoResponse]
)
@limiter.limit("60/minute")
def listar_pagos(request: Request):
    return PagoController.listar()


@router.get(
    "/{pago_id}",
    response_model=PagoResponse
)
@limiter.limit("60/minute")
def obtener_pago(
    request: Request,
    pago_id: int
):
    return PagoController.obtener(pago_id)


@router.post(
    "/",
    response_model=PagoResponse,
    status_code=201
)
@limiter.limit("20/minute")
def crear_pago(
    request: Request,
    pago: PagoCreate
):
    return PagoController.crear(pago)


@router.put(
    "/{pago_id}",
    response_model=PagoResponse
)
@limiter.limit("20/minute")
def actualizar_pago(
    request: Request,
    pago_id: int,
    pago: PagoUpdate
):
    return PagoController.actualizar(
        pago_id,
        pago
    )


@router.delete("/{pago_id}")
@limiter.limit("10/minute")
def eliminar_pago(
    request: Request,
    pago_id: int
):
    return PagoController.eliminar(pago_id)
