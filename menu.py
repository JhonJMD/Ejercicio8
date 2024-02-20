import os
menu = "1. Registrar Jugador\n2. Registrar resultados\n3. Ver tabla de resultados\n4. Campeon\n5. Salir"

def menuPpal()->int:
    hasError = True
    print(menu)
    while hasError:
        try:
            return int(input(":) "))
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
            hasError = True