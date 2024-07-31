#Creando una función que nos devuelva los números primos
#Entre el 0 y el argumento que pasemos

#Creamos una función que verifique si un número es primo
def es_primo(num):
    #Verificamos que el número pasado no sea divisible entre 2  y el mismo número
    #por ello es que inicimos desde el 2 y restamos -1 (mismo número)
    for i in range(2,num-1):
        if num%i == 0: return False #Si es divisible retornamos un false y termina el bucle
    #Si termina el bucle, significa que no fue divisible, entonces es primo
    return True

#Creando una funcion que retorne una lista con todos los números primos
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(3,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso sea primo, lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

#DEvolvemos a la lista
resultado = primos_hasta(53)
print (resultado) 

   