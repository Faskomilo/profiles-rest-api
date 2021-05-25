from rest_framework.exceptions import server_error
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
from profiles_project.engine import Engine

class TextAPIView(APIView):
    """
    API View that returns only a text
    """

    serializer_class = serializers.TextSerializer

    def get(self, request, format=None):
        """
        Method get of TextAPIViews
        """
        api_view = [
            "Uses HTTP Methods",
            "Similar to a Django view, but not quite",
            "mapped manually to URL's"
        ]
        return Response(Engine.serializeJson("Hello", api_view))

    def post(self, request):
        """
        Return a text with a given variable
        """
        serializer = self.serializer_class(data=request.data)
        data = {
            "Recieved data":request.data
            }

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response(
                Engine.serializeJson(
                    message, 
                    data
                    )
                )
        else:
            return Response(
                Engine.serializeJson(serializer.errors, data, "KO"), 
                status=status.HTTP_400_BAD_REQUEST
                )
    def put(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response(
            Engine.serializeJson(
                "Put",
                ""
            )
        )

    def patch(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response(
            Engine.serializeJson(
                "Patch",
                ""
            )
        )

    def delete(self, request, pk=None):
        """
        Delete an object
        """
        return Response(
            Engine.serializeJson(
                "Delete",
                ""
            )
        )