/*
Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)
*/
function evaluarExamen() {
    let correctas = 0;
    let incorrectas = 0;

    let res1 = document.getElementById("p1").value;
    let res2 = document.getElementById("p2").value;
    let res3 = document.getElementById("p3").value;
    let res4 = document.getElementById("p4").value;
    if (res1 === "correcta") {
        correctas = correctas + 1;
    } else {
        incorrectas = incorrectas + 1;
    }
    if (res2 === "correcta") {
        correctas = correctas + 1;
    } else {
        incorrectas = incorrectas + 1;
    }
    if (res3 === "correcta") {
        correctas = correctas + 1;
    } else {
        incorrectas = incorrectas + 1;
    }
    if (res4 === "correcta") {
        correctas = correctas + 1;
    } else {
        incorrectas = incorrectas + 1;
    }

    return [correctas, incorrectas];
}

function mostrarResultados(correctas, incorrectas) {
    let parrafoResultado = document.getElementById("resultado");
    parrafoResultado.textContent = "Respuestas correctas: " + correctas + " | Respuestas incorrectas: " + incorrectas;
}

function corregirExamen() {
    let puntaje = evaluarExamen();
    let correctas = puntaje[0];
    let incorrectas = puntaje[1];
    
    mostrarResultados(correctas, incorrectas);
}