# Calcula el área de un rectángulo

base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))
 
area = base * altura
 
print("El área del rectángulo es", area)

"""
Sobre int() o float(): conviene float(), porque una base puede medir 3.5 metros. 
Si usáramos int(), el programa daría error apenas alguien escribe un número con coma.
"""
