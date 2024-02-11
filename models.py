# In thesis/models.py

from django.db import models

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    abstract = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title
