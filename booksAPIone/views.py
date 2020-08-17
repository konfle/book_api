# from django.shortcuts import render
from rest_framework import viewsets
from . models import ListOfAllBooks
from . serializer import BooksAPIoneSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class BooksView(viewsets.ModelViewSet):
    queryset = ListOfAllBooks.objects.all()
    serializer_class = BooksAPIoneSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['published_date', 'authors']
    ordering_fields = ['published_date']


