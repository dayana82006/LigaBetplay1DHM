import os
def programarPartido(scr,equipos):
    
    try:
        fecha= input('Ingrese la fecha en que la que se guará el partido dd/mm/aa: ')
        local=input('Ingrese el nombre del equipo local: ')
        visitante=input(' Ingrese el nombre del equipo visitante: ')
        localExiste = False
        visitanteExiste = False
        for i in equipos:
            if i.get("nombre") ==local:
                localExiste = True
            
            if i.get("nombre") ==visitante:
                visitanteExiste = True
            
        if localExiste == True and visitanteExiste == True and local != visitante :           
            scr.append(
                        { 'id':scr[0]["id"]+1,
                         'fechaP': fecha,
                        'local': local,
                        'visitante':visitante,
                        "goles_local":0,
                        "goles_visitante":0}
                    )
        else:
            print("verifique lque los equipos existan y que sean diferentes entre si ")
        print(f'')
      
    except: 
        input('Alguno de los datos ingresados es erroneo')
        

def actualizarPartido(scr):
    print('Estos son los partidos programados')
    print(scr)
    
    id=input('ingrese el id del partido: ')
    goles_local=(input('Ingrese los goles anotados por el equipo local: '))
    goles_visitante=(input('Ingrese los goles anotados por el equipo visitante: '))
    for i in scr:
        if i.get('id')==id:
           i['goles_local']=goles_local
           i['goles_visitantes']=goles_visitante
    print(scr)
        