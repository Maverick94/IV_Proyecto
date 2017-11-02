# Proyecto IV
[![Build Status](https://travis-ci.org/Maverick94/IV_Proyecto.svg?branch=master)](https://travis-ci.org/Maverick94/IV_Proyecto)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
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

Yo he elegido Heroku ya que es el más económico. No hay que introducir datos bancarios y ofrecen un servicio bastate bueno para ser gratuito. Además, es bastante sencillo instalar una base de datos.

Tras instalar la interfaz que nos ofrece Heroku para el sistema operativo que estemos usando, vamos a proceder
al despligue.

Primeramente nos logueamos y tras logearnos lanzamos:

`$ heroku apps:create actividadetsiit`

para crear la aplicación. A continuación, he creado un archivo `Procfile` donde le he indicado el contenido
`worker: cd ./botActividadesEtsiit && python bot_actividad.py`

Gracias a esto, heroku sabe las tareas que tiene que hacer al desplegarse.



Para asignarle las varibles de entorno, lanzamos el comando:
`heroku config:set TOKEN=<el token del bot>`

por último levantamos su *dino* con:

`heroku ps:scale worker=1`

que es como hemos llamado su acción.

Para automatizar el proceso, entramos en heroku y en deploy le indicamos que queremos usar github. Le indicamos nuestro repositorio y seleccinamos el despligue automático si pasa los tests.


El bot esta lanzado [aquí](https://telegram.me/ActEtsiibot)
