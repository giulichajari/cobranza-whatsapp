from fastapi import APIRouter

router = APIRouter(
    prefix="/configuracion",
    tags=["Configuracion"]
)


@router.get("/")
def obtener_configuracion():
    pass


@router.put("/")
def actualizar_configuracion():
    pass