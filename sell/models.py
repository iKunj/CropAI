from django.db import models

class farmer_crops(models.Model):
    farmer_name = models.CharField(max_length=90)
    crop_name = models.CharField(max_length=90)
    amount = models.IntegerField()
    quantity = models.IntegerField()
    bought = models.CharField(max_length=90)
    flag = models.IntegerField(default = 0)

class buyer_demand(models.Model):
    buyer_name = models.CharField(max_length=90)
    crop_name = models.CharField(max_length=90)
    amount = models.IntegerField()
    quantity = models.IntegerField()
    bought = models.CharField(max_length=90)
    flag = models.IntegerField(default = 0)