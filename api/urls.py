from django.urls import path
from . import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

app_name = "api"

urlpatterns = [
    path("courses/", views.GetCourses.as_view()),
    path(
        "courses/<int:courseid>/",
        views.CourseDetail.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="coursedetail",
    ),
    path(
        "openapi",
        get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
]
