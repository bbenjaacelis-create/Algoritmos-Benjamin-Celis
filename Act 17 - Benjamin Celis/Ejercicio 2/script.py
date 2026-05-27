"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""
paises=[]
temperatura = []
for x in range(4):
    pais=input(f"Ingrese el pais N°{x+1}: ")
    paises.append(pais)
    temp1=float(input(f"Ingrese las temperaturas mens 1 de {pais}...: "))
    temp2=float(input(f"Ingrese las temperaturas mens 2 de {pais}...: "))
    temp3=float(input(f"Ingrese las temperaturas mens 3 de {pais}...: "))
    temperatura.append([temp1, temp2, temp3])
print("Temperaturas Mensuales")
for x in range(4):
     print(paises[x], ":", temperatura[x][0], temperatura[x][1], temperatura[x][2])
print("Temperatura media trimestral")
media=[]
for x in range(4):
     promedio=(temperatura[x][0] + temperatura[x][1] +  temperatura[x][2]) / 3
     media.append(promedio)
     print(paises[x], ":", promedio)
paismediamayor = paises[0]
mayor = media[0]

for x in range(1, 4):
    if media[x] > mayor:
        mayor = media[x]
        paismediamayor = paises[x]  

print(f"El pais con mejor media es {paismediamayor}, con la media de {mayor}")