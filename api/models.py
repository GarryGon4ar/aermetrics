# Create your models here.
from django.db import models


class Logs(models.Model):
    aircraft = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    info_count = models.IntegerField()
    errors_count = models.IntegerField()
    pre_legend = models.IntegerField()
    warning = models.IntegerField()
    paired_b = models.IntegerField()
    legend = models.IntegerField()
    lower_b = models.IntegerField()
    repeat_legend = models.IntegerField()
    upper_a = models.IntegerField()
    lower_a = models.IntegerField()
    paired_a = models.IntegerField()
