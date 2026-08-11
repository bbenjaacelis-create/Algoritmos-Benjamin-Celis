/*
Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[[&quot;Paciente&quot;, Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [[&quot;Carlos&quot;, 1], [&quot;Ana&quot;, 3], [&quot;Roberto&quot;, 2], [&quot;Lucía&quot;, 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3).
*/ 
function cargarPacientes() {
    let colaEspera = [];
    let cant = parseInt(prompt("Ingrese la cantidad de pacientes en espera:"));
    
    for (let i = 0; i < cant; i++) {
        let nombre = prompt("Nombre del paciente:");
        let prioridad = parseInt(prompt("Prioridad (1=Normal, 2=Moderado, 3=Critico):"));
        colaEspera.push([nombre, prioridad]);
    }
    
    return colaEspera;
}

function atenderSiguiente(colaEspera) {
    if (colaEspera.length === 0) {
        console.log("No hay pacientes en la cola de espera.");
        return;
    }
    
    let posicionMaxima = 0;
    let maximaPrioridad = colaEspera[0][1];
    
    for (let i = 1; i < colaEspera.length; i++) {
        if (colaEspera[i][1] > maximaPrioridad) {
            maximaPrioridad = colaEspera[i][1];
            posicionMaxima = i;
        }
    }
    
    let paciente = colaEspera.splice(posicionMaxima, 1)[0];
    
    console.log("Atiende a " + paciente[0] + " (Nivel " + paciente[1] + ")");
}

let cola = cargarPacientes();

console.log("--- Atendiendo pacientes ---");
let cantAAtender = cola.length;
for (let i = 0; i < cantAAtender; i++) {
    atenderSiguiente(cola);
}