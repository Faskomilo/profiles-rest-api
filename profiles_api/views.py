from rest_framework import authentication, status, viewsets, filters
from rest_framework.exceptions import server_error
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from profiles_api import models, serializers, permissions
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

class TextViewSet(viewsets.ViewSet):
    """
    View Set that returns only a text
    """
    serializer_class = serializers.TextSerializer
    
    def list(self, request):
        """
        Returns a text
        """

        viewset = [
            "Uses actions such as list, create, retrieve, update, partial_update",
            "Automatically maps to URLs using Routers",
            "Provides moore functionality with less code"
        ]

        return Response(Engine.serializeJson("Hola", viewset))

    def create(self, request):
        """
        Create a new text message
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

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        """
        return Response(
            Engine.serializeJson(
                "updating",
                { "http Method":"Get" }
            )
        )

    def update(self, request, pk=None):
        """
        Handle updating an object by its ID
        """
        return Response(
            Engine.serializeJson(
                "updating",
                { "http Method":"PUT" }
            )
        )

    def partial_update(self, request, pk=None):
        """
        Handle getting an object by its ID
        """
        return Response(
            Engine.serializeJson(
                "updating",
                { "http Method":"PATCH" }
            )
        )


    def destroy(self, request, pk=None):
        """
        Handle getting an object by its ID
        """
        return Response(
            Engine.serializeJson(
                "updating",
                { "http Method":"DELETE" }
            )
        )

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handle the creation and updating of profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """
    Handle creating user authentication tokens
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD of profile feed items
    """

    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemsSerializer
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user
        """

        serializer.save(user_profile = self.request.user)
        return super().perform_create(serializer)

