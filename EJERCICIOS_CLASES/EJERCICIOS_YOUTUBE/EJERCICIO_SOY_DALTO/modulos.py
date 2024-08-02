#Importando un modulo y asignándole el nombre "m_saludar"

#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y le cambiamos el nombre

from modulo_saludar import saludar as saludar_normal, saludar_raro as saludo_makanaki

#creaamos las variables con los saludos

saludo = saludar_normal("José")
saludo_raro = saludo_makanaki("Juancho")

#mostramos los resultados

print(saludo)
print(saludo_raro)

#Para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre desde este modulo

print(__name__)

#accediendo al nombre del modulo llamado
#print(m_saludar.__name__)