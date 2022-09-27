"""
es una manera de construir una lista en un elemento iterable con una sola expresion 

lista=[expresion(elemento) for elemento in objeto_iterable] 

los ciclos se definen de tal manera que sean cortos y elegantes 

"""
lista_num=[1,2,3,4,5,6,7,8]
lista_comprenhension=[num**2 for num in lista_num]

#print(lista_comprenhension)



#-----------List comprenhension con condiciones--------------------------------
"""
en este caso, se añaden condiciones para almacenar los elementos dentro de la lista

""" 

def calcular_cuadrado(num):
    return num**2 

def es_par(num):
    return num % 2 ==0


lista_cuadrados=[calcular_cuadrado(num) for num in lista_num if es_par(num)]
lista_resultados=[calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]

#----- set y diccionario list comprenhension 

"""
list comprenhension se puede usar para crear : listas, sets o diccionarios 

"""

set_pares={num for num in lista_num if num %2 == 0}

vocales= "aeiou"
diccionario= {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)


