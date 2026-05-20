"""
5. Realizar un programa que lea los lados de n triángulos, e informar:
a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b. Cantidad de triángulos de cada tipo.
"""
equi = 0
iso = 0
esc = 0
o = int(input("Cuantos queres ingresar?"))

for a in range(1, o+1):
    lado1=int(input("Ingrese los lado 1: "))
    lado2=int(input("Ingrese los lado 2: "))
    lado3=int(input("Ingrese los lado 3: "))

    if lado1==lado2 and lado2==lado3 and lado1==lado3:
        print("su triangulo es equilatero: ") 
        equi = equi + 1
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("su triangulo es isoceles")
        iso = iso + 1
    elif lado1!=lado2 or lado3!=lado2 or lado1!=lado3:
        print("su triangulo es escaleno")
        esc = esc + 1
print(f"Cantidad de triangulos equilateros {equi}")
print(f"Cantidad de triangulos isoceles {iso}")
print(f"Cantidad de triangulos escalenos {esc}")
