
"""
El orden de los parametros de una funcion son:  
Parametros propios, 
*args 
**kwargs  

de lo contrario, tendremos error


"""

def parametros_ordenados(nomnbre,apellido,*args,**kwargs): 
    pass 

def parametros_desordenados(nombre, apellido,**kwargs,*args):
    pass

