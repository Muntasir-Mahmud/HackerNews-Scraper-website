from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=2083, default="", unique=True)
    published = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    source = models.CharField(max_length=50, default="", blank=True, null=True)
