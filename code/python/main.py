def mostrar_menu():
    print("Calculadora en Python")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def calcular(operacion, num1, num2):
    if operacion == "1":
        return num1 + num2
    elif operacion == "2":
        return num1 - num2
    elif operacion == "3":
        return num1 * num2
    elif operacion == "4":
        return num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        return "Opción inválida"


while True:

    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = calcular(opcion, num1, num2)
    print(f"Resultado: {resultado}\n")
