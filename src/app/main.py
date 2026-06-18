from fastapi import FastAPI

from src.app.routes.cliente_routes import router as cliente_router
from src.app.routes.pago_routes import router as pago_router
from src.app.routes.configuracion_routes import router as configuracion_router
from src.app.models.cliente import Cliente
from src.app.models.pago import Pago
from src.app.models.configuracion import Configuracion
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "API funcionando"
    }


app.include_router(cliente_router)
app.include_router(pago_router)
app.include_router(configuracion_router)