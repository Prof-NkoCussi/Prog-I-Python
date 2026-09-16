"""Ampliá el programa anterior: que pida dos números y muestre las cuatro operaciones.
Primer número: 10
Segundo número: 4
Suma: 14
Resta: 6
Multiplicación: 40
División: 2.5

Extra 1: agregá la división entera con // y el resto con %. Fijate qué devuelve cada una."""

# Calculadora de cuatro operaciones
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
 
print("")
print("Suma:", numero_1 + numero_2)
print("Resta:", numero_1 - numero_2)
print("Multiplicación:", numero_1 * numero_2)
print("División:", numero_1 / numero_2)

"""
Con 10 y 4 usando int()
Suma: 14
Resta: 6
Multiplicación: 40
División: 2.5
Extra 1

print("División entera:", numero_1 // numero_2)   # da 2
print("Resto:", numero_1 % numero_2)              # da 2
// devuelve cuántas veces entra el segundo número en el primero, sin decimales. % devuelve lo que sobra.
"""
