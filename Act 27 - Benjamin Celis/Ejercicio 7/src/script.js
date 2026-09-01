/*
7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.
*/
function obtenerDeportesSeleccionados() {
    let deportes = "";

    let chkFutbol = document.getElementById("futbol");
    let chkBasquet = document.getElementById("basquet");
    let chkTenis = document.getElementById("tenis");

    if (chkFutbol.checked) {
        deportes = deportes + "Futbol ";
    }

    if (chkBasquet.checked) {
        deportes = deportes + "Basquet ";
    }

    if (chkTenis.checked) {
        deportes = deportes + "Tenis ";
    }

    return deportes;
}

function mostrarDeportes(deportes) {
    let parrafo = document.getElementById("resultado");

    if (deportes !== "") {
        parrafo.textContent = "Deportes seleccionados: " + deportes;
    } else {
        parrafo.textContent = "No selecciono ningun deporte.";
    }
}

function procesarDeportes() {
    let seleccion = obtenerDeportesSeleccionados();
    mostrarDeportes(seleccion);
}