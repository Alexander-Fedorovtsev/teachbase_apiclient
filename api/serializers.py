from rest_framework.serializers import ModelSerializer
from courses.models import CourseProfile


class CourseSerializer(ModelSerializer):
    class Meta:
        model = CourseProfile
        fields = "__all__"
