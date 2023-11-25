import math

def obtener_lista_numeros():
    n = int(input("Equipo DAO ingrese la cantidad de números: "))
    return [float(input(f"Ingresa el número #{i + 1}: ")) for i in range(n)]

def operacion_suma():
    numeros = obtener_lista_numeros()
    resultado = sum(numeros)
    print(f"Resultado de la suma: {resultado}")

def operacion_producto():
    numeros = obtener_lista_numeros()
    resultado = 1
    for num in numeros:
        resultado *= num
    print(f"Resultado del producto: {resultado}")

def operacion_division():
    num1 = float(input("Equipo DAO ingrese el primer número: "))
    num2 = float(input("Equipo DAO ingrese el segundo número: "))
    
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado de la división: {resultado}")
    else:
        print("¡Error! No se puede dividir entre cero.")

def calcular_factorial():
    n = int(input("Equipo DAO ingrese un número para calcular su factorial: "))
    resultado = math.factorial(n)
    print(f"Factorial de {n}: {resultado}")

def mostrar_tablas_multiplicar():
    num = int(input("Equipo DAO ingrese un número para mostrar su tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def calcular_cuadrado_cubo():
    num = float(input("Equipo DAO ingrese un número para calcular su cuadrado y cubo: "))
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"Cuadrado de {num}: {cuadrado}")
    print(f"Cubo de {num}: {cubo}")

def calcular_promedio():
    numeros = []
    while True:
        num = float(input("Equipo DAO ingrese (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"Promedio de los números: {promedio}")
    else:
        print("¡Error! No se ingresaron números.")

def encontrar_maximo_y_minimo():
    n = int(input("Equipo DAO ingrese la cantidad de números a comparar: "))
    if n > 0:
        numeros = [float(input(f"Ingresa el número #{i + 1}: ")) for i in range(n)]
        maximo = max(numeros)
        minimo = min(numeros)
        print(f"Valor máximo: {maximo}")
        print(f"Valor mínimo: {minimo}")
        print(f"Total de valores ingresados: {n}")
    else:
        print("Por favor, ingresa una cantidad válida de números.")

def menu_principal():
    while True:
        print("\n---hola, equipoDAO este es su Menú de Operaciones ---")
        print("1. Suma de números")
        print("2. Producto de números")
        print("3. División entre 2 números")
        print("4. Calcular factorial")
        print("5. Tablas de multiplicar")
        print("6. Cuadrado y cubo de un número")
        print("7. Promedio de una serie de números")
        print("8. Valor máximo y mínimo")
        print("9. Salir")

        opcion = input("Selecciona una opción (1-9): ")

        if opcion == "1":
            operacion_suma()
        elif opcion == "2":
            operacion_producto()
        elif opcion == "3":
            operacion_division()
        elif opcion == "4":
            calcular_factorial()
        elif opcion == "5":
            mostrar_tablas_multiplicar()
        elif opcion == "6":
            calcular_cuadrado_cubo()
        elif opcion == "7":
            calcular_promedio()
        elif opcion == "8":
            encontrar_maximo_y_minimo()
        elif opcion == "9":
            print("¡Aqui finaliza el programa, vuelve pronto!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
