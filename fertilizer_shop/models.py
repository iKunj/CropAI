from django.db import models

class fertilizer_data(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    buyer = models.CharField(max_length=30)
