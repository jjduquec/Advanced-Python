import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s ",
    datefmt="%H:%M:%S"





)
#parametro format asigna el formato a los logs  
# la s de los parentesis indica que es una string 
nombre="paco" 
logging.error(f"{nombre} creo el error") 
logging.warning("log de advertencia") 
logging.error("log de error") 
logging.critical("log de error critico ")


# los loggs se puede usar en los except blocks  

try: 
    division= 2/0
except: 
    logging.error("Division por cero")
    #una alternativa es logging.exception 
    #logging.exception("Division por cero")
