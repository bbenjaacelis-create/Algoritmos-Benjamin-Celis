function cargarNotaGuardada() {
    let notaGuardada = sessionStorage.getItem("notaTemporal");

    if (notaGuardada !== null) {
        document.getElementById("resultado").textContent = notaGuardada;
    } else {
        document.getElementById("resultado").textContent = "";
    }
}

function guardarNota() {
    let texto = document.getElementById("nota").value;

    if (texto !== "") {
        sessionStorage.setItem("notaTemporal", texto);
        document.getElementById("resultado").textContent = texto;
        document.getElementById("nota").value = "";
    }
}

function borrarNota() {
    sessionStorage.removeItem("notaTemporal");
    document.getElementById("resultado").textContent = "";
    document.getElementById("nota").value = "";
}

cargarNotaGuardada();