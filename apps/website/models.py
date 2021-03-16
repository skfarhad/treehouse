from django.db import models
from django.utils.timezone import now
from apps.website.config import PARA_TYPES, TEXT_TYPES


class Paragraph(models.Model):
    type = models.PositiveSmallIntegerField(default=0, choices=PARA_TYPES)
    title = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    image_path = models.ImageField(upload_to="para_images/", blank=True, null=True)
    timestamp = models.DateTimeField(default=now)


class TextField(models.Model):
    type = models.PositiveSmallIntegerField(default=0, choices=TEXT_TYPES)
    text = models.CharField(max_length=512, blank=False)


class ImageField(models.Model):
    title = models.CharField(max_length=256, blank=True)
    image_path = models.ImageField(upload_to="para_images/", blank=True, null=True)
