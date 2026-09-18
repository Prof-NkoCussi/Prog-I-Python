"""Programa que pida el saldo de la SUBE y el precio del boleto, y muestre cuántos viajes 
enteros se pueden hacer y cuánto sobra."""

# Calcula cuántos viajes se pueden hacer con el saldo de la SUBE
# Autor: 
 
# --- Entrada ---
saldo = int(input("Saldo de la SUBE: "))
boleto = int(input("Precio del boleto: "))
 
# --- Proceso ---
viajes = saldo // boleto # Calcula cuántos viajes completos se pueden pagar con el saldo (usando division entera)
sobra = saldo % boleto # Calcula cuánto dinero queda después de pagar los viajes (usando el operador modulo)
 
# --- Salida ---
print("")
print("Te alcanza para", viajes, "viajes.")
print("Te sobran $", sobra)
print("")

#Por qué // y no /: 
"""con / el resultado de 5000 dividido 700 sería 7.142857142857143. 
No existen los 0,14 viajes en colectivo. // descarta la parte decimal y deja solo 
los viajes enteros que se pueden hacer de verdad."""