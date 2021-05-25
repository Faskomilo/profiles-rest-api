from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_project.engine import Engine

class TextAPIView(APIView, Engine):
    """
    API View that returns only a text
    """

    def get(self, request, format=None):
        """
        Method get of TextAPIViews
        """
        apiView = [
            "Uses HTTP Methods",
            "Similar to a Django view, but not quite",
            "mapped manually to URL's"
        ]
        return Response(Engine.jsonify("Hello", apiView))