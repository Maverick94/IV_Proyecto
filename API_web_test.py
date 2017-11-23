import hug
import API_web

def test_raiz_OK():
    datos = hug.test.get(API_web, '/')
    assert datos.status == "200 OK"
    assert datos.data['status']=="OK"

def test_status_OK():
    datos = hug.test.get(API_web, '/status')
    assert datos.status == "200 OK"
    assert datos.data['status']=="OK"

# def test_actividades_bd_OK():
#     datos = hug.test.get(API_web, '/actividadprueba')
#     assert datos.status == "200 OK"
#     assert datos.data['Actividad_Ejemplo'] == "[(1, datetime.date(2017, 12, 5), datetime.date(2017, 12, 5), datetime.time(12, 0), datetime.time(13, 0), 'Conferencia 1', 'Esta es una conferencia de prueba que estamos haciendo para estrenar la BD')]"
#
# def test_one_OK():
#     datos = hug.test.get(API_web, '/actividad/1')
#     assert datos.status == "200 OK"
#     assert datos.data['Actividad'] == "[(1, datetime.date(2017, 12, 5), datetime.date(2017, 12, 5), datetime.time(12, 0), datetime.time(13, 0), 'Conferencia 1', 'Esta es una conferencia de prueba que estamos haciendo para estrenar la BD')]"
#     datos = hug.test.get(API_web, '/actividad/2')
#     assert datos.status == "200 OK"
#     assert datos.data['Actividad'] == "[(1, datetime.date(2017, 12, 5), datetime.date(2017, 12, 5), datetime.time(12, 0), datetime.time(13, 0), 'Conferencia 1', 'Esta es una conferencia de prueba que estamos haciendo para estrenar la BD')]"
