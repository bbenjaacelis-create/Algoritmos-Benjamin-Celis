function mostrar() {
    let selectPizza = document.getElementById("pizza");
    let inputPrecio = document.getElementById("precio");
    
    let precioSeleccionado = selectPizza.value;
    
    if (precioSeleccionado !== "") {
        inputPrecio.value = "$" + precioSeleccionado;
    } else {
        inputPrecio.value = "";
    }
}