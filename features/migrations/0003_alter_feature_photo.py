# Generated by Django 3.2.19 on 2023-05-24 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20230517_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='photo',
            field=models.FileField(upload_to='media/'),
        ),
    ]