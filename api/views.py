from re import template
from courses.models import CourseProfile
from .serializers import CourseSerializer
from rest_framework.generics import ListAPIView
from .pagination import CoursesPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from users.clientapi import getcourses
from django.shortcuts import render


class GetCourses(ListAPIView):
    """
    ###Returns a list of all courses stored in the database.

    You can use __page__ and __per_page__ paremeters for pagination.

    """

    queryset = CourseProfile.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursesPagination


class CourseDetail(viewsets.ModelViewSet):
    """
    ###Returns a detail information about course.

    You should use course __id__ number in url i.e. /courses/30133/.

    """

    serializer_class = CourseSerializer

    def get_object(self):
        return get_object_or_404(CourseProfile, id=self.kwargs["courseid"])


def storecoursesindb(request):
    courses = getcourses(per_page=50)
    template = "api/updatebd.html"
    countreaded = 0
    countstored = 0
    for course in courses:
        countreaded += 1

        if not CourseProfile.objects.filter(id=course.get("id")):
            serializer = CourseSerializer(data=course)
            if serializer.is_valid():
                countstored += 1
                serializer.save(id=course.get("id"))
            else:
                error = serializer.errors
    context = {
        "countstored": countstored,
        "countreaded": countreaded,
        "error": error,
    }
    return render(request, template, context)
