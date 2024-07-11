from django.urls import path
from .views.app_view import home
from .views import signup_view, login_view

urlpatterns = [
    path("home", home, name="home"),
    path("sign-up", signup_view.View.as_view(), name="signup"),
    path("login", login_view.View.as_view(), name="login"),
]
