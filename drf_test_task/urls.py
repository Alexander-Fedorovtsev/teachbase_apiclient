from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls", namespace="users")),
    path(
        "auth/", include(("django.contrib.auth.urls", "authorisation"), namespace="auth")
    ),
    path("courses/", include("courses.urls", namespace="courses")),
    path("api/", include("api.urls", namespace="api")),
]
