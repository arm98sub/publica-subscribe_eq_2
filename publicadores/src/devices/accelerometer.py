##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: accelerometer.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el publicador que enviará mensajes hacia el distribuidor de mensajes
#
#   A continuación se describen los métodos que se implementaron en esta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |       __init__()       |  - self: definición de   |  - constructor de la  |
#           |                        |    la instancia de la    |    clase              |
#           |                        |    clase                 |                       |
#           +------------------------+--------------------------+-----------------------+
#           |          run()         |  - self: definición de   |  - simula la          |
#           |                        |    la instancia de la    |    posición del       |
#           |                        |    clase                 |    adulto mayor en un |
#           |                        |                          |    determinado        |
#           |                        |                          |    momento            |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from faker import Faker
import random

class Accelerometer:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")
        self.ejeX = 0
        self.ejeY = 0
        self.ejeZ = 0

    def run(self):
        """
        una caída se puede determinar de acuerdo al posicionamiento
        de la persona en un determinado momento
        """
        
        self.ejeX = random.randint(-20,20)
        self.ejeY = random.randint(-20,20)
        self.ejeZ = random.randint(-20,20)
        