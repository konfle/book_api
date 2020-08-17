from django.db import models


class ListOfAllBooks(models.Model):
    tittle = models.CharField(max_length=50)
    authors = models.CharField(max_length=50)
    published_date = models.CharField(max_length=4)
    categories = models.CharField(max_length=50)
    average_rating = models.IntegerField()
    rating_counts = models.IntegerField()
    thumbnail = models.URLField()

    def __str__(self):
        return self.tittle
