#Creando una funcion

#def saludar():
#    print("Esta es la creación de una funcion")
    

#saludar()

#Crear una funcion que tenga parámetros

def saludar (nombre, sexo):
    
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'Reina'
    elif (sexo == 'hombre'):
        adjetivo = 'Rey'
    else:
        adjetivo = 'broca'    
        
        
        
    print(f"Hola {nombre}, mi {adjetivo},  ¿Cómo estás?")


saludar ("josea", "mUjer")
saludar ("Juan", "Hombre")
saludar ("carmen", "mUjer")

#Crear una función que retorne valores y un creador de contraseñas

def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    
    c1 = num - 2
    c2 = num
    c3 = num - 5
    
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return (contraseña, num) #se utiliza para guardar el valor.
    
password, primer_numero = crear_contrasena_random(5)

print (f'Tu contraseña nueva es: {password}')
print (f'El número utilizado para crearlo fue: {primer_numero}') 




