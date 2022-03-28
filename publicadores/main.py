##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: main.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Este archivo define el punto de ejecución del Publicador
#
#-------------------------------------------------------------------------
import random
from src.patient import Patient
from src.helpers.publicador import publish
import time

if __name__ == '__main__':
    print("Iniciando simulación del sistema SMAM...")
    older_patients = []
    total_patients = random.randint(1, 5)
    print(f"actualmente hay {total_patients} adultos mayores...")
    for _ in range(total_patients):
        older_patients.append(Patient())
    print("Comenzando monitoreo de signos vitales...")
    print()
    for _ in range(20):
        for patient in older_patients:
            print("extrayendo signos vitales...")
            patient.check_devices()
            print()
            print("analizando signos vitales...")
            if patient.wearable.blood_pressure > 110 or patient.wearable.temperature > 37.5 or patient.wearable.heart_rate > 110:
                print("anomalía detectada, notificando signos vitales...")
                publish('notifier', patient.to_json())
            print()
            # Agregado por Alan para la tarea 1
            if patient.timer.numero_random%8 == 0:
                print('Hora de Suministrar', patient.timer.medicine, 'al paciente')
                publish('notifier', patient.to_json())
            print()
            if patient.accelerometer.ejeX == 20 or patient.accelerometer.ejeY == 20 or patient.accelerometer.ejeZ == -20:
                print('Ya se cayó el paciente!!! ayudaaaaaaaaaaaaaaaaa :O')
                publish('notifier', patient.to_json())
            print()
            print("actualizando expediente...")
            publish('record', patient.to_json())
            publish('monitor', patient.to_json())
            time.sleep(1)
