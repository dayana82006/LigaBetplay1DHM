import os
def verEquipos(equipos):
    opcion = 0
    for i, index in enumerate(equipos):
       print(f"{i+1}.{index}")
    opcion = int(input(''))
    print(equipos[opcion-1])
    input()