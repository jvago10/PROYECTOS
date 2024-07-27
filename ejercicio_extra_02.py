'''Contador de vocales en python'''

frases =input('Frase: ')
vocales = "aeiou"
contador = 0

for letra in frases:
    if letra in vocales:
        contador += 1
        
print (f'\rNúmero de vocales: {contador}') 

