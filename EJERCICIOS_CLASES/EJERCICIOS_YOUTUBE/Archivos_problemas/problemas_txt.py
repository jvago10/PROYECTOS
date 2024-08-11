#2 listas, una con nombres y otra con apellidos
nombres = ["Lucas", "Matías", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zong", "Dalto", "Robertix","Mongol"]

#registrar esta informacion en un TXT de forma óptima

with open("EJERCICIOS_CLASES/EJERCICIOS_YOUTUBE/archivos_problemas/nombres y apellidos.txt","w", encoding="UTF-8") as arch:
    arch.writelines("Los datos son: \n \n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n--------------\n') for n,a in zip(nombres,apellidos)]