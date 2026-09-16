/*
Ejercicio 1: Guardar Preferencias de Usuario
Enunciado: Crear una función que guarde y recupere las preferencias de un usuario,
como su nombre y el color de fondo preferido, utilizando LocalStorage.
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente (mostrar el nombre del usuario y
cambiar el color de fondo).
*/
function cargarPreferencias() {
    let nombreGuardado = localStorage.getItem("nombreUsuario");
    let colorGuardado = localStorage.getItem("colorFondo");

    if (nombreGuardado !== null) {
        document.getElementById("mensaje").textContent = "Bienvenido, " + nombreGuardado;
        document.getElementById("nombre").value = nombreGuardado;
    }

    if (colorGuardado !== null) {
        document.body.style.backgroundColor = colorGuardado;
        document.getElementById("color").value = colorGuardado;
    }
}

function guardarPreferencias() {
    let nombre = document.getElementById("nombre").value;
    let color = document.getElementById("color").value;

    localStorage.setItem("nombreUsuario", nombre);
    localStorage.setItem("colorFondo", color);

    cargarPreferencias();
}

cargarPreferencias();