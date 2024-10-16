import os
import modulos as vd
def registrar_plantel(general):
    
    try:
        for equipo in general:
          print(equipo['nombre'])
        nombre = (input('Ingrese el nombre del equipo al que quiere registrar plantel: '))
        entrenador = input("Ingrese el nombre del entrenador: ")
        asistente = input("Ingrese el nombre del asistente: ")
        preparador = input("Ingrese el nombre del preparador: ")
        print('Plantel registrado satisfactoriamente\nAcontinuacion deberá registrar a los jugadores')

        while True:
            nombreJ = input('Ingrese el nombre del jugador -> ')
            posicionJ = input('Ingrese la posicion del jugador -> ')
            dorsal = int(input('Ingrese el dorsal del jugador -> '))
            for i in general:
                if i['nombre'] == nombre:
                    i['plantel']={'entrenador':entrenador,
                                'asistente': asistente,
                                'preparador':preparador}
                    i['jugadores'].append({'nombreJ':nombreJ,
                                           'posicionJ':posicionJ,
                                           'preparador':preparador,
                                           'dorsal':dorsal})
            break

        
    except:
       print("Dato inválido")
       input("Presione Enter para regresar: ")