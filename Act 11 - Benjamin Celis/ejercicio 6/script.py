"""
6. De un operario se conoce su sueldo y los años de antigüedad. Se pide
confeccionar un programa que lea los datos de entrada e informe:
a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
años, otorgarle un aumento de 5 %.
c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
cambios.
"""

sueldo = int(input("Ingrese sueldo del operario....:"))
años = int(input("Ingrese los años de antiguedad"))
aumento1 = sueldo * 1.20
aumento2 = sueldo * 1.05
if sueldo < 500 and años > 9:
    print(f"El aumento que usted recibira a su sueldo es de: {aumento1}")
elif sueldo < 500 and años < 10:
    print(f"El sueldo que usted recibira sera de {aumento2}")
else:
    print(f"Su sueldo es {sueldo}")
    