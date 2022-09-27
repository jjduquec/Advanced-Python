"""
la funcion map es una funcion qeu reemplaza la iteracion de listas a traves de ciclos 
map(function or expression, list) 

map no retorna un elemento iterable, debe de convertirse a map  
"""

lista_num=[1,2,3,4,5,6,7,8] 


resultado=map (lambda x: x+1, lista_num) 

print(list(resultado))



