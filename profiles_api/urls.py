from django import urls
from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('test-viewset', views.TextViewSet, basename='text-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('text_view/', views.TextAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]