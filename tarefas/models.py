from django.db import models

# Define uma tabela chamada Tarefa
class Tarefa(models.Model):
    # Um campo de texto com nome nome e com tamanho maximo de 200
    nome = models.TextField(max_length=200)
    # Um campo de texto com nome descricao com tamanho maximo de 3000
    descricao = models.TextField(max_length=3000)

    # Sobreescreve o metodo __str__ para podermos ter uma melhor representação do objeto no Django admin
    def __str__(self):
        return self.nome