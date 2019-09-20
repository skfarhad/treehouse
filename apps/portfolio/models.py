from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)


class WorkHistory(models.Model):
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    category = models.TextField(max_length=128, blank=True)
