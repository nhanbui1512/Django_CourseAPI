from django.http import HttpResponse
from .models import *
from .serializers import *

from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer


class LessionViewSet(viewsets.ModelViewSet):
    queryset = Lession.objects.filter(active=True)
    serializer_class = LessionSerializer


def api_home(request):
    return HttpResponse("Hello")
