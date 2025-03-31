from django.db import models

class New(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Новость")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создвния")


class Game(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название игры")
    description = models.TextField(blank=True, verbose_name="Теги")
    genre = models.CharField(max_length=255, verbose_name="творчество")
    release_date = models.DateTimeField(auto_now_add=True, verbose_name="творчество")


class Creation(models.Model):
    user_name = models.CharField(max_length=255)
    text = models.TextField( )
    image = models.ImageField(upload_to='creation/', verbose_name="творчество")
    description = models.TextField(blank=True, verbose_name="творчество")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="творчество")