from django.urls import path
from .views import signup_view, login_view, home_view

urlpatterns = [
    path("home", home_view.View.as_view(), name="home"),
    path("sign-up", signup_view.View.as_view(), name="signup"),
    path("login", login_view.View.as_view(), name="login"),
]
