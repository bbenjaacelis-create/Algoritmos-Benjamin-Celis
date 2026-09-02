/*
1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no.
*/
function confirmar(){
    if (document.getElementById("radio1").checked){
        alert("Usted es mayor de 18, puede seguir")
    }
    if (document.getElementById("radio2").checked){
        alert("Usted es menor de 18 años, salga de la pagina")
    }
}