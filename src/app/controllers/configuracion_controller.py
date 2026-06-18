from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.database.connection import SessionLocal
from src.app.models.configuracion import Configuracion

import logging

logger = logging.getLogger(__name__)


class ConfiguracionController:

    @staticmethod
    def obtener():
        logger.info("Consulta de configuración")

        db = SessionLocal()

        try:
            configuracion = db.query(
                Configuracion
            ).first()

            if not configuracion:
                configuracion = Configuracion(
                    importe_mensual=0,
                    dias_recordatorio=3
                )

                db.add(configuracion)
                db.commit()
                db.refresh(configuracion)

            return configuracion

        except SQLAlchemyError as e:
            logger.error(
                f"Error al obtener configuración: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error interno del servidor"
            )

        finally:
            db.close()

    @staticmethod
    def actualizar(config_data):
        logger.info(
            "Actualización de configuración"
        )

        db = SessionLocal()

        try:
            configuracion = db.query(
                Configuracion
            ).first()

            if not configuracion:
                configuracion = Configuracion()

                db.add(configuracion)

            configuracion.importe_mensual = (
                config_data.importe_mensual
            )

            configuracion.dias_recordatorio = (
                config_data.dias_recordatorio
            )

            db.commit()
            db.refresh(configuracion)

            logger.info(
                "Configuración actualizada"
            )

            return configuracion

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al actualizar configuración: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al actualizar configuración"
            )

        finally:
            db.close()

