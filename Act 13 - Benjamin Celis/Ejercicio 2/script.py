"""
2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada
cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe
finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un
programa que lea los datos de las cuentas corrientes e informe:
● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo,
sabiendo que:
○ Estado de la cuenta:
○ “Acreedor” si el saldo es > 0.
○ “Deudor” si el saldo es < 0.
○ “Nulo” si el saldo es = 0.
● b) La suma total de los saldos acreedores.
"""
sumaacredor = 0

n=int(input("Ingrese el numero de cuenta (negativo para terminar la operacion!!!!)"))
while n >= 0:
    o = float(input("Ingrese: "))

    if o > 0:
        estado = "Acreedor"
        sumaacredor = sumaacredor + o
    elif o < 0:
        estado = "Deudor"
    else:
        estado = "Nulo"
    print(f"La cuenta n° {n} es {estado}")
    n=int(input("Ingrese el numero de cuenta (negativo para terminar la operacion!!!!)"))
print("LA SUMA DE LOS DATOS ACREEDORES ES: ")
print(sumaacredor)