# Variable global
global_variable = 10

def modify_global_variable():
    # Utilizamos la palabra clave 'global' para indicar que queremos modificar la variable global_variable
    global global_variable
    global_variable = 20
    print("Dentro de la función:", global_variable)

print("Antes de llamar a la función:", global_variable)
modify_global_variable()
print("Después de llamar a la función:", global_variable)
