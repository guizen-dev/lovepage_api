from django.db import models

# Create your models here.

USER_CHOICES = (
    ('Luara','LUARA'),
    ('Guilherme', 'GUILHERME'),
)

class Usuario(models.Model):
    password = models.CharField(max_length=255)
    user = models.CharField(max_length=9, choices=USER_CHOICES, default='Luara')