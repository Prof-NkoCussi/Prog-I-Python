"""Esta actividad es para que veas el error más común de todos. Queremos que te dé error.
Escribí este programa tal cual y ejecutalo:"""

# Este programa NO funciona. Es a propósito.

edad = input("¿Cuántos años tenés? :  ")
print(edad + 10)

"""
a) El error es TypeError: can only concatenate str (not "int") to str.
b) Línea 3.
c) print(type(edad)) muestra <class 'str'>. La edad quedó guardada como texto, aunque la persona escribió un número.
d) Python no puede sumar un texto con un número. Son dos tipos distintos y la operación no tiene sentido para él. Sería como pedirle que sume la palabra "diecisiete" con el número 10.
"""