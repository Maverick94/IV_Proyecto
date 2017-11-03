#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import os   #Biblioteca para obtener las variables de entorno
import psycopg2
from funcionalidadBasicav2 import Actividad

token = os.environ["TOKEN"]#Accedemos a las variables de entorno (configuradas en travis y heroku)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['actividades'])
def send_activity(message):
	cid = message.chat.id
	act=Actividad()
	consulta=act.consultarActividad(1)
	# vuelta="Título: "+titulo+" Descripción: "+descripcion
	bot.send_message(cid, consulta)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop=True)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(commands=['actividades'])
# def send_activity(m):
#     """Función que envia las actividades de la semana al usuario. """
#     cid = m.chat.id # Obtenemos la id del usuario.
#     db = os.environ["NAME_BD"]
#     host_db = os.environ["HOST_BD"]
#     usuario = os.environ["USER_BD"]
#     pw = os.environ["PW_BD"]
#     con = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM Actividades")
#     resp = ""
#     #filas = len(cursor.fetchall())
#     titulo = cursor.fetchone()[5]
#     cursor.execute("SELECT * FROM Actividades")
#     descripcion=cursor.fetchone()[6]
#     con.close()
#     vuelta="Título: "+titulo+" Descripción: "+descripcion
#
#     bot.send_message(cid, vuelta)
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#
#
# bot.polling()


    # db = os.environ["NAME_BD"]
    # host_db = os.environ["HOST_BD"]
    # usuario = os.environ["USER_BD"]
    # pw = os.environ["PW_BD"]
    # con = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    # cursor = con.cursor()
    # cursor.execute("SELECT * FROM Actividades")
    # resp = ""
    # #filas = len(cursor.fetchall())
    # titulo = cursor.fetchone()[5]
    # cursor.execute("SELECT * FROM Actividades")
    # descripcion=cursor.fetchone()[6]
