from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('filme', 'filme'),
    ('lugar', 'lugar'),
    ('mural', 'mural')
)

class Feature(models.Model):
    photo_file = models.FileField(upload_to='media/', default='', null=True)
    photo_url = models.CharField(max_length=255, default='', null=True)
    name = models.CharField(max_length=455, default='')
    desc = models.CharField(max_length=455, default='')
    type = models.CharField(max_length=13, choices=STATE_CHOICES, default='')
    rating = models.CharField(max_length=2, default='0')
    checked = models.BooleanField(default=False)