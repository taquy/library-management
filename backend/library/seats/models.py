from django.db import models

class Seat(models.Model):
  name = models.CharField(max_length=30)
  age = models.CharField(max_length=30)