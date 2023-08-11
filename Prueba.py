import datetime

def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d / %m / %Y")
    return fecha_formateada

fecha_actual = obtener_fecha_actual()
print("La fecha actual es:", fecha_actual)