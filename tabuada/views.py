from django.shortcuts import render
# O Django sempre espera um retorno de um HttpResponse
from django.http import HttpResponse

# Create your views here.

# Geração da pagina manualmente, depois retornada como um HttpResponse
def gerado(request, numero):
    pagina = "<h1> Tabuada do " + str(numero) + "</h1>"

    pagina += "<table>"
    pagina += "<tr>"
    pagina += "<th>Fator</th>"
    pagina += "<th> </th>"
    pagina += "<th>Fator</th>"
    pagina += "<th> </th>"
    pagina += "<th>Produto</th>"
    pagina += "</tr>"

    for i in range(0, 11):
        pagina += "<tr>"
        pagina += "<td>" + str(i) + "</td>"
        pagina += "<td>X</td>"
        pagina += "<td>" + str(numero) + "</td>"
        pagina += "<td>=</td>"
        pagina += "<td>" + str(i * numero) + "</td>"
        pagina += "</tr>"

    pagina += "</table>"

    pagina += "<style>"
    pagina += "table, th, td {border: 1px solid black;border-collapse: collapse;}"
    pagina += "th, td {text-align: center;}"
    pagina += "</style>"
    return HttpResponse(pagina)


# Renderização de um template, a função render já retorna um objeto HttpResponse
def template(request, numero):

    return render(request, 'tabuada/tabuada.html', {
        'numero' : numero,
        'range': range(0, 11)
    })

def template2(request, numero, vezes):
    return render(request, 'tabuada/tabuada.html', {
        'numero' : numero,
        'range': range(0, vezes+1),
        'vezes': vezes
    })