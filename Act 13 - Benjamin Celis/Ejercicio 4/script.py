"""
4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
puntos a procesar.
"""

q1 = 0
q2 = 0
q3 = 0
q4 = 0

n = int(input("¿Cuántos puntos querés ingresar? "))

for i in range(1, n + 1):
    x = float(input(f"Punto {i} - Ingrese X: "))
    y = float(input(f"Punto {i} - Ingrese Y: "))

    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print(f"Puntos en el 1° cuadrante: {q1}")
print(f"Puntos en el 2° cuadrante: {q2}")
print(f"Puntos en el 3° cuadrante: {q3}")
print(f"Puntos en el 4° cuadrante: {q4}")