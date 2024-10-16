import os
import modulos as mdl
from tabulate import tabulate

if __name__ == '__main__':
    os.system('clear')
    os.system('cls')
    
    equipos = [
        {
            'nombre': 'warriors',
            'plantel': {},
            'jugadores': [
                {'nombrej': 'nombrej'}
            ]
  
        },
                {
            'nombre': 's',
            'plantel': {},
            'jugadores': [
                {'nombrej': 'nombrej'}
            ]
  
        }
    ]
    partidos=[
        {
            "id":1,
            'local':'',
            'visitante': '',
            'fechaP':'',
            'goles_local':0,
            'goles_visitantes':0
            }
    ]

    while True:
        titulo = """
            
        ╭╮╱╱╭━━┳━━━┳━━━╮   ╭━━╮╭━━━┳━━━━┳━━━┳╮╱╱╭━━━┳╮╱╱╭╮
        ┃┃╱╱╰┫┣┫╭━╮┃╭━╮┃   ┃╭╮┃┃╭━━┫╭╮╭╮┃╭━╮┃┃╱╱┃╭━╮┃╰╮╭╯┃
        ┃┃╱╱╱┃┃┃┃╱╰┫┃╱┃┃   ┃╰╯╰┫╰━━╋╯┃┃╰┫╰━╯┃┃╱╱┃┃╱┃┣╮╰╯╭╯
        ┃┃╱╭╮┃┃┃┃╭━┫╰━╯┃   ┃╭━╮┃╭━━╯╱┃┃╱┃╭━━┫┃╱╭┫╰━╯┃╰╮╭╯
        ┃╰━╯┣┫┣┫╰┻━┃╭━╮┃   ┃╰━╯┃╰━━╮╱┃┃╱┃┃╱╱┃╰━╯┃╭━╮┃╱┃┃
        ╰━━━┻━━┻━━━┻╯╱╰╯   ╰━━━┻━━━╯╱╰╯╱╰╯╱╱╰━━━┻╯╱╰╯╱╰╯
        """
        print(titulo)
        
        try:
            opc = int(input("1. Registrar Equipo\n2. Registrar Plantel Equipo\n3. Programar Fecha Partido\n4. Registrar Resultado Partido\n5. Ver Equipos\n6. Tabla de clasificación\n7. salir\n Ingresar opciòn: "))
            if (opc == 1):
                mdl.registrar_equipos(equipos)
                
            elif (opc == 2):
              mdl.registrar_plantel(equipos)
              
            elif (opc == 3):
              mdl.programarPartido(partidos,equipos)
              print(partidos)
            elif (opc == 4):
               mdl.actualizarPartido(partidos)
            elif (opc == 5):
               mdl.verEquipos(equipos)
            elif (opc == 6):
                mdl.mostrarEstado(equipos)
                print(mdl.resultado)
            elif (opc == 7):
               break   
            else:
                print("Opción no válida")
        except:
            print('Ingrese un dato correcto')
 

