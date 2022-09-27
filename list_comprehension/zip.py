"""
    zip me permite unir elementos de listas  
"""

nombres = ["Paco","Emilio","Javier"]
apellidos = ["Botero","Tafur","Quiñonez"]
#para poder ver el contenido de zip , tene los que convertir el objeto zip en lista
nombre_completo = list(zip(nombres,apellidos))
print(nombre_completo)

"""
   si dos iterables de diferente tamaño se unen a traves de zip,
   la cantidad de tuplas sera en base al iterable que tenga menos elementos 
"""

#desempaquetado de zip  
nombres_unzip,apellidos_unzip= zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

for nombre,apellido in zip (nombres,apellidos):
    print(nombre,apellido)