from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='images', verbose_name='Достопримечательность')
    image = models.ImageField('Картинка')
    position = models.IntegerField('Номер')

    def __str__(self):
        return f"{self.position} {self.place}"
