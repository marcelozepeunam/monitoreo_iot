'''Vamos a crear 60 lecturas para poder aplicar la funcion de resumen y ver si es cierto'''

import random
import time

lecturas=[]

for i in range (1,60):
    lectura_iuv = random.randint(1, 5)
    lecturas.append(lectura_iuv)

print("Lecturas registradas: ", lecturas)