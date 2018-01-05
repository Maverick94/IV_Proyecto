# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os

def InstalarApp():
    """ Función para descargar el bot del repositorio. """
	# Descargamos el repositorio
    run('git clone https://github.com/Maverick94/IV_Proyecto.git')

	# Instalamos pip3
    # run('sudo apt-get install -y python3-pip')

	# Accedemos al repositorio e instalamos las dependencias
    run('sudo apt-get install -y supervisor')
    run('cd IV_Proyecto/ && sudo pip3 install -r requirements.txt')
    run('sudo cp IV_Proyecto/apiweb.conf /etc/supervisor/conf.d/')

def BorrarApp():
    """ Función para borrar el repositorio. """
    # Borramos el repositorio
    run('sudo rm -rf ./IV_Proyecto')

def IniciarApp():
    """ Función para iniciar la web. """
	# Importamos las variables globales
	# with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"
    run('cd ~/IV_Proyecto/ && sudo supervisorctl reread && sudo supervisorctl start apiweb',pty=False)

def PararApp():
    """ Función para iniciar la web. """
	# Importamos las variables globales
	# with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"
    run('sudo supervisorctl stop apiweb',pty=False)
