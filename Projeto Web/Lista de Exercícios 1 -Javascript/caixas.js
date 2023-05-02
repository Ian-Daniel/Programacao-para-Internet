
function nomear(){
    var a = window.confirm("Posso saber qual o seu nome?")
    if (a == true){
        var nome = window.prompt("Qual o seu nome?")
        alert("Seja bem vindo(a) "+nome+"!")
    }
    else{
            alert("Você respondeu que não. Que pena! Bye bye!")
        }
}