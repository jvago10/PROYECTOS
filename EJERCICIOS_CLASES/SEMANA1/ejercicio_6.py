#Escribe un programa que solicite al usuario tres números y determine
#cuál de ellos es el mayor.

numero1 = int(input("Ingrese el primero número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
    
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    
    mayor = numero3
    
print (f"El número mayor es: {mayor}") 


          


