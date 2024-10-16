import os

def validateData(mensaje:str):
    global isAllow
    alerta = True
    opciones = ('','N','n','S','s')
    accion = input(f'{mensaje}')
    if (accion not in opciones):
        print('Ingrese una opción corecta.. ')
        validateData()
    elif (bool(accion)== False):
        alerta = False
    elif  (bool(accion) == True):
        alerta = True
    return alerta