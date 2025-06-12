

def mostrar_menu():
    print("\n--- Calculadora de Series de Maclaurin ---")
    print("1. e^x")
    print("2. sin(x)")
    print("3. cos(x)")
    print("4. arcsen(x)")
    print("5. arccos(x)")
    print("6. senh(x)")
    print("7. cosh(x)")
    print("0. Salir")

def pedir_datos():
    x = float(input("Ingrese el valor de x: "))
    terminos = int(input("Ingrese el número de términos (precisión): "))
    return x, terminos

def mostrar_resultado(resultado):
    print(f"Resultado aproximado: {resultado}")