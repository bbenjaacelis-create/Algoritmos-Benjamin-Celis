/*
Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato &quot;ID:TIPO:MONTO&quot;, donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
&quot;sospechosas&quot;. Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: &quot;TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000&quot; Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: [&#39;TX103&#39;]
*/ 
function cargarTransacciones() {
    return prompt("Ingrese el lote de transacciones:");
}

function procesarTransacciones(cadenaTexto) {
    let balance = 0;
    let sospechosas = [];
    
    let transacciones = cadenaTexto.split(",");
    
    for (let i = 0; i < transacciones.length; i++) {
        let partes = transacciones[i].trim().split(":");
        let idTx = partes[0];
        let tipo = partes[1];
        let monto = parseFloat(partes[2]);
        
        if (tipo === "I") {
            balance += monto;
        } else if (tipo === "E") {
            balance -= monto;
            if (monto > 50000) {
                sospechosas.push(idTx);
            }
        }
    }
    
    console.log("Balance final: $" + balance);
    console.log("Transacciones sospechosas: [" + sospechosas + "]");
}

// --- PROGRAMA PRINCIPAL ---
let textoIngresado = cargarTransacciones();
procesarTransacciones(textoIngresado);