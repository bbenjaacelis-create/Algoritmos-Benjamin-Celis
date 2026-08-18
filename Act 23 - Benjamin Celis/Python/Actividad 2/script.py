"""
Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato "ID:TIPO:MONTO", donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
"sospechosas". Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: "TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000" Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: ['TX103']
"""

def procesar_transacciones():
    
    num=int(input("cuantas veces desea ingresar datos?:"))
    for x in num:
        id=int(input("ingrese el id del movimiento: "))
        tipo=input("ingrese el tipo (I/E): ")
        monto=int(input("ingrese el monto: "))

        print(f"{id}:{tipo}:{monto}")

        if tipo == "I":
            suma= suma + monto

        elif tipo == "E":
            suma= suma - monto

        if tipo == "E" and monto > 50000:
            lista.append (id)

    print(f"Balance final: ${suma}")
    print(f"Transacciones sospechosas: {lista}")
    
lista=[]

procesar_transacciones()