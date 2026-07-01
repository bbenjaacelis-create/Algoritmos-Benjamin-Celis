"""
1-Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar():
    lista={}
    for x in range (4):
        documento=int(input("ingrese el documento de la persona: "))
        nombre=str(input("ingrese su nombre: "))
        lista[documento]=nombre

    return lista
   

def ingreso(lista):
    print("TODOS LOS DATOS INGRESADOS: ")
    print(lista)


def consulta(lista):
    valor=int(input("ingrese el numero de documento: "))
    if valor in lista:
        print(lista[valor])



lista=cargar()
ingreso(lista)
consulta(lista)