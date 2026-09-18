"""Programa que pida el nombre de un alumno, sus 3 notas, y muestre el promedio."""

# Calcula el promedio de 3 notas de un alumno
# Autor: 
 
# --- Entrada ---
nombre = input("Nombre del alumno: ")
nota_1 = float(input("Ingrese Nota 1: "))
nota_2 = float(input("Ingrese Nota 2: "))
nota_3 = float(input("Ingrese Nota 3: "))
 
# --- Proceso ---
promedio = (nota_1 + nota_2 + nota_3) / 3
 
# --- Salida ---
print("")
print("El promedio de", nombre, "es", promedio)
