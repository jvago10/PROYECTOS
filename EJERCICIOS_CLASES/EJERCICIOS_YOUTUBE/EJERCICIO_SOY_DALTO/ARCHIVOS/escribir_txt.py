with open ('C:\PROYECTOS\EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\EJERCICIO_SOY_DALTO\ARCHIVOS\\texto_de_jose.txt', "w", encoding="UTF-8") as archivo:
    
    #Sobreescribir el archivo
    #archivo.write("Hola, soy Jose. Este es mi primer texto.")
    
    
    #Agregando 2 líneas con writelines
    archivo.writelines([" - Hola chaval cómo andas\n", " - mucho tiempo sin verte\n"])
    
    #Agregando 2 líneas con writelines
    archivo.writelines([" - Hola pibe cómo estás\n", " - eres millonario o que\n"])
    