class Engine():
    def jsonify(message, data, status="OK"):
        json = {
            "message":message,
            "data": data,
            "status": status
        }
        return json