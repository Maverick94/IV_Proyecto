# Proyecto IV
[![Build Status](https://travis-ci.org/Maverick94/IV_Proyecto.svg?branch=master)](https://travis-ci.org/Maverick94/IV_Proyecto)
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

[Enlace al bot desplegado](https://telegram.me/ActEtsiibot)

Voy a desarrollar un bot de telegram cuyo propósito es conocer las actividades semanales de la *ETSIIT*.
Mediante una serie de comandos, se puede solicitar al bot que nos diga las conferencias del día seleccionado
o que hay de menú en el comedor.

El lenguaje seleccionado es Python, en principio, la versión 2.7 junto con la API de telegram. Para el desarrollo del bot, haré uso de un calendario programado por otro compañero mediante una API que se está desarrollando.

## Integración Continua

Para asegurar la calidad del código, estoy usando la biblioteca `unittest` de Python. Existe un archivo `testFuncionalidadBasicav2.py` donde se han desarrollado test unitarios para cada función desarrollada del código.

Debido a que no existe una base de datos diseñada, estoy usando datos estáticos del archivo `actividad_estatica.json` en formato JSON.

Estos tests son lanzados por **TravisCI**. **TravisCI** hace uso de la regla `make test` del Makefile. Esta regla lanza los tests del archivo anteriormente mencionado.

Al realizar estos test, nos aseguramos de que cualquier modificación, actualización o contribución, no *rompen* el código.

## Despliegue en un PaaS

Yo he elegido Heroku ya que es el más económico. No hay que introducir datos bancarios y ofrecen un servicio bastate bueno para ser gratuito. Además, es bastante sencillo instalar una base de datos. Por defecto nos ofrece *PostgreSQL*

Tras instalar la interfaz que nos ofrece Heroku para el sistema operativo que estemos usando, vamos a proceder
al despligue.

Primeramente nos logueamos con
```shell
$ heroku login
```
Nos pedirá los credenciales. Tras logearnos lanzamos:

```shell
$ heroku apps:create actividadetsiit
```
Con esto estamos creando la aplicación en Heroku.
 A continuación, he creado un archivo `Procfile` donde le he indicado el contenido
```
worker: cd ./botActividadesEtsiit && python bot_actividad.py
```
Gracias a esto, Heroku sabe las tareas que tiene que hacer al desplegarse.
Para asignarle las varibles de entorno, lanzamos el comando:
```shell
heroku config:set TOKEN=<el token del bot>
```
entre otras, las cuales son referente a la base de datos. En TravisCI habría que configurarlas también si queremos que el código pase los tests de calidad.

Por último levantamos su *dino* con:

```shell
heroku ps:scale worker=1
```
Este *dino* es el que se va a encargar de lanzar la sentencia `cd ./botActividadesEtsiit && python bot_actividad.py` y gracias a esto, el bot estará desplegado.
que es como hemos llamado su acción.

Para automatizar el proceso, entramos en heroku y en las opciones de despliegue, le indicamos que queremos usar github. Le indicamos nuestro repositorio y activamos el despligue autómatico. Selecionamos que sólo se permite el despligue automático si se pasan los test.
