# Generated by Django 3.2.19 on 2023-05-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.TextField(default='None'),
        ),
    ]