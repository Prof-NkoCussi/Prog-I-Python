"""Escribí un programa que pida el nombre y la edad, y muestre un mensaje como este:
¿Cómo te llamás? Leo Messi
¿Cuántos años tenés? 35
Hola....., en 10 años vas a tener 45 años."""

"""Usar dos variables con nombres claros.
• Convertir la edad con int().
• El mensaje final tiene que salir en una sola línea.
• Comentar el programa arriba."""

# Calcula la edad dentro de 10 años
 
nombre = input("¿Cómo te llamás?:  ")
edad = int(input("¿Cuántos años tenés?:  "))
 
edad_futura = edad + 10
 
print("Hola", nombre + ", en 10 años vas a tener", edad_futura, "años.")



