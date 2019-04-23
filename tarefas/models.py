from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.TextField(max_length=200)
    descricao = models.TextField(max_length=3000)

    def __str__(self):
        return self.nome