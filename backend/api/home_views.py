from rest_framework.response import Response
from rest_framework.decorators import api_view
from .middlewares import *

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# API chung
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve general data",
    tags=["General"],
    responses={200: openapi.Response(
        "Success", examples={"application/json": {"message": "Hello world"}})}
)
@api_view(['GET'])
def get_data(request, *args, **kwargs):
    print("hello")
    return Response(data={"message": "Hello world"}, status=200)


# API chi tiết
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve detailed data by ID and Book ID",
    tags=["Details"],
    manual_parameters=[
        openapi.Parameter(
            'id', openapi.IN_PATH, description="primary key", type=openapi.TYPE_INTEGER),
        openapi.Parameter('id_book', openapi.IN_PATH,
                          description="Book id", type=openapi.TYPE_INTEGER),
    ],
    responses={200: openapi.Response(
        "Success", examples={"application/json": {"message": "Detail data"}})}
)
@admin_middleware
@api_view(['GET'])
def get_detail_data(request, id, id_book, *args, **kwargs):
    return Response(data={"message": "Detail data" + str(id) + str(id_book)}, status=200)
