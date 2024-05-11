from django.db import models

class CropData(models.Model):
    id=models.AutoField(primary_key=True)
    nitrogen = models.FloatField(default=0)
    phosphorus = models.FloatField(default=0)
    potassium = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    rainfall = models.FloatField(default=0)
    result=models.CharField(max_length=200)