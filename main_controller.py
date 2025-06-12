# controller/main_controller.py

from model import taylor_model
from view import terminal_view

def ejecutar():
    while True:
        terminal_view.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Gracias por usar la calculadora.")
            break

        x, terminos = terminal_view.pedir_datos()

        if opcion == "1":
            resultado = taylor_model.taylor_exponencial(x, terminos)
        elif opcion == "2":
            resultado = taylor_model.taylor_seno(x, terminos)
        elif opcion == "3":
            resultado = taylor_model.taylor_coseno(x, terminos)
        elif opcion == "4":
            resultado = taylor_model.taylor_arcsen(x, terminos)
        elif opcion == "5":
            resultado = taylor_model.taylor_arccos(x, terminos)
        elif opcion == "6":
            resultado = taylor_model.taylor_seno_hiperbolico(x, terminos)
        elif opcion == "7":
            resultado = taylor_model.taylor_coseno_hiperbolico(x, terminos)
        else:
            print("Opción no válida.")
            continue

        terminal_view.mostrar_resultado(resultado)