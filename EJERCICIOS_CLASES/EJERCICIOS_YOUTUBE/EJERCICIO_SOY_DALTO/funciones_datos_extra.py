#creando una funcion de  parámetros

def frase (nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, soy {adjetivo}'

def frase2(nombre, apellido, adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, soy {adjetivo}'


frase_1= frase("José","Vargas","Capo")
print (frase_1)

frase_2= frase2("José","Vargas") #complementa porque ya definí el adjetivo
print (frase_2)

