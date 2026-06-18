from src.app.database.connection import SessionLocal
from src.app.models.cliente import Cliente


class ClienteController:

    @staticmethod
    def listar():
        db = SessionLocal()

        try:
            return db.query(Cliente).all()
        finally:
            db.close()

    @staticmethod
    def obtener(cliente_id: int):
        db = SessionLocal()

        try:
            return db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()
        finally:
            db.close()

    @staticmethod
    def crear(cliente_data):
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

            return cliente

        finally:
            db.close()

    @staticmethod
    def actualizar(cliente_id: int, cliente_data):
        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if not cliente:
                return {"error": "Cliente no encontrado"}

            cliente.nombre = cliente_data.nombre
            cliente.telefono = cliente_data.telefono
            cliente.email = cliente_data.email
            cliente.fecha_vencimiento = cliente_data.fecha_vencimiento

            db.commit()
            db.refresh(cliente)

            return cliente

        finally:
            db.close()

    @staticmethod
    def eliminar(cliente_id: int):
        db = SessionLocal()

        try:
            cliente = db.query(Cliente).filter(
                Cliente.id == cliente_id
            ).first()

            if not cliente:
                return {"error": "Cliente no encontrado"}

            db.delete(cliente)
            db.commit()

            return {"message": "Cliente eliminado"}
        finally:
            db.close()