# Generated by Django 4.1.4 on 2022-12-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_reclamacao_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatreclamacao',
            name='desc',
            field=models.TextField(default='', max_length=455),
        ),
    ]
