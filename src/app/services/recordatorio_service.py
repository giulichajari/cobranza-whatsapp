import logging

logger = logging.getLogger(__name__)


def generar_recordatorio(cliente):

    mensaje = (
        f"Hola {cliente.nombre}, "
        f"te recordamos que tu cuota "
        f"vence el {cliente.fecha_vencimiento}"
    )

    logger.info(mensaje)

    return mensaje