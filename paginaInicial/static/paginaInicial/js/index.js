// Redireciona para a pagina da tabuada gerada
function toTabuadaGerada() {
    let valor = document.getElementById("tabuadaGerada").value
    if (valor) {
        location.href=`tabuada/gerado/${valor}`
    }
}

// Redireciona para a pagina com template
function toTabuadaTemplate() {
    let valor = document.getElementById("tabuadaTemplate").value
    let vezes = document.getElementById("tabuadaTemplateVezes").value

    if (valor) {
        let url = `tabuada/template/${valor}`
        if (vezes) {
            url += `/${vezes}`
        }

        location.href = url
    }

}

// Redireciona para a pagina de tarefas
function toTarefas() {
    location.href = "tarefas"
}