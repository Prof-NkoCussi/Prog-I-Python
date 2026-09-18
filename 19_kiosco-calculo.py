"""Un cliente compra alfajores. El programa tiene que pedir el precio unitario, la cantidad y con cuánto
paga, y mostrar el total y el vuelto."""

# Calcula el total de una compra en el kiosco y el vuelto
# Autor: 
 
# --- Entrada ---
precio = float(input("Precio del alfajor: "))
cantidad = int(input("¿Cuántos lleva?: "))
paga_con = float(input("¿Con cuánto paga?: "))
 
# --- Proceso ---
total = precio * cantidad
vuelto = paga_con - total
 
# --- Salida ---
print("")
print("----- TICKET -----")
print("Cantidad:", cantidad)
print("Total a pagar: $", total)
print("Paga con: $", paga_con)
print("Su vuelto: $", vuelto)
print("------------------")
print("¡Gracias por su compra!")
print("")

