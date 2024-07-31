#Forma no optima de sumar valores

#def sumar(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = sumar([5,6,1,2,3,45])
  
#Utilizando el parámetro args

def suma(nombre, *numeros):
    
    return f'{nombre}, la suma de tus núemros es: {sum(numeros)}'


resultado = suma("José Vargas", 12,54,63,41,256,45)
print (resultado)    