from django.db import models
import json

# Create your models here.
class Imovel(models.Model):
    price = models.IntegerField()
    condo = models.IntegerField()
    area_total = models.IntegerField()
    area_util = models.IntegerField()
    room = models.IntegerField()
    bathroom = models.IntegerField()
    garage = models.IntegerField()
    address = models.TextField()


class Anuncio(models.Model):
    url = models.URLField()
    title = models.TextField()
    description = models.TextField()
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    images_url = models.JSONField()



