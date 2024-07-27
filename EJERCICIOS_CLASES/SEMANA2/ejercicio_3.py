#3. Escribir un programa que pida al usuario un número entero positivo
#mayor que 2 y muestre por pantalla si es un número primo o no.

numero = int(input("Introduce el nuúmero entero positivo MAYOR que 2: "))

es_primo = True

if numero < 2:
    es_primo = False
    
else:
    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0:
            es_primo = False
            break
        
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")            