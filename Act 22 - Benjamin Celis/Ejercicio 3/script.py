"""
3-Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
-Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: "192.168.1.50") y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).
"""



def cargar():
    lista={}

    for x in range (4):
        direccion=input("ingrese una direccion IP: ")
        nombre_del_dispositivo=str(input("ingrese el nombre del dispositivo: "))
        cantidad_intentos_fallidos=int(input(f"cuantos intentos fallidos lleva?: "))
        lista[direccion]=(nombre_del_dispositivo, cantidad_intentos_fallidos)

    return lista

def imprimir(lista):
    print("SE REGISTRÓ: ")
    for direccion in lista:
        print(direccion, lista[direccion])


def bloqueo(lista):
    for direccion in lista:
        if lista[direccion][1] > 5:
            print(f"{lista[direccion][0]} FUE BLOQUEADO POR LLEVAR MAS DE 5 INTENTOS FALLIDOS") 





lista=cargar()
imprimir(lista)
bloqueo(lista)