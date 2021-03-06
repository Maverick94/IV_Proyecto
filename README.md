# Proyecto IV
[![Build Status](https://travis-ci.org/Maverick94/IV_Proyecto.svg?branch=master)](https://travis-ci.org/Maverick94/IV_Proyecto) [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

* Despliegue: https://actividadetsiit.herokuapp.com/
* [Enlace al bot desplegado](https://telegram.me/ActEtsiibot)
* Contenedor: http://actividadesetsiitweb.azurewebsites.net/status
* DockerHub: https://hub.docker.com/r/maverick94/iv_proyecto/
* Despliegue final: botactividadesetsiit.westus.cloudapp.azure.com

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

### Justificación del PaaS elegido

Yo he elegido Heroku ya que es el más económico. No hay que introducir datos bancarios y ofrecen un servicio bastate bueno para ser gratuito. Además, es bastante sencillo instalar una base de datos. Por defecto nos ofrece *PostgreSQL*

### Despliegue de un Bot

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
$ heroku config:set TOKEN=<el token del bot>
```
entre otras, las cuales son referente a la base de datos. En TravisCI habría que configurarlas también si queremos que el código pase los tests de calidad.

Por último levantamos su *dino* con:

```shell
$ heroku ps:scale worker=1
```
Este *dino* es el que se va a encargar de lanzar la sentencia `cd ./botActividadesEtsiit && python bot_actividad.py` y gracias a esto, el bot estará desplegado.
que es como hemos llamado su acción.

Para automatizar el proceso, entramos en heroku y en las opciones de despliegue, le indicamos que queremos usar github. Le indicamos nuestro repositorio y activamos el despligue autómatico. Selecionamos que sólo se permite el despligue automático si se pasan los test.

Aquí una captura que documenta el despliegue automático a Heroku desde Github

![imagen](http://i65.tinypic.com/2v2axah.png)

Bot desplegado [aquí](https://telegram.me/ActEtsiibot)
### Despliegue de un servicio web
Para desplegar un servicio web, vamos a seguir haciendo uso de Heroku. Para ello, vamos a habilitar otro *dyno* de nuestra aplicación de Heroku para el mismo. En nuestro archivo `Procfile` añadimos `web: gunicorn API_web:__hug_wsgi__ --log-file=-` Heroku, usará nuestra API que está desarrollada en `API_web.py` que hace uso de *Hug*.

Para lanzar nuestro bot y servicio web en dos *dynos* diferentes, usamos este comando
```shell
$ heroku ps:scale worker=1 web=1
```
donde worker es el bot y web es el servicio web. Una vez pasados los test de integración continua, Heroku desplegará la aplicación.

Para comprobar que, efectivamente, funciona nuestro servicio web podemos usar algun comando como `curl`
```shell
$ curl https://actividadetsiit.herokuapp.com/
{"status": "OK"}
```
Podemos incluso lanzar:

```shell
$ curl https://actividadetsiit.herokuapp.com/actividadprueba
{"Actividad_Ejemplo": "[(1, datetime.date(2017, 12, 5), datetime.date(2017, 12, 5), datetime.time(12, 0), datetime.time(13, 0), 'Conferencia 1', 'Esta es una conferencia de prueba que estamos haciendo para estrenar la BD')]"}
```

Despliegue https://actividadetsiit.herokuapp.com/

## Uso de Docker
Podemos "taperizar" el proyecto en un Docker. Para ello, vamos a usar Dockerfile.
Lo primero que he hecho ha sido instalar Docker.

A continuación, vamos a crear la imagen.

```shell
$ sudo docker build -t botactividadesetsiit ./
```
o también

```shell
$ sudo docker pull maverick94/iv_proyecto
```
Para esta última orden, necesitamos haber sincronizado nuestro repositorio con dockerhub.

Una vez descargada la imagen, vamos a crear el contenedor a partir de ella.

```shell
$ sudo sudo docker run -i -t botactividadesetsiit
```

El contenedor se desplegará en local. Comprobamos que funciona en local.

```shell
$ curl localhost:8000/status
{"status": "OK"}
```

Por lo tanto, vamos a proceder al despliegue en Azure.

Para ello, en el Marketplace, elegimos una aplicación web normal. En la configuración de estos recursos,
nos dan la opción de asociar nuestro repositorio de DockerHub. Tras la configuración, la máquina virtual de Azure comienza a descargarse nuestro contenedor y lo despliega en un servicio web.

Aquí un ejemplo:
![imagen](http://i65.tinypic.com/rm5sgn.png)

## Despliegue en un IAAS

Para hacer un despligue en un IAAS, vamos a necesitar una parte de aprovisionamiento y una parte de despligue.
Para ello, vamos a comenzar por la parte de aprovisionamiento. Lo primero que vamos a hacer es instalar vagrant (desde la pagina oficial, ya que la del repositorio no es compatible con el plugin de azure)

```shell
$ sudo dpkg -i vagrant_2.0.1_x86_64.deb
```
y a continuación instalamos el plugin de azure:

```shell
$ sudo vagrant plugin install vagrant-azure
```
Para que Vagrant despliegue nuestra máquina virtual en Azure necesitamos un archivo *Vagrantfile*. Ahí tambien especificaremos el aprovisionamiento con ansible.

Ansible tomará el archivo *playbook.yml* y hará las "gestiones iniciales" de la máquina.

Para proceder hacemos:

```shell
$ vagrant up
```

y creará una máquina virtual en azure con el aprovisionamiento necesario.

Tras aprovisionar, necesitamos desplegar. Para ello usaremos fabric. En la carpeta despliegue, crearemos un archivo *fabfile.py* que consiste en 4 acciones. Instalar la aplicación, ejecutar la aplicación, parar la aplicación y borrar la aplicación.

Un ejemplo del comando sería:
```shell
$ fab -H vagrant@botactividadesetsiit IniciarApp
```
Con este comando, concretamente, lanza la aplicación. Por último, tengo que decir que he usado supervisor para que el servicio quede levantado en segundo plano. Si no usamos supervisor, fabric se quedará conectado eternamente al servidor. Si forzamos su salida, el servicio web no continuará desplegado.

Despliegue final: botactividadesetsiit.westus.cloudapp.azure.com
