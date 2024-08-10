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

print (ultimas_filas)






