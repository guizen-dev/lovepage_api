# Generated by Django 4.1.4 on 2023-05-09 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('chat', '0003_chatreclamacao_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatreclamacao',
            old_name='desc',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='chatreclamacao',
            name='isEnvio',
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='state',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=13),
        ),
        migrations.AlterField(
            model_name='reclamacao',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
