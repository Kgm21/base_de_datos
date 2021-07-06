#! /usr/bin/env python
# encoding: utf8

import csv

def guardar_puntajes(nombre_archivo, puntajes):
    """ Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
         puntajes corresponde a una lista de secuencias de elementos.
    Post: se guardaron los valores en el archivo,
          separados por comas.
    """

    archivo = open(nombre_archivo, "w", newline='') # Agrego newline = '' sino hace una linea entre cada linea de datos y cuando quiere leer no funciona
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(puntajes)
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    """ Recupera los puntajes a partir del archivo provisto.
        Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en el formato esperado,
         separados por comas
    Post: la lista devuelta contiene los puntajes en el formato:
          [(nombre1,puntaje1,tiempo1),(nombre2,puntaje2,tiempo2)].
"""

    puntajes = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for nombre, puntaje, tiempo in archivo_csv:
        puntajes.append((nombre, int(puntaje), tiempo))
    archivo.close()
    return puntajes

valores = [("mimi", 89, "4:15"), ("rosa", 23, "5:02")]
guardar_puntajes("puntajes_csv.csv", valores)
print (recuperar_puntajes("puntajes_csv.csv"))