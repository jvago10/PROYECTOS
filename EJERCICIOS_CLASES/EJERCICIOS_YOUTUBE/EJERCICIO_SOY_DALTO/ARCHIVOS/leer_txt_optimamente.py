#Abriendo el archivo con with open 

with open("C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\texto_de_jose.txt", encoding="UTF-8") as archivo:
    
    #leemos el contenido
    contenido = archivo.read()
    
    #mostramos el archivo
    
    print(contenido)

#No es necesario cerrarlo al usar with open    
    
    


