from django.db import models
from django.urls import reverse

# Create your models here.

USER_CHOICES = (
    ('Luara','LUARA'),
    ('Guilherme', 'GUILHERME'),
)

class Usuario(models.Model):
    user = models.CharField(max_length=9, choices=USER_CHOICES, default='Luara')
    password = models.CharField(max_length=255)
    slug = models.SlugField(max_length=510, unique=True, default='Luara')
    
    def __str__(self):
        return str(self.user)