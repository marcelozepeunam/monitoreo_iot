'''En este archivo se enviaran las lecturas recopiladas hacia una 
hoja de calculo en donde se guardaran los registros del proyecto'''
#!Hace falta probar este codigo con lecturas reales


import pyexcel
import main 


#Importamos las listas con los valores recopilados
lecturas = main.lecturas_registradas
categorias = main.categorias_registradas
horas = main.horas_registrados
errores = main.errores_registrados

# Crear un diccionario de datos (estos serán los encabezados)
data = {
    "IUV": lecturas,
    "Categorias": categorias,
    "Horas": horas,
    "Errores": errores
}

# Guardar los datos en un archivo de hoja de cálculo
nombre_archivo = "datos.ods"  # Extensión .ods para hoja de cálculo Calc
pyexcel.save_as(registros=data, ubicacion_archivo=nombre_archivo)
