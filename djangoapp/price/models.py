from django.db import models


# Create your models here.

class pi_db (models.Model):
    date = models.TextField()
    value = models.FloatField()
    currency = models.TextField(max_length=3)
    