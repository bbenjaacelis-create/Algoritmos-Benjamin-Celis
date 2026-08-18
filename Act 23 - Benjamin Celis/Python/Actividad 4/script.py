"""
Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: "AAABBCDDDD" Salida Esperada: "A3B2C1D4"
"""
def cargar_texto():
    return input("Ingrese el texto a comprimir: ")

def comprimir_rle(texto):
    if len(texto) == 0:
        return ""
    
    comprimido = ""
    caracter_actual = texto[0]
    contador = 1
    
    for i in range(1, len(texto)):
        if texto[i] == caracter_actual:
            contador = contador + 1
        else:
            comprimido = f"{comprimido}{caracter_actual}{contador}"
            caracter_actual = texto[i]
            contador = 1
            
    comprimido = f"{comprimido}{caracter_actual}{contador}"
    return comprimido

def mostrar_resultado(resultado):
    print(f'Salida Esperada: "{resultado}"')


cadena = cargar_texto()
resultado_comprimido = comprimir_rle(cadena)
mostrar_resultado(resultado_comprimido)