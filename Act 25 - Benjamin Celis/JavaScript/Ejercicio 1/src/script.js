/*
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
*/ 
function cargarTemperaturas() {
    let temperaturas = [];
    for (let i = 0; i < 6; i++) {
        let temp = parseFloat(prompt("Ingrese la temperatura de la hora " + (i + 1) + ":"));
        temperaturas.push(temp);
    }
    return temperaturas;
}

function procesarExtremos(temperaturas) {
    let maxima = temperaturas[0];
    let minima = temperaturas[0];
    
    for (let i = 1; i < temperaturas.length; i++) {
        if (temperaturas[i] > maxima) {
            maxima = temperaturas[i];
        }
        if (temperaturas[i] < minima) {
            minima = temperaturas[i];
        }
    }
    
    return [maxima, minima];
}


let listaTemps = cargarTemperaturas();
let extremos = procesarExtremos(listaTemps);
let maxima = extremos[0];
let minima = extremos[1];

console.log("La temperatura maxima registrada fue de " + maxima + " grados.");
console.log("La temperatura minima registrada fue de " + minima + " grados.");