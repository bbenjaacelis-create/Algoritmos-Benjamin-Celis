/*
Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.
*/ 

function mostrarSala(sala) {
    console.log("[");
    for (let i = 0; i < sala.length; i++) {
        let filaTexto = "  [";
        for (let j = 0; j < sala[i].length; j++) {
            filaTexto = filaTexto + sala[i][j];
            if (j < sala[i].length - 1) {
                filaTexto = filaTexto + ", ";
            }
        }
        filaTexto = filaTexto + "],";
        console.log(filaTexto);
    }
    console.log("]");
}

function reservarConsecutivos(sala, fila, cantidad) {
    let columnasFila = sala[fila].length;
    let libresSeguidos = 0;
    let colInicio = -1;
    let col = 0;
    
    while (col < columnasFila && libresSeguidos < cantidad) {
        if (sala[fila][col] === 0) {
            if (libresSeguidos === 0) {
                colInicio = col;
            }
            libresSeguidos++;
        } else {
            libresSeguidos = 0;
        }
        col++;
    }
    
    if (libresSeguidos === cantidad) {
        let columnasReservadas = [];
        for (let c = colInicio; c < colInicio + cantidad; c++) {
            sala[fila][c] = 1;
            columnasReservadas.push(c);
        }
        console.log("Reserva exitosa en la fila " + fila + ". Columnas asignadas: " + columnasReservadas);
    } else {
        console.log("No fue posible realizar la reserva: no hay " + cantidad + " asientos consecutivos libres.");
    }
}

function cargarSala() {
    let filas = parseInt(prompt("Ingrese cantidad de filas de la sala:"));
    let cols = parseInt(prompt("Ingrese cantidad de columnas de la sala:"));
    
    let sala = [];
    for (let i = 0; i < filas; i++) {
        let filaActual = [];
        for (let j = 0; j < cols; j++) {
            let estado = parseInt(prompt("Estado asiento [Fila " + i + ", Columna " + j + "] (0=Libre, 1=Ocupado):"));
            filaActual.push(estado);
        }
        sala.push(filaActual);
    }
    return sala;
}

// --- PROGRAMA PRINCIPAL ---
let sala = cargarSala();

console.log("Sala inicial cargada:");
mostrarSala(sala);

let fDeseada = parseInt(prompt("Ingrese la fila donde desea reservar:"));
let cantDeseada = parseInt(prompt("Ingrese la cantidad de asientos a reservar:"));

reservarConsecutivos(sala, fDeseada, cantDeseada);

console.log("Estado final de la sala:");
mostrarSala(sala);