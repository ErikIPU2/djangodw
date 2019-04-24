from django.contrib import admin
from .models import Tarefa

# Register your models here.

# Adiciona a tabela Tarefa no Django admin
admin.site.register(Tarefa)