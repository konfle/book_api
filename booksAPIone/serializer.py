from . models import ListOfAllBooks
from rest_framework import serializers


class BooksAPIoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfAllBooks
        fields = ('id', 'tittle', 'authors', 'published_date', 'categories',
                  'average_rating', 'rating_counts', 'thumbnail')
