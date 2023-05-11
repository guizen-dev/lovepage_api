from django.db import models
from usuario.models import Usuario

# Create your models here.

USER_CHOICES = (
    ('Luara', 'LUARA'),
    ('Guilherme', 'GUILHERME'),
)

STATE_CHOICES = (
    ('0', '0'),
    ('1', '1')
)

class Reclamacao(models.Model):
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=13, choices=STATE_CHOICES, default='0')
    user = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.title)


class ChatReclamacao(models.Model):
    reclamacao = models.ForeignKey(Reclamacao, on_delete=models.CASCADE)
    user = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )
    message = models.TextField(max_length=455, default='')
    