from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    phone_number = models.CharField(max_length=255, verbose_name=_('Phone Number'), unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    worker = models.ForeignKey(Worker, related_name='units', on_delete=models.CASCADE, verbose_name=_('Worker'))

    def __str__(self):
        return f'Unit {self.name} by {self.worker.name}'


class Visit(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='visits', verbose_name=_('Unit'))
    datetime = models.DateTimeField(default=timezone.now, verbose_name=_('Date/Time'))
    latitude = models.FloatField(verbose_name=_('Latitude'))
    longitude = models.FloatField(verbose_name=_('Longitude'))

    def __str__(self):
        return f'Visit to {self.unit.name} on {self.datetime}'
