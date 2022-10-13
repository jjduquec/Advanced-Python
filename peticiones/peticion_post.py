"""
    Permite enviar informacion al servidor 

"""


import requests  


#url sacada de : webhoook.site  

url="https://webhook.site/72e6bd40-3841-4e07-a007-d319e7afd5bb" 

payload = {"plato":"pasta","cantidad":2}  
response = requests.post(url, data=payload) 
print(response.status_code)

