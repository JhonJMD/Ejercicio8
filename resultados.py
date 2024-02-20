import os
def winSet(cat:dict,jug,puntos1,jugp,puntos2):
    pg = cat[jug]['puntuacion']['pg'] + 1
    cat[jug]['puntuacion'].update({'pg':pg})
    pa = cat[jug]['puntuacion']['pa'] + puntos1
    cat[jug]['puntuacion'].update({'pa':pa})
    pa = cat[jugp]['puntuacion']['pa'] + puntos2
    cat[jugp]['puntuacion'].update({'pa':pa})
    pp = cat[jugp]['puntuacion']['pp'] + 1
    cat[jugp]['puntuacion'].update({'pp':pp})
    tp = cat[jug]['puntuacion']['tp'] + 2
    cat[jug]['puntuacion'].update({'tp':tp})

def marcadores(cat:dict):
    os.system("cls")
    setP1=0
    setP2=0
    puntos1=0
    puntos2 = 0
    sets=int(input("Digite la cantidad de sets que se jugaron en el partido: "))
    print("Jugadores de la Categoria:")
    for x,y in cat.items():
        print(f"{x} : {y['nombre']}")
    p1 = int(input("Ingrese el ID del jugador A: "))
    pj = cat[p1]['puntuacion']['pj'] + 1
    cat[p1]['puntuacion'].update({'pj':pj})
    p2 = int(input("Ingrese el ID del jugador B: "))
    pj = cat[p2]['puntuacion']['pj'] + 1
    cat[p2]['puntuacion'].update({'pj':pj})

    for i in range(1,sets+1):
        marc1 = int(input(f"Ingrese el marcador de {cat[p1]['nombre']}: "))
        marc2 = int(input(f"Ingrese el marcador de {cat[p2]['nombre']}: "))
        if marc1<marc2:
            setP2 +=1
            puntos1 = puntos1 + marc1 - marc2
            puntos2 = puntos2 + marc2 - marc1
            print(f"Ganador del set {i}: {cat[p2]['nombre']}")
        elif marc2<marc1:
            setP1 +=1
            puntos1 = puntos1 + marc1 - marc2
            puntos2 = puntos2 + marc2 - marc1
            print(f"Ganador del set {i}: {cat[p1]['nombre']}")
            
    if setP2<setP1:
        print(f"El jugador {cat[p1]['nombre']} gano el partido")
        winSet(cat,p1,puntos1,p2,puntos2)
        
    if setP1<setP2:
        print(f"El jugador {cat[p2]['nombre']} gano el partido")
        winSet(cat,p2,puntos2,p1,puntos1)
    
def puntuacion(torneo:dict):
    os.system("cls")
    print("Jugadores inscritos:")
    for x in torneo:
        print(f"{x}: {len(torneo[x])}",end="\t\t")
    print("\nSeleccione la categoria que registrara resultados: ")
    print("1. Novato\n2. Intermedio\n3. Avanzado\n4. Cancelar")
    isActive = True
    while isActive:
        try:
            cat = int(input(":) "))
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
        else:
            if cat==1:
                if len(torneo["novato"])<5:
                    print(f"No es posible iniciar los juegos en la categoria seleccionada por falta de participantes, faltan {5-len(torneo['novato'])} jugadores ")
                    os.system("pause")
                    isActive = False
                else:
                    novato = torneo.get("novato")
                    marcadores(novato)
                    return {'novato':novato}
            elif cat==2:
                if len(torneo["intermedio"])<5:
                    print(f"No es posible iniciar los juegos en la categoria seleccionada por falta de participantes, faltan {5-len(torneo['intermedio'])} jugadores ")
                    os.system("pause")
                    isActive = False
                else:
                    intermedio = torneo.get("intermedio")
                    marcadores(intermedio)
                    return {'intermedio':intermedio}
                
            elif cat==3:
                if len(torneo["avanzado"])<5:
                    print(f"No es posible iniciar los juegos en la categoria seleccionada por falta de participantes, faltan {5-len(torneo['avanzado'])} jugadores ")
                    os.system("pause")
                    isActive = False
                else:
                    avanzado = torneo.get("avanzado")
                    marcadores(avanzado)
                    return {'avanzado':avanzado}
            elif cat==4:
                isActive = False
                return{}
            else:
                print("Opcion seleccionada inexistente.")
                os.system("pause")
                isActive = True


