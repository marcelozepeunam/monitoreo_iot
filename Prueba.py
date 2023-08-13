import datetime
import time 
import os
import statistics
import paho.mqtt.client as mqtt

from time import strftime
 


lecturas_registradas = []
categorias_registradas = []
horas_registradas = []

procesos = 0

lecturas = [1, 1, 2, 1, 2, 2, 3, 3, 1, 1]
for lectura_iuv in lecturas: 


    while procesos <= 10: 
        procesos += 1



        def fecha_actual():
            fecha_actual = datetime.datetime.now()
            fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
            return fecha_formateada
            fecha_actual = fecha_actual()

        def hora_actual():
            return strftime("%H:%M:%S")

        def define_categoria(lectura_iuv):
                if lectura_iuv <= 2:
                    return "BAJO"
                elif lectura_iuv >= 3 and lectura_iuv <= 5:
                    return "MODERADO"
                elif lectura_iuv >= 6 and lectura_iuv <= 7:
                    return "ALTO"
                elif lectura_iuv >= 8 and lectura_iuv <= 10:
                    return "MUY ALTO"
                elif lectura_iuv >= 11:
                    return "EXTREMO"

        categoria = define_categoria(lectura_iuv)

        def agregando_a_coleccion():
                lecturas_registradas.append(lectura_iuv)
                categorias_registradas.append(categoria)
                horas_registradas.append(hora_actual())

        print(f"\nProceso #{procesos}")
        print("IUV:", lectura_iuv)
        print("Categoria: ", categoria)
        print("Hora: ", strftime("%H:%M:%S"))
        agregando_a_coleccion()
        time.sleep(1)

# Mostrando valores recolectados
print("\nLecturas registradas")
print(lecturas_registradas)

print("\nCategorias registradas")
print(categorias_registradas)

print("\nHoras registradas")
print(horas_registradas)



