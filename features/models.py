from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('filme', 'filme'),
    ('lugar', 'lugar'),
    ('mural', 'mural')
)

class Feature(models.Model):
    photo = models.FileField(upload_to='media/')
    name = models.CharField(max_length=255, default='filme')
    desc = models.CharField(max_length=255, default='filme')
    type = models.CharField(max_length=13, choices=STATE_CHOICES, default='filme')
    rating = models.CharField(max_length=2, default='0')