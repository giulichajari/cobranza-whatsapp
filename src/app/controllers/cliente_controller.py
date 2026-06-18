from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.database.connection import SessionLocal
from src.app.models.cliente import Cliente

import logging

logger = logging.getLogger(__name__)


class ClienteController:

    @staticmethod
    def listar():
        logger.info("Listado de clientes solicitado")

        db = SessionLocal()

        try:
            return db.query(Cliente).all()

        except SQLAlchemyError as e:
            logger.error(f"Error al listar clientes: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Error interno del servidor"
            )

        finally:
            db.close()

    @staticmethod
    def obtener(cliente_id: int):
        logger.info(f"Consulta de cliente ID={cliente_id}")

        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if not cliente:
                logger.warning(
                    f"Cliente no encontrado ID={cliente_id}"
                )

                raise HTTPException(
                    status_code=404,
                    detail="Cliente no encontrado"
                )

            return cliente

        except SQLAlchemyError as e:
            logger.error(f"Error al obtener cliente: {str(e)}")

            raise HTTPException(
                status_code=500,
                detail="Error interno del servidor"
            )

        finally:
            db.close()

    @staticmethod
    def crear(cliente_data):
        logger.info(
            f"Intento de creación de cliente EMAIL={cliente_data.email}"
        )

        db = SessionLocal()

        try:
            cliente = Cliente(
                nombre=cliente_data.nombre,
                telefono=cliente_data.telefono,
                email=cliente_data.email,
                fecha_vencimiento=cliente_data.fecha_vencimiento
            )

            db.add(cliente)
            db.commit()
            db.refresh(cliente)

            logger.info(
                f"Cliente creado ID={cliente.id} EMAIL={cliente.email}"
            )

            return cliente

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al crear cliente: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al crear cliente"
            )

        finally:
            db.close()

    @staticmethod
    def actualizar(cliente_id: int, cliente_data):
        logger.info(
            f"Actualización de cliente ID={cliente_id}"
        )

        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if not cliente:
                logger.warning(
                    f"Cliente no encontrado ID={cliente_id}"
                )

                raise HTTPException(
                    status_code=404,
                    detail="Cliente no encontrado"
                )

            cliente.nombre = cliente_data.nombre
            cliente.telefono = cliente_data.telefono
            cliente.email = cliente_data.email
            cliente.fecha_vencimiento = cliente_data.fecha_vencimiento

            db.commit()
            db.refresh(cliente)

            logger.info(
                f"Cliente actualizado ID={cliente.id}"
            )

            return cliente

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al actualizar cliente: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al actualizar cliente"
            )

        finally:
            db.close()

    @staticmethod
    def eliminar(cliente_id: int):
        logger.warning(
            f"Solicitud de eliminación cliente ID={cliente_id}"
        )

        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if not cliente:
                raise HTTPException(
                    status_code=404,
                    detail="Cliente no encontrado"
                )

            db.delete(cliente)
            db.commit()

            logger.warning(
                f"Cliente eliminado ID={cliente_id}"
            )

            return {
                "message": "Cliente eliminado correctamente"
            }

        except SQLAlchemyError as e:
            db.rollback()

            logger.error(
                f"Error al eliminar cliente: {str(e)}"
            )

            raise HTTPException(
                status_code=500,
                detail="Error al eliminar cliente"
            )

        finally:
            db.close()

