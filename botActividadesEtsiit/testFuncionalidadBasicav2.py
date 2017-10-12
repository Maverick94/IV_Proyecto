#!/usr/bin/python
# -*- coding: utf-8 -*-

from funcionalidadBasicav2 import Actividad
import unittest


class TestFuncionesBasicas(unittest.TestCase):

    def setUp(self):
        self.actividad=Actividad()

    def test_creacion_actividad_correcta(self):
        self.assertIsInstance(self.actividad,Actividad,"Se creó correctamente la actividad")

    def test_modificacion_actividad_correcta(self):
        self.assertTrue(self.actividad.ModificarActividad(),"Se Modificó correctamente la actividad")

    def test_consulta_actividad(self):
        self.assertIsInstance(self.actividad.ConsultarActividad(), str, "Se Consultó correctamente la actividad")


if __name__ == '__main__':
    unittest.main()
