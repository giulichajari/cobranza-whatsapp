from fastapi import APIRouter

from src.app.controllers.cliente_controller import ClienteController
from src.app.schemas.client_schema import ClienteCreate

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get("/")
def listar_clientes():
    return ClienteController.listar()


@router.get("/{cliente_id}")
def obtener_cliente(cliente_id: int):
    return ClienteController.obtener(cliente_id)


@router.post("/")
def crear_cliente(cliente: ClienteCreate):
    return ClienteController.crear(cliente)


@router.put("/{cliente_id}")
def actualizar_cliente(
    cliente_id: int,
    cliente: ClienteCreate
):
    return ClienteController.actualizar(
        cliente_id,
        cliente
    )


@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    return ClienteController.eliminar(cliente_id)