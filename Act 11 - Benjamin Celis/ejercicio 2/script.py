#2. Calcular el sueldo mensual de un operario conociendo la cantidad de horas
#trabajadas y el valor por hora.

horas = int(input("Ingrese la cantidad de horas trabajadas del operario"))
valor = int(input("Ingrese el valor por horas"))
sueldo = horas * valor * 30
print(f"sueldo mensual es: {sueldo}")