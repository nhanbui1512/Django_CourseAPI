from rest_framework.serializers import ModelSerializer
from .models import *


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_at', 'category']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class LessionSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    course = CourseSerializer()

    class Meta:
        model = Lession
        fields = ['id', 'subject', 'content',
                  'created_at', 'course', 'tags', 'image']
