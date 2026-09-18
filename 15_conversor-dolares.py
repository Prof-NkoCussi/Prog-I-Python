"""Programa que pida una cantidad de pesos y muestre a cuántos dólares equivale.
La cotización va como constante al principio del programa, con un comentario:"""

# Conversor de pesos a dólares
# Autor: 
 
COTIZACION = 1550   # pesos por dólar (actualizar cuando cambie)
 
pesos = float(input("¿Cuántos pesos querés convertir? "))
 
dolares = pesos / COTIZACION
 
print("$", pesos, "equivalen a US$", dolares)

#Por qué es constante: 
"""porque no la decide el usuario del programa, la decide 
el que escribe el programa. Es un valor que se mantiene fijo durante toda la ejecución. 
Si el usuario pudiera ingresarla, cada uno podría poner la cotización que quisiera y 
el programa perdería sentido."""