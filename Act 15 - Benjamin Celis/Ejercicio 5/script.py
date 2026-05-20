"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""
pais=[]
habitantes=[]

for x in range(5):
    e=input("Ingrese el nombre del pais: ")
    pais.append(e)
    d=float(input(f"Ingrese el numero de habitantes de {e}: "))  
    habitantes.append(d) 
print("Paises ordenador alfabeticamente: ") 
pais.sort()
print(pais)
for x in range(4):
    for o in range(4):
        if habitantes[o]<habitantes[o+1]:
            aux=habitantes[o]
            habitantes[o]=habitantes[o+1]
            habitantes[o+1]=aux
print("---Mayor a menor---")
print(habitantes)