from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return f"{self.title}"
