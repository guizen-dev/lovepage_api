# Generated by Django 4.1.4 on 2023-05-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AddField(
            model_name='usuario',
            name='slug',
            field=models.SlugField(default='Luara', max_length=510, unique=True),
        ),
    ]