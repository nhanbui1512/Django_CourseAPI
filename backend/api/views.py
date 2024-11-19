from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .middlewares import *


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @auth_middleware
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer


class LessionViewSet(viewsets.ModelViewSet):
    queryset = Lession.objects.filter(active=True)
    serializer_class = LessionSerializer

    @action(methods=['patch'], detail=True, url_path="hide-lession")
    # /api/lessions/{pk}/hide-lession
    def hide_lession(self, request, pk):
        try:

            lession = Lession.objects.get(pk=pk)
            lession.active = False
            lession.save()
        except Lession.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(data=LessionSerializer(lession, context={'request': request}).data, status=status.HTTP_200_OK)


def api_home(request):
    return HttpResponse("Hello")
