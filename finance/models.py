from django.db import models

class history(models.Model):
    farmer_name = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    amount = models.IntegerField()
    date = models.CharField(max_length=10)

class total_budget(models.Model):
    farmer_name = models.CharField(max_length=90)
    amount = models.IntegerField()