from django.urls import path
from .views import UserListMyProfileAPIView, UserUpdateAPIView


urlpatterns = [
    path("update/", UserUpdateAPIView.as_view(), name='atualizer_user'),
    path("perfil/", UserListMyProfileAPIView.as_view(), name="perfil_user")
]

