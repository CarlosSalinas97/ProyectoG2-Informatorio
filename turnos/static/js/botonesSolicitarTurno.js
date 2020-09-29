function mostrar1(){
    document.getElementById("id_invitado1").disabled = false
    document.getElementById("-1").style.display = ""
    document.getElementById("-2").style.display = "none"
    document.getElementById("-3").style.display = "none"
    document.getElementById("+1").style.display = "none"
    document.getElementById("+2").style.display = ""
    document.getElementById("+3").style.display = "none"
}
function mostrar2(){
    document.getElementById("id_invitado2").disabled = false
    document.getElementById("-1").style.display = "none"
    document.getElementById("-2").style.display = ""
    document.getElementById("-3").style.display = "none"
    document.getElementById("+1").style.display = "none"
    document.getElementById("+2").style.display = "none"
    document.getElementById("+3").style.display = ""
}
function mostrar3(){
    document.getElementById("id_invitado3").disabled = false
    document.getElementById("-1").style.display = "none"
    document.getElementById("-2").style.display = "none"
    document.getElementById("-3").style.display = ""
    document.getElementById("+1").style.display = "none"
    document.getElementById("+2").style.display = "none"
    document.getElementById("+3").style.display = "none"
}
function esconder1(){
    document.getElementById("id_invitado1").disabled = true
    document.getElementById("id_invitado1").value = ""
    document.getElementById("-1").style.display = "none"
    document.getElementById("-2").style.display = "none"
    document.getElementById("-3").style.display = "none"
    document.getElementById("+1").style.display = ""
    document.getElementById("+2").style.display = "none"
    document.getElementById("+3").style.display = "none"
}
function esconder2(){
    document.getElementById("id_invitado2").disabled = true
    document.getElementById("id_invitado2").value = ""
    document.getElementById("-1").style.display = ""
    document.getElementById("-2").style.display = "none"
    document.getElementById("-3").style.display = "none"
    document.getElementById("+1").style.display = "none"
    document.getElementById("+2").style.display = ""
    document.getElementById("+3").style.display = "none"
    
}
function esconder3(){
    document.getElementById("id_invitado3").disabled = true
    document.getElementById("id_invitado3").value = ""
    document.getElementById("-1").style.display = "none"
    document.getElementById("-2").style.display = ""
    document.getElementById("-3").style.display = "none"
    document.getElementById("+1").style.display = "none"
    document.getElementById("+2").style.display = "none"
    document.getElementById("+3").style.display = ""
}