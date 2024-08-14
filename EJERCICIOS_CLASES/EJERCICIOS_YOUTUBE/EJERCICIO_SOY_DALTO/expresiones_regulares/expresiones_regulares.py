import re

texto = '''Hola Maestro, esta es la cadena 154. como estas mi capitan
Esta es la linea 2 de texto.
Y Esta es la final (linea 10) definitiva mi capitan'''

#Haciendo una búsqueda simple
#resultado = re.findall("Esta", texto) #flags=re.IGNORECASE) para ignorar mayúsculas

#print (resultado)

#\d -> |  busca digitos numéricos del  0 - 9 
#\d+ ->|  busca digitos numéricos de dos cifras
#\D -> |  busca TODO MENOS dígitos númericos
#\w -> |  busca caracteres alfanumericos [a-z A-Z 0-9 _]
#\W -> |  busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
#\s -> |  busca espacios en blanco  -> espacios, tabs, salto de línea
#\S -> |  busca TODO MENOS espacios en blanco  -> espacios, tabs, salto de línea
#. -> |  busca TODO MENOS saltos de líneas
#\n -> |  busca saltos de líneas
#\ -> |  Cancela los caracteres especiales #re.findall(r'\.', texto)

#resultado1 = re.findall(r'\.', texto) 

#armando una cadena que busque un número, seguido de un punto y espacio 
#resultado = re.findall(f'\d\.\s', texto)

#Buscando el principio de una Línea
#^ -> Busca el comienzo de una linea (buscando hola al principio de la linea)
# flags=re.M -> multilínea
#$ -> Busca el final de una
resultado = re.findall(f'^Esta', texto, flags=re.M) 
resultado1 = re.findall(f'capitan$', texto, flags=re.M) 

#{n} -> busca n cantidad de veces el valor de la izquierda (3 números juntos esta vez)

resultado3 = re.findall(r'\d{3}', texto)

#{n.m} -> al menos n, como máximo m

resultado4 = re.findall(r'\d{1,4}', texto)

# | -> busca una cosa o la otra

resultado5 = re.findall(r'\d{2,4}|Hola',texto)

print (resultado5)




