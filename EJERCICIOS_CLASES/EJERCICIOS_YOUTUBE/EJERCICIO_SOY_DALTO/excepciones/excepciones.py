#Creando la función que sume números
def sumar_dos():
    #inciando un blucle
    while True:
        #Pidiendo numeros
        a = input('Ingrese el primer número: ')
        b = input('Ingrese el segundo número: ')
        #intentando convertir a números y sumarlos
        try:
            resultado = int(a) + int(b)
        #Si lanza una excepción, perdirle que reingrese los datos    
        except:
            print('Por favor, ingrese números válidos.')
        #si todo sale bien terminamos el bucle 
        else:
            break
    return resultado            
   

print('El resultado de la suma es:', sumar_dos())

