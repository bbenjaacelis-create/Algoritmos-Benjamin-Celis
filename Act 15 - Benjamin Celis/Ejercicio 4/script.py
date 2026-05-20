"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""
l=[]
for x in range(5):
    d=int(input("Ingrese sus valores: "))
    l.append(d)
for x in range(4):
    for o in range(4):
        if l[o]<l[o+1]:
            aux=l[o]
            l[o]=l[o+1]
            l[o+1]=aux
print("---Mayor a menor---")
print(l)
for x in range(4):
    for o in range(4):
        if l[o]>l[o+1]:
            aux=l[o]
            l[o]=l[o+1]
            l[o+1]=aux
print("---Menor a mayor---")
print(l)