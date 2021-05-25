from django.urls import path
from profiles_api import views

urlpatterns = [
    path('text_view/', views.TextAPIView.as_view()),
]