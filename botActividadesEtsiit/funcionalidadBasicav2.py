#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Actividad:
    """Una clase para las actividades """

    def __init__(self):
        try:
            with open('actividad_estatica.json') as data_file:
                self.actividad = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo actividad_estatica.json: %s", fallo.errno,fallo.strerror)

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


    def ConsultarActividad(idActividad=None):
        #Se realiza una consulta a la "BBDD" con la idActividad
        #Puesto que no tenemos base de datos funcional, suponemos que el archivo estatico es la consulta
        try:
            with open('actividad_estatica.json') as data_file:
                actividadAModificar = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo actividad_estatica.json: %s", fallo.errno,fallo.strerror)

        return str(actividadAModificar)

# prueba=Actividad()
# print type(str(prueba.ConsultarActividad()))
