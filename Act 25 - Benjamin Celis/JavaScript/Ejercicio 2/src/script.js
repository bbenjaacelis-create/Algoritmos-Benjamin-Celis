/*
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).
*/
function cargarCoordenadas() {
    let camaras = [];
    for (let i = 0; i < 4; i++) {
        let lat = parseFloat(prompt("Ingrese la latitud de la camara " + (i + 1) + ":"));
        let lon = parseFloat(prompt("Ingrese la longitud de la camara " + (i + 1) + ":"));
        camaras.push([lat, lon]);
    }
    return camaras;
}

function listarPosiciones(camaras) {
    console.log("--- POSICIONES DE LAS CAMARAS ---");
    let i = 1;
    for (let [lat, lon] of camaras) {
        console.log("Camara " + i + ": Latitud " + lat + ", Longitud " + lon);
        i = i + 1;
    }
}

function contarHemisferioNorte(camaras) {
    let contador = 0;
    for (let [lat, lon] of camaras) {
        if (lat > 0) {
            contador = contador + 1;
        }
    }
    return contador;
}

function mostrarReporteHemisferio(cantidadNorte) {
    console.log("--- REPORTE DE HEMISFERIO ---");
    console.log("Cantidad de camaras en el hemisferio norte: " + cantidadNorte);
}

let listaCamaras = cargarCoordenadas();
listarPosiciones(listaCamaras);
let norteCant = contarHemisferioNorte(listaCamaras);
mostrarReporteHemisferio(norteCant);