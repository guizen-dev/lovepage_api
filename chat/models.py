from django.db import models

# Create your models here.

USER_CHOICES = (
    ('Luara', 'LUARA'),
    ('Guilherme', 'GUILHERME'),
)

STATE_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
)

class Reclamacao(models.Model):
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=13, choices=STATE_CHOICES, default='Não resolvido')
    user = models.CharField(max_length=9, choices=USER_CHOICES, default='Luara')

    def __str__(self):
        return str(self.title)


class ChatReclamacao(models.Model):
    reclamacao = models.ForeignKey(Reclamacao, on_delete=models.CASCADE)
    isEnvio = models.BooleanField()
    user = models.CharField(max_length=9, choices=USER_CHOICES, default='Luara')
    desc = models.TextField(max_length=455, default='')