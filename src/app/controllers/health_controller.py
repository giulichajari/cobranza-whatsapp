class HealthController:

    @staticmethod
    def check():
        return {
            "status": "ok",
            "message": "API funcionando"
        }