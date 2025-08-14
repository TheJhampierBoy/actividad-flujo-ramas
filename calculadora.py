import math

def sumar(*numeros):
    return sum(numeros)

def restar(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir(*numeros):
    try:
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado /= num
        return resultado
    except ZeroDivisionError as e:
        return str(e)

def raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(numero)

def pedir_numeros():
    numeros = []
    while True:
        entrada = input("Ingresa un número (o presiona Enter para terminar): ")
        if entrada == "":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return numeros

while True:
    print("\n--- Calculadora Mejorada ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        numeros = pedir_numeros()
        print("Resultado:", sumar(*numeros))
    elif opcion == "2":
        numeros = pedir_numeros()
        print("Resultado:", restar(*numeros))
    elif opcion == "3":
        numeros = pedir_numeros()
        print("Resultado:", multiplicar(*numeros))
    elif opcion == "4":
        numeros = pedir_numeros()
        print("Resultado:", dividir(*numeros))
    elif opcion == "5":
        try:
            numero = float(input("Ingresa el número: "))
            print("Resultado:", raiz_cuadrada(numero))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
