/*
Ejercicio 2: Carrito de Compras con Conteo de Productos
Enunciado: Crear un carrito de compras utilizando LocalStorage, que permita a los
usuarios agregar productos y muestre la cantidad total de productos en el carrito.
1. Los productos deben tener un botón para agregar al carrito.
2. Al agregar un producto, se debe mostrar el número total de productos en el
carrito, almacenándolo en LocalStorage.
3. Al recargar la página, el número total de productos debe recuperarse de
LocalStorage y mostrarse correctamente.
*/
function cargarCarrito() {
    let cantidadGuardada = localStorage.getItem("cantidadCarrito");

    if (cantidadGuardada !== null) {
        document.getElementById("contador").textContent = cantidadGuardada;
    } else {
        document.getElementById("contador").textContent = 0;
    }
}

function agregarAlCarrito() {
    let cantidadActual = localStorage.getItem("cantidadCarrito");

    if (cantidadActual === null) {
        cantidadActual = 0;
    } else {
        cantidadActual = parseInt(cantidadActual);
    }

    let nuevaCantidad = cantidadActual + 1;
    localStorage.setItem("cantidadCarrito", nuevaCantidad);

    document.getElementById("contador").textContent = nuevaCantidad;
}

cargarCarrito();