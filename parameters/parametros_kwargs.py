"""
los parametros kwargs  
son parametros que no estan declarados 
pero se pueden enviar a traves de un diccionario 

variable: **kwargs 

resultado:  

{'nombre':'paco'}

"""

def funcion_kwargs(**kwargs): 
    print(kwargs) 
    for llave,valor in kwargs.items(): 
        print(kwargs["nombre"],kwargs["apellido"])


funcion_kwargs(nombre='paco',apellido="botero")