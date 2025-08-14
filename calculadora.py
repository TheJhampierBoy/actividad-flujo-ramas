import math

historial = []

def mostrar_historial():
    if not historial:
        print("No hay operaciones registradas.")
    else:
        print("\n--- Historial de Operaciones ---")
        for i, op in enumerate(historial, 1):
            print(f"{i}. {op}")
        print("-------------------------------\n")

def suma(a, b):
    resultado = a + b
    historial.append(f"{a} + {b} = {resultado}")
    return resultado

def resta(a, b):
    resultado = a - b
    historial.append(f"{a} - {b} = {resultado}")
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    historial.append(f"{a} * {b} = {resultado}")
    return resultado

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    resultado = a / b
    historial.append(f"{a} / {b} = {resultado}")
    return resultado

def raiz_cuadrada(a):
    if a < 0:
        print("Error: No se puede sacar raíz cuadrada de un número negativo.")
        return None
    resultado = math.sqrt(a)
    historial.append(f"√{a} = {resultado}")
    return resultado

def potencia(a, b):
    resultado = math.pow(a, b)
    historial.append(f"{a}^{b} = {resultado}")
    return resultado

def logaritmo_base10(a):
    if a <= 0:
        print("Error: El logaritmo base 10 solo está definido para números positivos.")
        return None
    resultado = math.log10(a)
    historial.append(f"log10({a}) = {resultado}")
    return resultado

def logaritmo_natural(a):
    if a <= 0:
        print("Error: El logaritmo natural solo está definido para números positivos.")
        return None
    resultado = math.log(a)
    historial.append(f"ln({a}) = {resultado}")
    return resultado

def menu():
    while True:
        print("\n--- Calculadora Mejorada ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz cuadrada")
        print("6. Potencia")
        print("7. Logaritmo base 10")
        print("8. Logaritmo natural")
        print("9. Ver historial")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")
        
        try:
            if opcion == "0":
                print("Saliendo de la calculadora...")
                break
            elif opcion == "9":
                mostrar_historial()
            elif opcion == "5":
                num = float(input("Introduce el número: "))
                resultado = raiz_cuadrada(num)
                if resultado is not None:
                    print(f"Resultado: {resultado}")
            elif opcion in ["1", "2", "3", "4", "6"]:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                if opcion == "1":
                    print(f"Resultado: {suma(num1, num2)}")
                elif opcion == "2":
                    print(f"Resultado: {resta(num1, num2)}")
                elif opcion == "3":
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                elif opcion == "4":
                    resultado = division(num1, num2)
                    if resultado is not None:
                        print(f"Resultado: {resultado}")
                elif opcion == "6":
                    print(f"Resultado: {potencia(num1, num2)}")
            elif opcion == "7":
                num = float(input("Introduce el número: "))
                resultado = logaritmo_base10(num)
                if resultado is not None:
                    print(f"Resultado: {resultado}")
            elif opcion == "8":
                num = float(input("Introduce el número: "))
                resultado = logaritmo_natural(num)
                if resultado is not None:
                    print(f"Resultado: {resultado}")
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Debes ingresar un número.")

if __name__ == "__main__":
    menu()
