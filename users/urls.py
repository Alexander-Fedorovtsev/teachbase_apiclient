from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordResetView
from . import views


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
        PasswordChangeView.as_view(template_name='users/passchange.html'),
    ),
    path(
        "password_reset/",
        PasswordChangeView.as_view(template_name='users/passreset.html'),
        name="passwordreset"
    ),
    path('tbregister/', views.teachbaseregister, name='tbregister'),
    path('user_profile/', views.showprofilepageview, name='user_profile'),
]
