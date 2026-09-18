# 🐍 Programación I — Primeros pasos en Python

Repositorio de actividades para arrancar con Python desde cero: mostrar cosas en pantalla, guardar datos en variables, pedirle datos al usuario y hacer cuentas.

Todos los ejemplos usan situaciones conocidas: el kiosco, la SUBE, las notas del trimestre, el dólar. La idea es que programar se sienta como resolver problemas de todos los días, no como matemática abstracta.

[![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Prof-NkoCussi/Prog-I-Python?quickstart=1)

---

## 🎯 ¿Qué vamos a aprender?

- Qué es Python y para qué se usa.
- Mostrar mensajes con `print()`.
- Escribir comentarios con `#` y con `""" """`.
- Guardar datos en **variables** y elegir buenos nombres.
- Reconocer los **tipos de datos**: `int`, `float`, `str`, `bool`.
- Pedir datos al usuario con `input()`.
- Convertir texto a número con `int()` y `float()`.
- Hacer cuentas: `+`, `-`, `*`, `/`, `//` (división entera) y `%` (resto).
- Leer los mensajes de error y entender qué te están diciendo.
- Ordenar un programa en **Entrada → Proceso → Salida**.

---

## 🚀 Cómo usar este repositorio

### Opción 1: GitHub Codespaces (no instalás nada)

1. Tocá el botón **Open in GitHub Codespaces** de arriba (necesitás cuenta de GitHub).
2. Esperá a que cargue. El entorno ya viene con **Python 3.12** y la extensión de Python para VS Code.
3. Abrí cualquier archivo `.py` y ejecutalo con el botón ▶️ de arriba a la derecha, o desde la terminal:

```bash
python 02_hola.py
```

### Opción 2: En tu compu

Necesitás tener [Python](https://www.python.org/downloads/) instalado.

```bash
git clone https://github.com/Prof-NkoCussi/Prog-I-Python.git
cd Prog-I-Python
python 02_hola.py
```
## 📚 Actividades

Están numeradas en el orden en que conviene hacerlas. Cada una suma algo nuevo a la anterior.

### 1️⃣ Mostrar cosas en pantalla

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`02_hola.py`](02_hola.py) | El clásico "Hola, mundo" | `print()`, comentarios |
| [`03_ficha.py`](03_ficha.py) | Muestra nombre, edad y ciudad en líneas separadas | Varios `print()` |
| [`04_comillas.py`](04_comillas.py) | Experimento: ¿qué cambia con y sin comillas? ⚠️ | Texto vs. variable |
| [`05_cartel.py`](05_cartel.py) | Cartel de precios de un kiosco | Salida ordenada en pantalla |

### 2️⃣ Variables y tipos de datos

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`06_traduccion.py`](06_traduccion.py) | Calcula el total de una compra | Variables y operaciones |
| [`07_saludo.py`](07_saludo.py) | Te pregunta el nombre y te saluda | `input()` |
| [`08_tipos.py`](08_tipos.py) | "Detective de tipos": le pregunta a Python qué es cada dato | `type()`, `int`, `float`, `str`, `bool` |

### 3️⃣ El error más común (y cómo arreglarlo)

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`09_trampa.py`](09_trampa.py) | Intenta sumarle 10 a la edad… y falla ⚠️ | Leer un `TypeError` |
| [`10_arreglado-input.py`](10_arreglado-input.py) | La versión que funciona + tabla de cuándo convertir | `int()`, `float()` |
| [`11_input-variables.py`](11_input-variables.py) | "En 10 años vas a tener…" | `input()` + conversión + cuentas |

### 4️⃣ Programas con cuentas

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`12_suma.py`](12_suma.py) | Suma dos números (sin que dé "128") | Conversión antes de sumar |
| [`13_calculadora.py`](13_calculadora.py) | Las cuatro operaciones con dos números | `+ - * /`, `//`, `%` |
| [`14_area-rectangulo.py`](14_area-rectangulo.py) | Área de un rectángulo | Cuándo usar `float()` |
| [`15_conversor-dolares.py`](15_conversor-dolares.py) | Pesos a dólares | Constantes en MAYÚSCULAS |

