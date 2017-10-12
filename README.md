# Proyecto IV
[![Build Status](https://travis-ci.org/Maverick94/IV_Proyecto.svg?branch=master)](https://travis-ci.org/Maverick94/IV_Proyecto)

Voy a desarrollar un bot de telegram cuyo propósito es conocer las actividades semanales de la *ETSIIT*.
Mediante una serie de comandos, se puede solicitar al bot que nos diga las conferencias del día seleccionado
o que hay de menú en el comedor.

El lenguaje seleccionado es Python, en principio, la versión 2.7 junto con la API de telegram. Para el desarrollo del bot, haré uso de un calendario programado por otro compañero mediante una API que se está desarrollando.

Para asegurar la calidad del código, estoy usando la biblioteca `unittest` de Python. Existe un archivo `testFuncionalidadBasicav2.py` donde se han desarrollado test unitarios para cada función desarrollada del código.

Debido a que no existe una base de datos diseñada, estoy usando datos estáticos del archivo `actividad_estatica.json` en formato JSON.

Estos tests son lanzados por **TravisCI**. **TravisCI** hace uso de la regla `make test` del Makefile. Esta regla lanza los tests del archivo anteriormente mencionado.

Al realizar estos test, nos aseguramos de que cualquier modificación, actualización o contribución, no *rompen* el código.
