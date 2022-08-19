from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views


app_name = "courses"
urlpatterns = [
    path(
        "get_courses/",
        views.getcoursesinfo,
        name="getcourses",
    ),
     path(
        "course_detail/<int:id>",
        views.coursedetail,
        name="coursedetail",
    ),
    path(
        "course_detail/<int:courseid>/sessionregister/<int:sessionid>",
        views.sessionregister,
        name="sessionregister",
    ),
]
