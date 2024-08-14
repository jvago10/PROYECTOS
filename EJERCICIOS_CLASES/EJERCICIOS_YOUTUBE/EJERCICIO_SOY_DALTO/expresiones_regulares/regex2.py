import re

#La cadena en la que se buscarán los patrones
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

#El patron a buscar
pattern = (r"\d{2}/\d{2}/\d{4}")

#El texto con el que se reemplazará el patrón

replacement = "fecha oculta"

#Reemplazar todas las apariciones del patrón en la cadena de texto

new_text = re.sub(pattern,replacement,text)

#imprmir el resultado

print("Texto modificado", new_text)

