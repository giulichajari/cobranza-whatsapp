from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.database.connection import SessionLocal
from src.app.models.pago import Pago
from src.app.models.cliente import Cliente

import logging

logger = logging.getLogger(__name__)


class PagoController:

    ESTADOS_VALIDOS = [
        "pendiente",
        "pagado",
        "vencido"
    ]

    @staticmethod
    def listar():
        logger.info("Listado de pagos solicitado")

        db = SessionLocal()

        try:
            return db.query(Pago).all()

        except SQLAlchemyError as e:
            logger.error(f"Error al listar pagos: {str(e)}")

            raise HTTPException(
                status_code=500,
                detail="Error interno del servidor"
            )

        finally:
            db.close()

    @staticmethod
    def obtener(pago_id: int):
        logger.info(f"Consulta de pago ID={pago_id}")

        db = SessionLocal()

        try:
            pago = db.query(Pago).filter(
                Pago.id == pago_id
            ).first()

            if not pago:
                raise HTTPException(
                    status_code=404,
                    detail="Pago no encontrado"
                )

            return pago

        except HTTPException:
            raise

        except SQLAlchemyError as e:
            logger.error(f"Error al obtener pago: {str(e)}")

            raise HTTPException(
                status_code=500,
                detail="Error interno del servidor"
            )

        finally:
            db.close()

    @staticmethod
    def crear(pago_data):
        logger.info(
            f"Creación de pago para cliente ID={pago_data.cliente_id}"
        )

        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == pago_data.cliente_id
            ).first()

            if not cliente:
                raise HTTPException(
                    status_code=404,
                    detail="Cliente no encontrado"
                )

            if pago_data.estado not in PagoController.ESTADOS_VALIDOS:
                raise HTTPException(
                    status_code=400,
                    detail="Estado de pago inválido"
                )

            pago = Pago(
                cliente_id=pago_data.cliente_id,
                importe=pago_data.importe,
                fecha_pago=pago_data.fecha_pago,
                estado=pago_data.estado
            )

            db.add(pago)
            db.commit()
            db.refresh(pago)

            logger.info(
                f"Pago creado ID={pago.id}"
            )

            return pago

        except HTTPException:
            raise

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al crear pago: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al crear pago"
            )

        finally:
            db.close()

    @staticmethod
    def actualizar(pago_id: int, pago_data):
        logger.info(
            f"Actualización de pago ID={pago_id}"
        )

        db = SessionLocal()

        try:
            pago = db.query(Pago).filter(
                Pago.id == pago_id
            ).first()

            if not pago:
                raise HTTPException(
                    status_code=404,
                    detail="Pago no encontrado"
                )

            cliente = db.query(Cliente).filter(
                Cliente.id == pago_data.cliente_id
            ).first()

            if not cliente:
                raise HTTPException(
                    status_code=404,
                    detail="Cliente no encontrado"
                )

            if pago_data.estado not in PagoController.ESTADOS_VALIDOS:
                raise HTTPException(
                    status_code=400,
                    detail="Estado de pago inválido"
                )

            pago.cliente_id = pago_data.cliente_id
            pago.importe = pago_data.importe
            pago.fecha_pago = pago_data.fecha_pago
            pago.estado = pago_data.estado

            db.commit()
            db.refresh(pago)

            logger.info(
                f"Pago actualizado ID={pago.id}"
            )

            return pago

        except HTTPException:
            raise

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al actualizar pago: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al actualizar pago"
            )

        finally:
            db.close()

    @staticmethod
    def eliminar(pago_id: int):
        logger.warning(
            f"Solicitud de eliminación de pago ID={pago_id}"
        )

        db = SessionLocal()

        try:
            pago = db.query(Pago).filter(
                Pago.id == pago_id
            ).first()

            if not pago:
                raise HTTPException(
                    status_code=404,
                    detail="Pago no encontrado"
                )

            db.delete(pago)
            db.commit()

            logger.warning(
                f"Pago eliminado ID={pago_id}"
            )

            return {
                "message": "Pago eliminado correctamente"
            }

        except HTTPException:
            raise

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al eliminar pago: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al eliminar pago"
            )

        finally:
            db.close()

