with open ('C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\texto_de_jose.txt', "a", encoding="UTF-8") as archivo:
    
    #Usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregando lineas
        archivo.write(f'Línea {i+1} Agregada con la función "a"\n')
        
