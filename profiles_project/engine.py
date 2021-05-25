class Engine():
    def serializeJson(message, data, status="OK"):
        json = {
            "message":message,
            "data": data,
            "status": status
        }
        return json