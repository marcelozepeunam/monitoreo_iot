'''En este archivo se enviaran las lecturas recopiladas hacia una 
hoja de calculo en donde se guardaran los registros del proyecto'''

#?import main 
import openpyxl


import openpyxl

def enviar_datos_a_excel(nombres, edades, puntajes, nombre_archivo):
    # Crear un nuevo libro de Excel
    workbook = openpyxl.Workbook()

    # Obtener la hoja activa (por defecto)
    sheet = workbook.active

    # Agregar encabezados
    sheet.append(["Nombre", "Edad", "Puntaje"])

    # Agregar datos a la hoja
    for nombre, edad, puntaje in zip(nombres, edades, puntajes):
        sheet.append([nombre, edad, puntaje])

    # Guardar el archivo Excel
    workbook.save(nombre_archivo)

# Datos en listas
nombres = ["Juan", "María", "Carlos", "Laura"]
edades = [25, 30, 28, 22]
puntajes = [95, 85, 92, 88]

# Llamar a la función para enviar datos a Excel
enviar_datos_a_excel(nombres, edades, puntajes, "datos.xlsx")
