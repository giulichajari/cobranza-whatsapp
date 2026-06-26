from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from src.app.automation.cobranza_job import (
    verificar_vencimientos
)

scheduler = BackgroundScheduler()

scheduler.add_job(
    verificar_vencimientos,
    "interval",
    minutes=1
)