from users.clientapi import getcourses
from courses.models import CourseProfile
from .serializers import CourseSerializer


def storecoursesindb(num=1):
    courses = getcourses(per_page=num)
    for course in courses:
        if not CourseProfile.objects.filter(id=course.get("id")):
            serializer = CourseSerializer(data=course)
            if serializer.is_valid():
                serializer.save(id=course.get("id"))
