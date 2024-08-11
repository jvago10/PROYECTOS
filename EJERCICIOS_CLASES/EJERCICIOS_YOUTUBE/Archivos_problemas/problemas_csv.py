#cambiar el tipo de datos de una columna
import pandas as pd
df = pd.read_csv("EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas\\datos.csv") # importante que el nombre esté en mayuscula
#print(df)

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de datos del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos "dalto" por "Mi_king"
df['apellido'].replace("dalto", "Mi_king", inplace=True)
#print(df['apellido'])

#Eliminando datos con filas vacías
df = df.dropna()
#print(df)

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)

df.to_csv("EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas\\datos_limpios.csv")

