from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('filme', 'filme'),
    ('lugar', 'lugar'),
    ('mural', 'mural'),
    ('jogo', 'jogo')
)

class Feature(models.Model):
    photo = models.CharField(max_length=255, default='filme')
    name = models.CharField(max_length=255, default='filme')
    desc = models.CharField(max_length=255, default='filme')
    type = models.CharField(max_length=13, choices=STATE_CHOICES, default='filme')