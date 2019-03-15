from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

