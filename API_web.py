import hug
from botActividadesEtsiit.funcionesBD import Actividad
import json


act=Actividad()

@hug.get('/')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/actividadprueba')
def actividades_bd():
    consulta=act.consultarActividad(1)
    return { "Actividad_Ejemplo": consulta }

@hug.get('/actividad/{id}')
def one(id):
    consulta=act.consultarActividad(int(id))
    if id == 2 or id == 1:
        return { "Actividad": consulta }
    else:
        return { "Actividad": "No existe esa actividad"}
