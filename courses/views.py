from django.shortcuts import render
import datetime
from django.shortcuts import render
from users import clientapi
from users.models import Profile


def getcoursesinfo(request):
    template = "courses/get_courses.html"
    courses = clientapi.getcourses(page=1, per_page=50)
    context = {
        "courses": courses,
    }
    return render(request, template, context)


def coursedetail(request, id):
    template = "courses/course_detail.html"
    course = clientapi.getcoursedetail(courseid=id)
    sessions = clientapi.getcoursesessions(courseid=id)
    sessionscount = len(sessions)
    course["created_at"] = datetime.datetime.strptime(
        course["created_at"][:19], "%Y-%m-%dT%H:%M:%S"
    ).date()
    course["updated_at"] = datetime.datetime.strptime(
        course["updated_at"][:19], "%Y-%m-%dT%H:%M:%S"
    ).date()
    print(course["created_at"])
    context = {
        "course": course,
        "sessions": sessions,
        "sessionscount": sessionscount,
    }
    return render(request, template, context)


def sessionregister(request, courseid, sessionid):
    template = "courses/session_register.html"
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    response = clientapi.sessionregister(
        sessionid=sessionid, email=user.email, user_id=profile.externalid
    )
    context = {"user": user, "statuscode": response[0], "message": response[1]}
    return render(request, template, context)
