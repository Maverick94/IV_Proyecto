#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import psycopg2

class Actividad(object):
    """Una clase para las actividades """
    idActividad=""
    fechai=""
    fechaf=""
    horai=""
    horaf=""
    denominacion=""
    descripcion=""


    def __init__(self):
        self.db = os.environ["NAME_BD"]
        self.host_db = os.environ["HOST_BD"]
        self.usuario = os.environ["USER_BD"]
        self.pw = os.environ["PW_BD"]
        try:
            with open('actividad_estatica.json') as data_file:
                self.actividad = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo actividad_estatica.json: %s", fallo.errno,fallo.strerror)

    def conectarBD(self):
        con = psycopg2.connect(database=self.db, user=self.usuario, password=self.pw, host=self.host_db)
        return con


    def ModificarActividad(idActividad=None, horai=None, horaf=None, fechai=None, fechaf=None, denominacion=None, descripcion=None):
        #Se realiza una consulta a la "BBDD" con la idActividad
        #Puesto que no tenemos base de datos funcional, suponemos que el archivo estatico es la consulta
        try:
            with open('actividad_estatica.json') as data_file:
                actividadAModificar = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo actividad_estatica.json: %s", fallo.errno,fallo.strerror)

        #Decodificacion del json
        oldfechai = str(actividadAModificar["fechai"])
        oldfechaf = str(actividadAModificar["fechaf"])
        oldhorai = str(actividadAModificar["horai"])
        oldhoraf = str(actividadAModificar["horaf"])
        olddenominacion = str(actividadAModificar["denominacion"])
        olddescripcion = str(actividadAModificar["descripcion"])
        newfechai=oldfechai
        newfechaf=oldfechaf
        newhorai=oldhorai
        newhoraf=oldhoraf
        newdenominacion=olddenominacion
        newdescripcion=olddescripcion
        if fechai != None:
            newfechai=fechai
        if fechaf != None:
            newfechaf=fechaf
        if horai != None:
            newhorai=horai
        if horaf != None:
            newhoraf=horaf
        if denominacion != None:
            newdenominacion=denominacion
        if descripcion != None:
            newdescripcion=descripcion
        volcado = {"horai":newhorai, "horaf":newhoraf,"fechai":newfechai,"fechaf":newfechaf,"denominacion":newdenominacion,"descripcion":newdescripcion}

        try:
            with open('test.json','w') as outfile:
                json.dump(volcado, outfile)
                return True
        except IOError as fallo:
            print("Error %d escribiendo en test.json: %s", fallo.errno,fallo.strerror)


    def consultarActividad(self,idActividad=None):
        pe = self.conectarBD()
        cursor = pe.cursor()
        cursor.execute("SELECT * FROM Actividades WHERE idactividad="+str(idActividad))
        consulta = cursor.fetchone()
        pe.close()
        cursor.close()
        #Se realiza una consulta a la "BBDD" con la idActividad
        #Puesto que no tenemos base de datos funcional, suponemos que el archivo estatico es la consulta
        # try:
        #     with open('actividad_estatica.json') as data_file:
        #         actividadAConsultar = json.load(data_file)
        # except IOError as fallo:
        #     print("Error %d leyendo actividad_estatica.json: %s", fallo.errno,fallo.strerror)

        return str(consulta)
