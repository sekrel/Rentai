from django.db import models

class New(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)