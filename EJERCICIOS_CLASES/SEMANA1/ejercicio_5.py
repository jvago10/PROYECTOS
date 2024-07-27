'''Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F'''

def calificacion_letra (calificacion):
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80 and calificacion <= 89:
        return 'B'
    elif calificacion >= 70 and calificacion <= 79:
        return 'C'
    elif calificacion >= 60 and calificacion <= 69:
        return 'D'
    else:
        return 'F'
    
#Solicitar que el usuario ingrese la nota

try:
    calificacion_numerica = float(input('Ingrese la calificación: '))
    
    letra = calificacion_letra (calificacion_numerica)
    
    print (f'La calificación en letra es: {letra}')
    
except ValueError:
    print ('Por favor ingrese un número valido') 
    
    
       
                                   