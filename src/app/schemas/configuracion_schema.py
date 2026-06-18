from decimal import Decimal

from pydantic import BaseModel


class ConfiguracionCreate(BaseModel):
    importe_mensual: Decimal
    dias_recordatorio: int = 3


class ConfiguracionResponse(BaseModel):
    id: int
    importe_mensual: Decimal
    dias_recordatorio: int

    model_config = {
        "from_attributes": True
    }