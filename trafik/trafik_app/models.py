from django.db import models

# Create your models here.
class ODBE(models.Model):
    ndn = models.CharField(max_length=10)
    megnevezes = models.CharField(max_length=200)
    gyarto = models.CharField(max_length=200)
    kategoria = models.CharField(max_length=200)
