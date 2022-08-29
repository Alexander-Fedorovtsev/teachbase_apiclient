from django.shortcuts import render
from users.clientapi import getcourses
from courses.models import CourseProfile
from rest_framework.generics import ListCreateAPIView
from .serializers import CourseSerializer


def index(request):
    template = "base.html"
    context = {
        "page_obj": "page_obj",
        "values": "valu",
        "max_order": "max_order",
        "min_order": "min_order",
        "sum_order": "sum_order",
        "sum_cost": "sum_cost",
    }
    return render(request, template, context)

def storycoursesindb():
    courses = getcourses()
    for course in courses:
        validated_data = {
                'id': course.get("id"),
                'name': course.get("name"),
                'created_at': course.get("created_at"),
                'updated_at': course.get("updated_at"),
                'owner_id': course.get("owner_id"),
                'owner_name': course.get("owner_name"),
                'thumb_url': course.get("thumb_url"),
                'cover_url': course.get("cover_url"),
                'description': course.get("description"),
                'last_activity': course.get("last_activity"),
                'total_score': course.get("total_score"),
                'total_tasks': course.get("total_tasks"),
                'unchangeable': course.get("unchangeable"),
                'include_weekly_report': course.get("include_weekly_report"),
                'content_type': course.get("content_type"),
        }
        course = CourseProfile.objects.create(**validated_data)
    
class GetCourses(ListCreateAPIView):
    storycoursesindb()
    queryset = CourseProfile.objects.all()
    serializer_class = CourseSerializer

    
