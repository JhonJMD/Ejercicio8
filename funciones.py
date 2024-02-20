import os
txtCat = "1. Novato (edad entre 15 y 16 años)\n2. Intermedio (edad entre 17 y 20 años)\n3. Avanzado (edad mayores a 20 años)\n4. Cancelar"

def subReg(men,may,id):
    print("\nRecuerde que no puede comenzar la categoria sin inscribir por lo menos a 5 jugadores.\n")
    edad = int(input("Ingrese la edad del jugador que va a inscribir: "))
    if men<=edad<=may:
        nombre = input("Ingrese el nombre del jugador: ")
        id+=1
        print(f"\n El ID unico para el jugador que acaba de inscribir es {id}\n")
        jugador={
            "nombre":nombre,
            "edad":edad,
            "puntuacion":{
                "pj":0,
                "pg":0,
                "pp":0,
                "pa":0,
                "tp":0
            }
        }
        return{id:jugador}
    else:
        print("El jugador no pertenece a esta categoria porque no cumple con la edad")
        os.system("pause")
        return {}

idNov = 100
idInte = 300
idAva = 500
novato = {}
intermedio = {}
avanzado = {}
def registrar():
    global idNov,idInte,idAva
    os.system("cls")
    print(f"Jugadores inscritos:\nNovato: {len(novato)}\t\tIntermedio: {len(intermedio)}\t\tAvanzado: {len(avanzado)}")
    print(f"Seleccione la categoria de la cual quiere inscribir a un jugador:\n{txtCat}")
    opCat = int(input(":) "))
    if opCat==1:
        novato.update(subReg(men=15,may=16,id=idNov))
        idNov+=1
        return {"novato":novato}
    elif opCat==2:
        intermedio.update(subReg(men=17,may=20,id=idInte))
        idInte+=1
        return{"intermedio":intermedio}
    elif opCat==3:
        avanzado.update(subReg(men=21,may=100,id=idAva))
        idAva+=1
        return{"avanzado":avanzado}
    elif opCat==4:
        return{}
    else:
        print("Opcion seleccionada inexstente.")
        return{}

    
def tabla(torneo:dict):
    isActive = True
    os.system("cls")
    while isActive:
        try:
            print("\nSeleccione la categoria para ver los resultados: ")
            print("1. Novato\n2. Intermedio\n3. Avanzado\n4. Cancelar")
            cat = int(input(":) "))
            os.system("cls")
            print("ID\t\tNombre\t\tPJ\tPG\tPP\tPA\tTP")
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
        else:
            if cat==1:
                novato = torneo.get('novato')
                for x,y in novato.items():
                    print(f"{x}\t\t{y['nombre']}\t\t{y['puntuacion']['pj']}\t{y['puntuacion']['pg']}\t{y['puntuacion']['pp']}\t{y['puntuacion']['pa']}\t{y['puntuacion']['tp']}")
                isActive = False
            elif cat==2:
                intermedio = torneo.get('intermedio')
                for x,y in intermedio.items():
                    print(f"{x}\t\t{y['nombre']}\t\t{y['puntuacion']['pj']}\t{y['puntuacion']['pg']}\t{y['puntuacion']['pp']}\t{y['puntuacion']['pa']}\t{y['puntuacion']['tp']}")
                isActive = False
            elif cat==3:
                avanzado = torneo.get('avanzado')
                for x,y in avanzado.items():
                    print(f"{x}\t\t{y['nombre']}\t\t{y['puntuacion']['pj']}\t{y['puntuacion']['pg']}\t{y['puntuacion']['pp']}\t{y['puntuacion']['pa']}\t{y['puntuacion']['tp']}")
                isActive = False
            elif cat==4:
                isActive = False
            else:
                print("Opcion seleccionada inexistente.")
                os.system("pause")
                isActive = True 

def campeon(torneo:dict):
    os.system("cls")
    isActive = True
    tp = 0
    pa = 0
    while isActive:
        try:
            print("\nSeleccione la categoria para ver los resultados: ")
            print("1. Novato\n2. Intermedio\n3. Avanzado\n4. Cancelar")
            cat = int(input(":) "))
            os.system("cls")
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
        else:
            if cat==1:
                novato = torneo.get('novato')
                for x,y in novato.items():
                    if tp<y['puntuacion']['tp']:
                        tp = y['puntuacion']['tp']
                        pa = y['puntuacion']['pa']
                        idCamp = x
                    elif tp==y['puntuacion']['tp']:
                        if pa<y['puntuacion']['pa']:
                            tp = y['puntuacion']['tp']
                            pa = y['puntuacion']['pa']
                            idCamp = x
                print(f"🏆🏆 El Campeon de la categoria Novato es: {novato[idCamp]['nombre']} con {novato[idCamp]['puntuacion']['tp']} puntos 🏆🏆")
                isActive = False
            elif cat==2:
                intermedio = torneo.get('intermedio')
                for x,y in intermedio.items():
                    if tp<y['puntuacion']['tp']:
                        tp = y['puntuacion']['tp']
                        pa = y['puntuacion']['pa']
                        idCamp = x
                    elif tp==y['puntuacion']['tp']:
                        if pa<y['puntuacion']['pa']:
                            tp = y['puntuacion']['tp']
                            pa = y['puntuacion']['pa']
                            idCamp = x
                print(f"🏆🏆 El Campeon de la categoria Intermedio es: {intermedio[idCamp]['nombre']} con {intermedio[idCamp]['puntuacion']['tp']} puntos 🏆🏆")
                isActive = False
            elif cat==3:
                avanzado = torneo.get('avanzado')
                for x,y in avanzado.items():
                    if tp<y['puntuacion']['tp']:
                        tp = y['puntuacion']['tp']
                        pa = y['puntuacion']['pa']
                        idCamp = x
                    elif tp==y['puntuacion']['tp']:
                        if pa<y['puntuacion']['pa']:
                            tp = y['puntuacion']['tp']
                            pa = y['puntuacion']['pa']
                            idCamp = x
                print(f"🏆🏆 El Campeon de la categoria Avanzado es: {avanzado[idCamp]['nombre']} con {avanzado[idCamp]['puntuacion']['tp']} puntos 🏆🏆")
                isActive = False
            elif cat==4:
                isActive = False
            else:
                print("Opcion seleccionada inexistente.")
                os.system("pause")
                isActive = True 