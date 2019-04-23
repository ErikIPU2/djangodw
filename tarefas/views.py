from django.shortcuts import render, get_object_or_404
from .models import Tarefa
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', {
        'tarefas' : tarefas
    })

def editar(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.POST:
        tarefa.nome = request.POST['nome']
        tarefa.descricao = request.POST['descricao']
        tarefa.save()
        return HttpResponseRedirect(reverse('tarefas:index'))

    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})

def adicionar(request):
    if request.POST:
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        Tarefa.objects.create(nome=nome, descricao=descricao)
        return HttpResponseRedirect(reverse('tarefas:index'))
    return render(request, 'tarefas/adicionar.html')

def remover(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()
    return  HttpResponseRedirect(reverse('tarefas:index'))