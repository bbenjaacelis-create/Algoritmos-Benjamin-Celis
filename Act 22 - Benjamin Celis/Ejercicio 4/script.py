"""
4-Un observatorio astronómico registra los descubrimientos de nuevos planetas
fuera del sistema solar.
 Diseñar un diccionario donde la Clave sea el nombre científico del
exoplaneta (ej: "Kepler-22b") y el Valor sea una tupla con sus datos:
(distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
Desarrollar las siguientes funciones:
1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
descubiertos.
2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
(utilizando el operador in), mostrar todos sus detalles físicos y si reúne
condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
"El exoplaneta no figura en el catálogo actual".
3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
exoplanetas cargados que fueron marcados como habitables.
"""


def carga():
    lista={}
    for x in range (4):
        nombre=str(input(f"ingrese el planeta N° {x+1}: "))
        clave=str(input("ingrese su nombre cientifico: "))
        dist=int(input("ingrese su distancia a años luz: "))
        atmos=str(input("ingrese su tipo de atmosfera: "))
        esHab=str(input("es habitable? (si/no): "))
        lista[clave]=(nombre, dist, atmos, esHab)

        

    return lista

def entera(lista):
    print("LISTA COMPLETA: ")
    print(lista)



def consulta(lista):
    variable="s"
    while variable=="s":
        valor=str(input("ingrese el nombre cientifico del planeta: "))
        if valor in lista:
            print(lista[valor])    
            variable=input("desea buscar otro exoplaneta? (s/n): ")
        
        else:
            print("el exoplaneta no figura en el catagolo actual.")


def busqueda():
    lista2=[]
    for clave in lista:
        if "si" in lista[clave]:
            lista2.append(lista[clave][0])
    
    print("Exoplanetas habitables: ")
    print(lista2)

    return lista2


lista=carga()
entera(lista)
consulta(lista)
busqueda()