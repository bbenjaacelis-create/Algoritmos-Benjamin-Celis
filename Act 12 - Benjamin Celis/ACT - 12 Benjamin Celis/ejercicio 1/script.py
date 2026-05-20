"""
1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
aprobados = 0
des = 0
for f in range(1,11):
    n=int(input("Ingrese notas"))
    if n >= 7:
        aprobados= aprobados + 1
    else:
        des = des + 1
print(f"Los alumnos con mayores a 7 {aprobados}")
print(f"Menores a 7: {des}")