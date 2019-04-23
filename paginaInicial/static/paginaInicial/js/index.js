function toTabuadaGerada() {
    let valor = document.getElementById("tabuadaGerada").value
    if (valor) {
        location.href=`tabuada/gerado/${valor}`
    }
}

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

function toTarefas() {
    location.href = "tarefas"
}