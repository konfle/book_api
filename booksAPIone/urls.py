from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers
from . models import ListOfAllBooks

router = routers.DefaultRouter()
router.register('books', views.BooksView)

urlpatterns = [
    path('', include(router.urls)),
]
