"""
    La variable args  me permite recibir
    multiples argumentos para una funcion 
    
    *args -> vector

""" 


def calcular_perimetro(*args): 
    perimetro=0 
    for lado in args:  
        perimetro +=lado 
    return perimetro 

perimetro = calcular_perimetro(1,2,3,4,5)

print(perimetro)