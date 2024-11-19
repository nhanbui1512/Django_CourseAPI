from django.urls import path, include
from . import home_views

urlpatterns = [
    path('', home_views.get_data),
    path('<int:id>/<int:id_book>/', home_views.get_detail_data),
]
