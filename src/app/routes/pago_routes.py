from fastapi import APIRouter

router = APIRouter(prefix="/pagos", tags=["Pagos"])


@router.get("/")
def listar_pagos():
    pass


@router.get("/{pago_id}")
def obtener_pago(pago_id: int):
    pass


@router.post("/")
def crear_pago():
    pass