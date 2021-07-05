from django.db import models


class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=13)
    date_pub = models.DateTimeField('date published')
