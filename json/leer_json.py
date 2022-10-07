import json 

with open("persona.json","r") as archivo_json: 
    #cargar el contenido del archivo
    datos_json= json.load(archivo_json) 

print(type(datos_json)) 
#contenido del json  
print(datos_json)

# para acceder a un dato en especifico del json  
# se hace como si fuera un diccionario  
print(datos_json["nombre"])