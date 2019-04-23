from django.urls import path
from . import views

app_name = "tarefas"
urlpatterns = [
    path('', views.index, name="index"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('adicionar', views.adicionar, name="adicionar"),
    path('remover/<int:id>', views.remover, name="remover")
]