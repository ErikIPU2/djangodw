# Generated by Django 2.2 on 2019-04-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='dataModificacao',
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
