/*
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
*/
function cargarPilotos() {
    let pilotos = [];
    for (let i = 0; i < 4; i++) {
        let nombre = prompt("Ingrese el nombre del piloto " + (i + 1) + ":");
        let tiempos = [];
        for (let j = 0; j < 3; j++) {
            let tiempo = parseFloat(prompt("Ingrese el tiempo de la vuelta " + (j + 1) + " para " + nombre + " (en segundos):"));
            tiempos.push(tiempo);
        }
        pilotos.push([nombre, tiempos]);
    }
    return pilotos;
}

function calcularPromedios(pilotos) {
    let promedios = [];
    for (let i = 0; i < pilotos.length; i++) {
        let nombre = pilotos[i][0];
        let tiempos = pilotos[i][1];
        let suma = 0.0;
        for (let j = 0; j < tiempos.length; j++) {
            suma = suma + tiempos[j];
        }
        let promedio = suma / tiempos.length;
        promedios.push([nombre, promedio]);
    }
    return promedios;
}

function buscarMejorVuelta(pilotos) {
    let mejorTiempo = pilotos[0][1][0];
    let pilotoMejorVuelta = pilotos[0][0];
    
    for (let i = 0; i < pilotos.length; i++) {
        let nombre = pilotos[i][0];
        let tiempos = pilotos[i][1];
        for (let j = 0; j < tiempos.length; j++) {
            if (tiempos[j] < mejorTiempo) {
                mejorTiempo = tiempos[j];
                pilotoMejorVuelta = nombre;
            }
        }
    }
    
    return [pilotoMejorVuelta, mejorTiempo];
}

function mostrarPromedios(promedios) {
    console.log("--- TIEMPOS PROMEDIO POR PILOTO ---");
    for (let i = 0; i < promedios.length; i++) {
        console.log("Piloto: " + promedios[i][0] + " - Tiempo Promedio: " + promedios[i][1] + " segundos");
    }
}

function mostrarMejorVuelta(nombre, tiempo) {
    console.log("--- MEJOR VUELTA DE LA CLASIFICACION ---");
    console.log("La vuelta mas rapida fue de " + tiempo + " segundos, lograda por " + nombre + ".");
}


let datosPilotos = cargarPilotos();
let promediosObtenidos = calcularPromedios(datosPilotos);
mostrarPromedios(promediosObtenidos);

let mejorVuelta = buscarMejorVuelta(datosPilotos);
let pilotoRapido = mejorVuelta[0];
let tiempoRapido = mejorVuelta[1];
mostrarMejorVuelta(pilotoRapido, tiempoRapido);