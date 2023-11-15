'''El proposito de este modulo es para comprobar los tiempos de carga de algunas funciones'''
import time 

inicio = time.time()

#Ingresar la funcion a evaluar 
from voz_artificial import voz_artificial
fin = time.time()

speed = fin-inicio
print(f"\nTiempo de ejecución: {speed} segundos".format(speed))