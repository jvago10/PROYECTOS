import csv

with open('C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\datos.csv') as archivo:
    reader = csv.reader(archivo)
    
    for row in reader:
        print(row)





          