### 5️⃣ Encontrar errores

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`16_errores.py`](16_errores.py) | Seis programas rotos para diagnosticar ⚠️ | `NameError`, `TypeError`, `SyntaxError` |

### 6️⃣ Problemas de la vida real

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`17_promedio-notas.py`](17_promedio-notas.py) | Promedio de 3 notas de un alumno | Entrada → Proceso → Salida |
| [`18_sube.py`](18_sube.py) | Cuántos viajes te alcanzan con la SUBE y cuánto sobra | `//` y `%` en un caso real |
| [`19_kiosco-calculo.py`](19_kiosco-calculo.py) | Total y vuelto de una compra, con ticket | Todo junto |

### 7️⃣ Cierre: revisar y crear

| Archivo | Qué hace | Qué practicás |
|---|---|---|
| [`20_mejorado.py`](20_mejorado.py) | Tomás el programa de un compañero (el del kiosco o el de la SUBE) y lo mejorás | Leer código ajeno, proponer mejoras |
| [`21_mi_programa.py`](21_mi_programa.py) | Resolvés un problema real de tu casa, tu barrio o la escuela con un programa propio | Pensar el problema y programarlo de punta a punta |

> 🤝 **Actividad 20:** antes de cambiar nada, leé el programa entero y ejecutalo. Después preguntate: ¿se entienden los nombres de las variables? ¿tiene comentarios? ¿los mensajes son claros para quien lo usa? Dejá un comentario arriba con lo que cambiaste y por qué.
>
> 💡 **Actividad 21:** si no se te ocurre nada, pensá en algo que calcules seguido "de cabeza": cuánto gastás por semana, cuántas horas te faltan para algo, cuánta nafta necesitás para un viaje, cuánto sale dividir una pizza entre amigos.

> ⚠️ **Los archivos marcados con ⚠️ dan error a propósito.** No están mal subidos: la actividad es ejecutarlos, leer el error y entender qué pasó.

---

## 🧩 Cómo está armado cada programa

A partir de la actividad 17, los programas siguen siempre la misma estructura:

```python
# Qué hace el programa
# Autor: tu nombre

# --- Entrada ---
nombre = input("Nombre del alumno: ")
nota = float(input("Nota: "))

# --- Proceso ---
resultado = nota * 2

# --- Salida ---
print("Resultado:", resultado)
```

Separar el programa en estas tres partes ayuda a pensar antes de escribir: **¿qué datos necesito? ¿qué hago con ellos? ¿qué muestro?**

---

## 🆘 Errores que te vas a cruzar

| Error | Qué significa | Ejemplo típico |
|---|---|---|
| `NameError` | Python no conoce ese nombre | Escribiste `Print` en vez de `print`, o `Edad` en vez de `edad` |
| `TypeError` | Estás mezclando tipos que no se pueden combinar | Sumar un texto de `input()` con un número |
| `SyntaxError` | Algo está mal escrito | Te faltó cerrar un paréntesis o unas comillas |
| `ValueError` | El dato no se puede convertir | Escribiste "hola" cuando el programa esperaba un número |

💡 **Tip:** el mensaje de error siempre dice **en qué línea** está el problema. Empezá a buscar por ahí.

---

## ✍️ Para estudiantes

1. Hacé un **fork** de este repositorio (botón *Fork* arriba a la derecha).
2. Resolvé las actividades en tu copia.
3. Completá la línea `# Autor:` con tu nombre en cada archivo.
4. Guardá tus avances con commits que digan qué hiciste, por ejemplo: `Resuelvo actividad 18 - SUBE`.

---

## 👨‍🏫 Autor

**Prof. Nicolás A. Cussi** — [@Prof-NkoCussi](https://github.com/Prof-NkoCussi)

Material para uso educativo. Podés usarlo y adaptarlo para tus clases citando la fuente.
