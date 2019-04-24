from django.urls import path
from . import views

# Define o nome desse app, para deixar o roteamento mais facil

# O que é colocado entre tag( <> ) significa um valor dinaminco.
#
# O campo "name" serve para darmos um nome ao endereço, para depois nos templates
# apenas precisar referenciar esse nome ao inves do endereço inteiro
app_name = "tarefas"
urlpatterns = [
    path('', views.index, name="index"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('adicionar', views.adicionar, name="adicionar"),
    path('remover/<int:id>', views.remover, name="remover")
]