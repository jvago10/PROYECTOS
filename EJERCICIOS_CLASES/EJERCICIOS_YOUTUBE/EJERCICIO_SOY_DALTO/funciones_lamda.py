#Crando una funcion lambda para multiplicar por dos

multiplicar_por_dos = lambda x: x*2

print  (multiplicar_por_dos(5))

#ejemplo de una buena práctica del uso de lambda

numeros = [2, 5, 6 , 7 , 9 , 10 , 12 ,42] #creamos la lista

def es_par(num):
    if (num%2 ==0):
        return True
    
#usando filter con una funcion común
numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))

#---------Aquí usamos la función def para crear la función 
#---------y determinar si el número es par o impar en una lista

numeros_pares_lambda = filter(lambda x: x%2 == 0, numeros)
print(list(numeros_pares_lambda))

#------Ejemplo de uso de lambda para el ahorro de codigos






      