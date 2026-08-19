function verificar() {
    let input = document.getElementById("temperatura");
    let temp = parseFloat(input.value);
    let mensaje = document.getElementById("mensaje");

    if (temp < 10) {
        mensaje.textContent = "Hace frío";
        mensaje.style.color = "blue";
    } else if (temp >= 10 && temp <= 25) {
        mensaje.textContent = "Clima agradable";
        mensaje.style.color = "green";
    } else if (temp > 25) {
        mensaje.textContent = "Hace calor";
        mensaje.style.color = "red";
    }

    let fecha = new Date();
    console.log("Verificación realizada el: " + fecha);
}