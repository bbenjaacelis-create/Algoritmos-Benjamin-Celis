"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""

def contar_letras_a(texto):
    contador = 0
    texto_minuscula = texto.lower() 
    
    for letra in texto_minuscula:
        if letra == 'a':
            contador += 1    
    return contador 
def solicitar_frase():
    print("Captura de Texto")
    frase = input("Ingrese una palabra o frase para analizar: ")
    return frase
def mostrar_resultado(total):
    print("Resultado del Análisis")
    print(f"La cantidad total de letras 'a' o 'A' encontradas es: {total}")

texto_usuario = solicitar_frase()
cantidad_letras = contar_letras_a(texto_usuario)
mostrar_resultado(cantidad_letras)