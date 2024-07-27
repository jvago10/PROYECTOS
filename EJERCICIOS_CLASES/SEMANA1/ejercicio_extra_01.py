'''PROGRAMA QUE TE DE ACCESO
SOLO SI ERES MAYOR DE EDAD'''

def validar_edad(edad):
    if edad >= 18:
        print ("Tienes acceso")
    else:
        print (" No tienes acceso")

edad_ingresada = int(input("Introduce tu edad: "))

validar_edad(edad_ingresada)       