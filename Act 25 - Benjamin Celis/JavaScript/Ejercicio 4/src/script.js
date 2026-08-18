/*
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
*/
function cargarInventario() {
    let inventario = [];
    for (let i = 0; i < 5; i++) {
        let nombre = prompt("Ingrese el nombre del articulo " + (i + 1) + ":");
        let precio = parseFloat(prompt("Ingrese el precio de " + nombre + ":"));
        let stock = parseInt(prompt("Ingrese el stock de " + nombre + ":"));
        inventario.push([nombre, precio, stock]);
    }
    return inventario;
}

function imprimirListado(inventario) {
    console.log("--- LISTADO DE COMPONENTES ---");
    for (let [nombre, precio, stock] of inventario) {
        console.log("Articulo: " + nombre + " | Precio: $" + precio + " | Stock: " + stock + " unidades");
    }
}

function calcularValorInventario(inventario) {
    let total = 0.0;
    for (let [nombre, precio, stock] of inventario) {
        total = total + (precio * stock);
    }
    return total;
}

function obtenerAlertasReposicion(inventario) {
    let articulosBajos = [];
    for (let [nombre, precio, stock] of inventario) {
        if (stock <= 10) {
            articulosBajos.push(nombre);
        }
    }
    return articulosBajos;
}

function mostrarValorTotal(valorTotal) {
    console.log("--- VALOR TOTAL DEL INVENTARIO ---");
    console.log("El valor total de la mercaderia es: $" + valorTotal);
}

function mostrarAlertas(alertas) {
    console.log("--- ALERTA DE REPOSICION (URGENTE) ---");
    if (alertas.length === 0) {
        console.log("No hay articulos con necesidad urgente de reposicion.");
    } else {
        for (let i = 0; i < alertas.length; i++) {
            console.log("AVISO: Stock bajo (<= 10 unidades) en articulo: " + alertas[i]);
        }
    }
}


let inventario = cargarInventario();
imprimirListado(inventario);
let valorTotal = calcularValorInventario(inventario);
mostrarValorTotal(valorTotal);
let alertas = obtenerAlertasReposicion(inventario);
mostrarAlertas(alertas);