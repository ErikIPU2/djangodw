from django.shortcuts import render, get_object_or_404
from .models import Tarefa
from django.http import HttpResponseRedirect
from django.urls import reverse

# Pagina inicial
def index(request):
    # Pega todos os objetos da tabela tarefas e manda junto com o template para renderizar
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', {
        'tarefas' : tarefas
    })

# Pagina de edição
def editar(request, id):
    # Checa se existe um objeto com o id informado, se não existir manda para uma pagina 404
    tarefa = get_object_or_404(Tarefa, pk=id)
    # Verifica se foi feita uma requisição post
    if request.POST:
        # Redefine os campos do objetos com as informações mandadas no post
        tarefa.nome = request.POST['nome']
        tarefa.descricao = request.POST['descricao']
        tarefa.save()
        # Redireciona a pagina para a pagina index
        return HttpResponseRedirect(reverse('tarefas:index'))
    # Se não for feita nenhuma requisição post, renderiza o template editar.html
    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})

# Pagina de adição
def adicionar(request):
    # Verifica se foi feita uma requisição posst
    if request.POST:
        # Cria um novo objeto no bando de dados e redireciona a pagina para o index
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        Tarefa.objects.create(nome=nome, descricao=descricao)
        return HttpResponseRedirect(reverse('tarefas:index'))
    # Se não for feita nenhuma requisição renderiza o template adicionar.html
    return render(request, 'tarefas/adicionar.html')

# Rota de remoção
def remover(request, id):
    # Verifica se existe um objeto com o id informado, se não existir vai para uma pagina 404
    tarefa = get_object_or_404(Tarefa, pk=id)
    # Se existir deleta ele e redireciona para o index
    tarefa.delete()
    return  HttpResponseRedirect(reverse('tarefas:index'))
