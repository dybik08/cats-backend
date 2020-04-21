from django.db import models


class Cat(models.Model):
    tags = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=30, blank=True)
    user = models.CharField(max_length=30, blank=True)
    imageURL = models.CharField(max_length=100, blank=True)
