num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
print("[s] Sumar a + b")
print("[m] Multiplicar a * b")
print("[d] Dividir a / b")
print("[r] Restar a - b")
operacion = input("ingrese una operación: ")

match operacion:
    case "s":
        print("Resultado: ", (num1 + num2))
    case "m":
        print("Resultado: ", (num1 * num2))
    case "d":
        print("Resultado: ", (num1 / num2))
    case "r":
        print("Resultado: ", (num1 - num2))
    case _:
        print("Operación no valida")



