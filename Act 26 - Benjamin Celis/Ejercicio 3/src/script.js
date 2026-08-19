/*
Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”.
*/
let votosAriel = 0;
let votosLuciano = 0;
let votosVictor = 0;

function votos(candidato) {
    if (candidato === "Ariel Ledezma") {
        votosAriel = votosAriel + 1;
        document.getElementById("votos-ariel").textContent = votosAriel;
    } else if (candidato === "Luciano Frisancho") {
        votosLuciano = votosLuciano + 1;
        document.getElementById("votos-luciano").textContent = votosLuciano;
    } else if (candidato === "Victor Alvarez") {
        votosVictor = votosVictor + 1;
        document.getElementById("votos-victor").textContent = votosVictor;
    }

    verificarGanador();
}

function verificarGanador() {
    if (votosAriel > votosLuciano && votosAriel > votosVictor) {
        console.log("Va ganando: Ariel Ledezma");
    } else if (votosLuciano > votosAriel && votosLuciano > votosVictor) {
        console.log("Va ganando: Luciano Frisancho");
    } else if (votosVictor > votosAriel && votosVictor > votosLuciano) {
        console.log("Va ganando: Victor Alvarez");
    } else {
        console.log("Hay un empate");
    }
}