"""
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""
def cargar():
    candidatosyvotos=[]
    for x in range(3):
        c=input(f"Ingrese el nombre del {x+1}° candidato: ")
        p=input(f"Ingrese el nombre de la provincia para cargar los votos de {c}: ")
        v=int(input(f"Ingrese los votos de {c}, en {p}: "))
        lista_prov = [(p,v)]
        candidatosyvotos.append([c,lista_prov])
    return candidatosyvotos
def imprimir(candidatosyvotos):
    print("Candidatos, Provincias Y Sus Votos")
    nombre,provincia,voto=candidatosyvotos
    print(f"{nombre}, {provincia}, {voto}")

messi=cargar()
imprimir(messi)