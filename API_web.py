import hug
from funcionesBD import Actividad


act=Actividad()

@hug.get('/')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/actividadprueba')
def actividades_bd():
    """Devuelve una actividad de prueba"""
	consulta=act.consultarActividad(1)
    return { "Actividad_Ejemplo": consulta }

@hug.get('/actividad/{id}')
def one( id: int ):
    """Devuelve un hito"""
    consulta=act.consultarActividad(id)
    if id == 2 || id == 1:
        return { "Actividad": consulta }
    else:
        return { "Actividad": No existe esa actividad}
