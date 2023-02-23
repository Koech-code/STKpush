from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views

from .views import (
    RegisterAPI,
    LoginAPI,
)


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]
