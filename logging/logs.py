import logging 

#asignamos un nivel de loggin al archivo 
logging.basicConfig(level=logging.DEBUG,filename="ejemplo_logs.log",filemode="w")

# DEBUG : todos los niveles son impresos 
#filename : permite guardar los registros del programa, evita que se impriman los logging en la consola 
#filemode : permite determinar la operacion a efectuar sobre el archivo de logs , w -> escribe, a -> escribe al final

logging.debug("Log de debugging") 
logging.info("log informativo") 
logging.warning("log de adrvertencia") 
logging.error("log de error") 
logging.critical("log de error critico") 

"""
no se imprimen los log debug ni info 
la libreria  usa por defecto los warning,error & critical




"""

