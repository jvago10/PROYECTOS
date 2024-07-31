#Pedir el nombre y la edad de los compañeros que vinieron a clase


#Función para obtener el asistente y el profesor
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = [] #Crea una lista con los compañeros
    
    #Ejecuta un for para pedir informaciíon de los compañeros
    for i in range(cantidad_de_compañeros):
        nombre = input('Ingresa el nombre del compañero: ')
        edad = input('Ingresa la edad del compañero: ')
        compañero = (nombre, edad)
        compañeros.append(compañero)#Agrega información a la lista
        
    compañeros.sort(key=lambda x: x[1]) #Ordena de mayor a menor según su edad
    
    #Compañeros [x] devuelve una tupla con (nombre,edad) y después accedemos al nombre
    #para definir al asistente y profesor
    asistente = compañeros [0][0]
    profesor = compañeros [-1][0]
    return asistente, profesor #Retornamos una tupla 

    
asistente, profesor = obtener_compañeros(3) #Desempaquetamos lo que nos retorna la función

#Mostramos el resultado
print (f'El profesor es: {profesor} y su asistente es: {asistente}') 


      