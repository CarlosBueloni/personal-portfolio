from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)
