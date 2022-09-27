import logging 

#crear un logger personalizado 
logger = logging.getLogger("logger_personalizado")
print(logger) 

logger.warning("Log de advertencia")