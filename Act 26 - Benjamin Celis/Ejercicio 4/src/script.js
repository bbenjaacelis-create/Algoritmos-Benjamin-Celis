function agregarProducto() {
    let producto = prompt("Ingrese el nombre del producto:");
    
    if (producto !== "") {
        let lista = document.getElementById("lista");
        let nuevoItem = document.createElement("li");
        
        nuevoItem.textContent = producto;
        nuevoItem.onclick = function() {
            nuevoItem.remove();
            mostrarCantidad();
        };

        lista.appendChild(nuevoItem);
        mostrarCantidad();
    }
}

function mostrarCantidad() {
    let lista = document.getElementById("lista");
    let cantidad = lista.children.length;
    console.log("Cantidad de productos: " + cantidad);
}