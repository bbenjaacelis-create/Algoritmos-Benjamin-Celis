function cargarDatos() {
    let equipos = [];
    let puntos = [];
    let diferenciaGol = [];
    
    let cant = parseInt(prompt("Ingrese la cantidad de equipos:"));
    for (let i = 0; i < cant; i++) {
        let eq = prompt("Nombre del equipo:");
        let pts = parseInt(prompt("Puntos:"));
        let df = parseInt(prompt("Diferencia de gol:"));
        
        equipos.push(eq);
        puntos.push(pts);
        diferenciaGol.push(df);
    }
    
    return { equipos: equipos, puntos: puntos, diferenciaGol: diferenciaGol };
}

function ordenarTabla(equipos, puntos, diferenciaGol) {
    let n = equipos.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - 1 - i; j++) {
            if (puntos[j] < puntos[j + 1] || (puntos[j] === puntos[j + 1] && diferenciaGol[j] < diferenciaGol[j + 1])) {
                let auxEq = equipos[j];
                equipos[j] = equipos[j + 1];
                equipos[j + 1] = auxEq;
                
                let auxPts = puntos[j];
                puntos[j] = puntos[j + 1];
                puntos[j + 1] = auxPts;
                
                let auxDf = diferenciaGol[j];
                diferenciaGol[j] = diferenciaGol[j + 1];
                diferenciaGol[j + 1] = auxDf;
            }
        }
    }
}

function mostrarTabla(equipos, puntos, diferenciaGol) {
    let resultado = "Salida Esperada: ";
    for (let i = 0; i < equipos.length; i++) {
        let posicion = (i + 1) + "° " + equipos[i] + " (" + puntos[i] + " pts";
        
        let empates = 0;
        for (let j = 0; j < equipos.length; j++) {
            if (i !== j && puntos[i] === puntos[j]) {
                empates = empates + 1;
            }
        }
        
        if (empates > 0) {
            posicion = posicion + ", DG " + diferenciaGol[i];
        }
        
        posicion = posicion + ")";
        
        if (i < equipos.length - 1) {
            posicion = posicion + ", ";
        }
        
        resultado = resultado + posicion;
    }
    
    console.log(resultado + ".");
}

// --- PROGRAMA PRINCIPAL ---
let datos = cargarDatos();
ordenarTabla(datos.equipos, datos.puntos, datos.diferenciaGol);
mostrarTabla(datos.equipos, datos.puntos, datos.diferenciaGol);