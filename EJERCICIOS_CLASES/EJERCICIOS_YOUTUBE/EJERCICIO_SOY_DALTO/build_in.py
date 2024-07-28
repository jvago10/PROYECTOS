numeros = [4,12,58,41,63,5,9] # valido para tupla también

#Econtrando el número mayor y menor de una lista

numero_mas_alto = max(numeros)
numero_mas_bajo = min(numeros)

print (f'El número mas alto es: {numero_mas_alto}')
print (f'El número mas bajo es: {numero_mas_bajo}')

#redondeando a 6 decimales

numero_a_redondear = round(124.2548,3)

print(f'El número redondeado es: {numero_a_redondear}')

#retorna false -> 0, vacio, False, none  /  true -> Distinto a 0, True, cadena, o datos no vacio 

resultado_bool = bool()

print(resultado_bool)

#retorna True -> sí todos los datos son verdaderos

resultado_all = all([{0, 123, 45, (54)}])

print (resultado_all)

#Suma total de núemeros

suma_total = sum(numeros)

print(f'La suma total de los numeros es: {suma_total}')




