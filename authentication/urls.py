from django.urls import path

from .views import SinginView, SignoutView, SingupView

urlpatterns = [
    path("register/", SingupView.as_view(), name="criar_user"),
    path("login/", SinginView.as_view(), name="login_user"),
    path("logout/", SignoutView.as_view(), name="logout_user"),
]
