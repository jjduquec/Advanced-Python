import requests  

#endpoint para obtener informacion  

#response = requests.get("https://api.github.com") 
#print(response) 

#para acceder a los headers de la respuesta se usa response.headers 
# print(response.headers) 

#codigo de la respuesta 
#print(response.status_code) 

# ver datos de la respuesta : content (  retorna en bytes)  o texto  
#print(response.text) 

#ver datos en diccionario : 
#print(response.json()["current_user_url"])


response = requests.get(

    "https://api.github.com/search/repositories", 
    params={"q":"python"} 



) 

data = response.json() 
print(data["total_count"])