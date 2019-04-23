# Faz o roteamento dos caminhos
from django.urls import path
from . import views

urlpatterns = [
    # O que é colocado entre tag( <> ) significa um valor dinaminco.
    #
    # O campo "name" serve para darmos um nome ao endereço, para depois nos templates
    # apenas precisar referenciar esse nome ao inves do endereço inteiro
    path('gerado/<int:numero>', views.gerado, name="gerado"),
    path('template/<int:numero>', views.template, name="template"),
    path('template/<int:numero>/<int:vezes>', views.template2, name="template2")
]
