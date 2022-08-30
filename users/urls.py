from django.urls import path, include
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
    PasswordChangeView,
    PasswordResetView,
)
from . import views
from django.urls import reverse_lazy


app_name = "users"
urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path(
        "signup/",
        views.SignUp.as_view(template_name="users/signup.html"),
        name="signup",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(success_url=reverse_lazy('index'),template_name="users/passchange.html"),
    ),
    path("tbregister/", views.teachbaseregister, name="tbregister"),
    path("user_profile/", views.showprofilepageview, name="user_profile"),
]
