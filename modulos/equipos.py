import os
import modulos as plantel

import modulos as vd
def registrar_equipos(general):
    isAddEquipo=True
    while(isAddEquipo):
        print("Registrar Equipo")
        try:
           
            nombre=input('Ingrese el nombre del equipo')
            general.append({'nombre':nombre, 'plantel':{}})
           # general['equipo'].update({'nombre':nombre})
            isAddEquipo= vd.validateData(mensaje='Desea Seguir agrgando S(si) Enter (no)')  
            break
        except:
           print("Dato no valido")
           input("Presione Enter para regresar: ")
