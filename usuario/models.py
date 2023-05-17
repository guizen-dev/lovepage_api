from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.

class Usuario(AbstractBaseUser):
    user = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    photo = models.TextField(default='None')
    
    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return str(self.user)