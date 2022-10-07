import json  

persona={

    "nombre":"Juan",
    "apellido":"Duque",
    "edad":24



} 

#serializamos a json com dumps 
#indent : indentacion 2 espacios 
#objeto_json=json.dumps(persona,indent=2) 

#escribimos el archivo  
with open("persona.json","w") as archivo_json:  
    #archivo_json.write(objeto_json)
    json.dump(persona,archivo_json)

#json.dump es una forma mas sencilla de crear archivos json sin tener que serializar 
# mientras que json.dumps requiere de  serializar los objetos json 
