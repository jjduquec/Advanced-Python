lista_numeros = [1,2,3,4,5,6,7,8]

"""
lista pares nos determina si un numero enviado por parametro 
es par 

la idea de las funciones lambda, es que sean funciones de una sola 
expresión 

de lo contrario, se debe de usar una funcion como tal 



"""
lista_pares = list(filter(lambda numero: numero % 2 ==0, lista_numeros))

print(lista_pares)
