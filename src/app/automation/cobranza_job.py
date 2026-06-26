from datetime import date, timedelta
import logging

from src.app.database.connection import SessionLocal
from src.app.models.cliente import Cliente
from src.app.models.configuracion import Configuracion

logger = logging.getLogger(__name__)


def verificar_vencimientos():

    logger.info(
        "Iniciando verificación de vencimientos"
    )

    db = SessionLocal()

    try:

        configuracion = db.query(
            Configuracion
        ).first()

        if not configuracion:
            logger.warning(
                "No existe configuración cargada"
            )
            return

        hoy = date.today()

        fecha_limite = (
            hoy +
            timedelta(
                days=configuracion.dias_recordatorio
            )
        )

        clientes_proximos = db.query(
            Cliente
        ).filter(
            Cliente.fecha_vencimiento >= hoy,
            Cliente.fecha_vencimiento <= fecha_limite,
            Cliente.activo == True
        ).all()

        clientes_vencidos = db.query(
            Cliente
        ).filter(
            Cliente.fecha_vencimiento < hoy,
            Cliente.activo == True
        ).all()

        logger.info(
            f"Clientes próximos a vencer: "
            f"{len(clientes_proximos)}"
        )

        logger.info(
            f"Clientes vencidos: "
            f"{len(clientes_vencidos)}"
        )

        for cliente in clientes_proximos:

            dias_restantes = (
                cliente.fecha_vencimiento - hoy
            ).days

            logger.info(
                f"[ID {cliente.id}] "
                f"{cliente.nombre} "
                f"vence en {dias_restantes} días"
            )

        for cliente in clientes_vencidos:

            dias_vencido = (
                hoy - cliente.fecha_vencimiento
            ).days

            logger.warning(
                f"[ID {cliente.id}] "
                f"{cliente.nombre} "
                f"vencido hace {dias_vencido} días"
            )

    except Exception as e:

        logger.error(
            f"Error verificando vencimientos: {str(e)}"
        )

    finally:
        db.close()