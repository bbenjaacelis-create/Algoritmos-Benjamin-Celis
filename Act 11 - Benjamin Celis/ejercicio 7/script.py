"""
7. Escribir un programa en el cual: dada una lista de tres valores numéricos
distintos se calcule e informe su rango de variación (debe mostrar el mayor
y el menor de ellos)
"""
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
num3=int(input("ingrese el tercer numero: "))

if num1>num2 and num2>num3:

    variacion1= num1-num2
    variacion1=int(variacion1)
   
    variacion2= num2-num3
    variacion2=int(variacion2)

    print(f"variacion entre el primer y segundo numero: {variacion1}")
    print(f"variacion entre el segundo y tercer numero: {variacion2}")
    print(f"numero menor: {num3}")
    print(f"numero mayor: {num1}")

elif num1<num2 and num2<num3:

    variacion1= num2-num1
    variacion1=int(variacion1)
   
    variacion2= num3-num2
    variacion2=int(variacion2)

    print(f"variacion entre el primer y segundo numero: {variacion1}")
    print(f"variacion entre el segundo y tercer numero: {variacion2}")
    print(f"numero menor: {num1}")
    print(f"numero mayor: {num3}")

elif num1<num2 and num2>num3 and num1>num3:

    variacion1= num2-num1
    variacion1=int(variacion1)
   
    variacion2= num2-num3
    variacion2=int(variacion2)

    print(f"variacion entre el primer y segundo numero: {variacion1}")
    print(f"variacion entre el segundo y tercer numero: {variacion2}")
    print(f"numero menor: {num3}")
    print(f"numero mayor: {num2}")

elif num1<num2 and num2>num3 and num1<num3:

    variacion1= num2-num1
    variacion1=int(variacion1)
   
    variacion2= num2-num3
    variacion2=int(variacion2)

    print(f"variacion entre el primer y segundo numero: {variacion1}")
    print(f"variacion entre el segundo y tercer numero: {variacion2}")
    print(f"numero menor: {num1}")
    print(f"numero mayor: {num2}")