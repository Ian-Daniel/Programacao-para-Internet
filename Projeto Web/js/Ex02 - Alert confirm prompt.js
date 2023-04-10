function nomear(){
    var nome
    var resposta = confirm("Poderia digitar seu nome, por gentileza.")
    if (resposta == true){
        var nome = prompt("Digite seu nome completo.")
        alert("Seja bem vindo(a), "+nome+"!")
    }
    else{
        var nome = alert("Você decidiu não escrever seu nome.")
    }
}