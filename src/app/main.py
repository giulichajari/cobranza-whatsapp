from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from src.app.auth.auth_routes import router as auth_router
from src.app.automation.scheduler import scheduler
from src.app.middleware.rate_limit import limiter

from src.app.routes.cliente_routes import router as cliente_router
from src.app.routes.pago_routes import router as pago_router
from src.app.routes.configuracion_routes import (
    router as configuracion_router
)

# Importar modelos para SQLAlchemy
from src.app.models.cliente import Cliente
from src.app.models.pago import Pago
from src.app.models.configuracion import Configuracion


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    logger.info("Scheduler iniciado")

    yield

    scheduler.shutdown()
    logger.info("Scheduler detenido")


app = FastAPI(
    lifespan=lifespan
)

logger.info("Iniciando API de cobranza")

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(SlowAPIMiddleware)


@app.get("/")
def home():
    return {
        "message": "API funcionando"
    }


app.include_router(cliente_router)
app.include_router(pago_router)
app.include_router(configuracion_router)