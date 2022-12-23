from django.db import models

# Create your models here.

class Filme(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

class Lugar(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

class Mural(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

class Jogo(models.Model):
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
