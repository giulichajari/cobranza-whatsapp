from datetime import date

from pydantic import BaseModel, EmailStr


class ClienteCreate(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr
    fecha_vencimiento: date
class ClienteUpdate(BaseModel):
    nombre: str
    telefono: str
    email: EmailStr
    fecha_vencimiento: date
    activo: bool
class ClienteResponse(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str
    fecha_vencimiento: date
    activo: bool

    model_config = {
        "from_attributes": True
    }