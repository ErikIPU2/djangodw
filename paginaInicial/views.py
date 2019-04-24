from django.shortcuts import render

# Create your views here.

# Rota principal
def index(request):
    return render(request, 'paginaInicial/index.html')