#1. Escribe un programa que solicite al usuario dos números y muestre su
#suma, resta, multiplicación, división, división entera y residuo (módulo).
num1 = int(input("Ingrese el numero 1 entero: "))

num2 = int(input("Ingrese el numero 2 entero: "))

suma = int(num1 + num2)
resta = int(num1 - num2)
multiplicacion = int(num1*num2)
division = round(num1/num2, 3)#acepta 3 digitos para la division
divison_entera = round(num1 / num2,)#acepta 2 digitos para la division
residuo = num1 % num2

print (f'La suma es: {suma}')
print (f'La resta es: {resta}')
print (f'La multiplicación es: {multiplicacion}')
print (f'la división es: {division}')
print (f'La division entera es: {divison_entera}')
print (f'El residuo es: {residuo}')

