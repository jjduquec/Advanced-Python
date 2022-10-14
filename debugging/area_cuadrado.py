def calcular_area_cuadrado(lado): 
    "calcular el area de un cuadrdado" 
    area= lado*lado 
    return area 

lado_cuadrados=[1,2,3] 
area_cuadrados=[] 

for lado in lado_cuadrados: 
    area = calcular_area_cuadrado(lado) 
    area_cuadrados.append(area) 