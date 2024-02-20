import os
import menu
import funciones
import resultados as res

torneo ={}
isActive = True
while isActive:
    os.system("cls")
    try:
        opMenu = menu.menuPpal()
    except ValueError:
        print("Error en el dato de ingreso, intente nuevamente")
    else:
        if opMenu==1:
            rta = "S"
            while rta in ["S","s"]:
                torneo.update(funciones.registrar())
                rta = input("Desea registrar otro jugador s(Si) o n(No): ")
        elif opMenu==2:
            rta = "S"
            while rta in ["S","s"]:
                torneo.update(res.puntuacion(torneo))
                rta = input("Desea registrar resultados de otro partido s(Si) o n(No): ")            
        elif opMenu==3:
            funciones.tabla(torneo)
            os.system("pause")
        elif opMenu==4:
            funciones.campeon(torneo)
            os.system("pause")
        elif opMenu==5:
            isActive = False
        else:
            print("Opcion seleccionada inexistente.") 
            os.system("pause")           


