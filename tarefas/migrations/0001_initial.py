# Generated by Django 2.2 on 2019-04-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=200)),
                ('descricao', models.TextField(max_length=3000)),
                ('dataCriacao', models.DateField(auto_now_add=True)),
                ('dataModificacao', models.DateField(auto_now=True)),
            ],
        ),
    ]
