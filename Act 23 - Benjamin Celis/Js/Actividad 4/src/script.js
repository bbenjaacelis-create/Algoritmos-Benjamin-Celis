/*
Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot;
*/ 
function cargarTexto() {
    return prompt("Ingrese el texto a comprimir:");
}

function comprimirRLE(texto) {
    if (texto.length === 0) {
        return "";
    }
    
    let comprimido = "";
    let caracterActual = texto[0];
    let contador = 1;
    
    for (let i = 1; i < texto.length; i++) {
        if (texto[i] === caracterActual) {
            contador = contador + 1;
        } else {
            comprimido = comprimido + caracterActual + contador;
            caracterActual = texto[i];
            contador = 1;
        }
    }
    
    comprimido = comprimido + caracterActual + contador;
    return comprimido;
}

function mostrarResultado(resultado) {
    console.log('Salida Esperada: "' + resultado + '"');
}

// --- PROGRAMA PRINCIPAL ---
let cadena = cargarTexto();
let resultadoComprimido = comprimirRLE(cadena);
mostrarResultado(resultadoComprimido);