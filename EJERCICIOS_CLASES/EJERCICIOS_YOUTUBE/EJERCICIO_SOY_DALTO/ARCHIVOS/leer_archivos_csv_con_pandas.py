import pandas as pd
#usando la función read_csv para leer el archivo csv
df = pd.read_csv('C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\datos.csv')
df2 = pd.read_csv('C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\datos.csv')
#obtieniendo los datos de la columna nombre
nombres =  (df["nombre"])

#recorrer por cadena

cadena = "0123456789"

obtener_por_elementos = (cadena[2:6])

#ordenando el dataframe por la edad

df_orden_ascendente = df.sort_values("edad")

#ordenando el dataframe de forma descendente

df_orden_descendente = df.sort_values("edad", ascending=False)

#print (df_orden_descendente)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#print (df_concatenado)

#Accediendo a las primeras 3 filas con head()

primeras_filas = df.head(3)

#print (primeras_filas)

#Accediendo a las últimas 3 filas con head()

ultimas_filas = df.tail(3)

#print (ultimas_filas)

#Accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales = df.shape

#print (filas_totales)
#print (columnas_totales)

#obteniendo data estadística del dataframe

df_info = df.describe()

#print (df_info)

#accediendo a la edad de la fila 2 
elemento_especifico_loc = df.loc[2,"edad"]
#print (elemento_especifico_loc)

#accediedno a la edad de la fila 2 con iloc

elementos_especifico_iloc = df.iloc[2,2] #En mi percepción se carga más rápido que loc
#print (elementos_especifico_iloc)

#Accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]
#print (apellidos_loc)

#Accediendo a todos los apellidos con iloc

apellidos_iloc = df.iloc[:,1]
#print(apellidos_iloc)

#accediendo a todos los elementos de las filas de una columna 
apellido = df.iloc[:,1]

#print (apellido)

#accediendo a la fila 3 con loc

fila_3= df.loc[2,:]

#accediendo a la fila 3 con iloc

fila_3= df.iloc[2,:]

#print(fila_3)

#accediendo a filas con edad mayor que 30  con loc

'''mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)'''

#accediendo a filas con edad mayor que 30  con loc

#ejemplo con iloc

indices = df.index[df["edad"] > 30]

mayor_que_30 = df.iloc[indices]
print(mayor_que_30)









