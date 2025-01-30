Aquí tienes una serie de **ejercicios de Python** divididos por dificultad. ¡Intenta resolverlos y me dices si necesitas ayuda! 🚀  

---

## 🟢 **Ejercicios Básicos**
### 1️⃣ **Par o Impar**  
Escribe un programa que solicite un número al usuario y determine si es par o impar.  
🔹 **Entrada:** `4`  
🔹 **Salida:** `El número 4 es par.`  

### 2️⃣ **Suma de Números**  
Solicita dos números al usuario y muestra su suma.  
🔹 **Entrada:** `3, 5`  
🔹 **Salida:** `La suma es 8.`  

### 3️⃣ **Factorial de un Número**  
Escribe una función que calcule el factorial de un número.  
🔹 **Entrada:** `5`  
🔹 **Salida:** `El factorial de 5 es 120.`  

```python
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
print(f"El factorial de {numero} es {factorial(numero)}")
```

---

## 🟡 **Ejercicios Intermedios**
### 4️⃣ **Lista de Números Pares**  
Crea una función que reciba un número `n` y retorne una lista con los números pares hasta `n`.  
🔹 **Entrada:** `10`  
🔹 **Salida:** `[2, 4, 6, 8, 10]`  

### 5️⃣ **Palíndromo**  
Escribe un programa que determine si una palabra es un palíndromo (se lee igual al derecho y al revés).  
🔹 **Entrada:** `"radar"`  
🔹 **Salida:** `Es un palíndromo.`  

```python
def es_palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("Ingresa una palabra: ").lower()
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
```

### 6️⃣ **Adivina el Número**  
Crea un programa donde el usuario debe adivinar un número generado aleatoriamente entre 1 y 100.  

```python
import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-100): "))
    intentos += 1
    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break
```

---

## 🔴 **Ejercicios Avanzados**
### 7️⃣ **Gestor de Contactos (POO)**  
Crea una clase `Contacto` con los atributos `nombre`, `teléfono` y `correo`. Luego, crea una clase `Agenda` que permita:  
- Agregar contactos  
- Buscar contactos  
- Mostrar todos los contactos  

```python
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.correo}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        self.contactos.append(Contacto(nombre, telefono, correo))

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

agenda = Agenda()
agenda.agregar_contacto("Carlos", "123456", "carlos@email.com")
agenda.mostrar_contactos()
```

### 8️⃣ **Contar Palabras en un Archivo**  
Escribe un programa que lea un archivo `.txt` y cuente la cantidad de veces que aparece cada palabra.  

```python
from collections import Counter

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read().lower().split()

conteo_palabras = Counter(contenido)

for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra}: {cantidad}")
```

---

Aquí tienes algunos **ejercicios avanzados de Python** con aplicaciones reales. Cada ejercicio incluye su enunciado y la solución detallada.  

---

# 🏦 **1. Sistema de Gestión de Cuentas Bancarias (POO, Archivos)**
**Escenario:** Un banco necesita un sistema que permita administrar cuentas bancarias.  
**Requisitos:**  
- Crear una clase `CuentaBancaria` con atributos `titular`, `saldo` y `numero_cuenta`.  
- Métodos: `depositar()`, `retirar()`, `mostrar_saldo()`.  
- Guardar las transacciones en un archivo `transacciones.txt`.  

## ✅ **Solución:**
```python
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        self.registrar_transaccion(f"Depósito de ${cantidad}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            self.registrar_transaccion(f"Retiro de ${cantidad}")

    def mostrar_saldo(self):
        return f"Saldo actual: ${self.saldo}"

    def registrar_transaccion(self, mensaje):
        with open("transacciones.txt", "a") as archivo:
            archivo.write(f"Cuenta {self.numero_cuenta}: {mensaje}\n")

# Uso
cuenta = CuentaBancaria("Juan Pérez", "123456789", 500)
cuenta.depositar(200)
cuenta.retirar(100)
print(cuenta.mostrar_saldo())
```

---

# 📦 **2. Inventario de Productos (POO, Diccionarios, JSON)**
**Escenario:** Una tienda necesita administrar su inventario de productos.  
**Requisitos:**  
- Crear una clase `Producto` con `nombre`, `precio`, `cantidad`.  
- Crear una clase `Inventario` con métodos para `agregar_producto()`, `vender_producto()`, `guardar_inventario()`, `cargar_inventario()`.  
- Guardar y cargar el inventario en un archivo `inventario.json`.  

## ✅ **Solución:**
```python
import json

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad):
        if cantidad > self.cantidad:
            print("Stock insuficiente")
        else:
            self.cantidad -= cantidad

    def to_dict(self):
        return {"nombre": self.nombre, "precio": self.precio, "cantidad": self.cantidad}

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio, cantidad):
        if nombre in self.productos:
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, precio, cantidad)

    def vender_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre].vender(cantidad)
        else:
            print("Producto no encontrado")

    def guardar_inventario(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f)

    def cargar_inventario(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {k: Producto(v["nombre"], v["precio"], v["cantidad"]) for k, v in data.items()}
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")

# Uso
inventario = Inventario()
inventario.cargar_inventario()
inventario.agregar_producto("Laptop", 800, 5)
inventario.vender_producto("Laptop", 2)
inventario.guardar_inventario()
```

---

# 📅 **3. Sistema de Gestión de Tareas (FastAPI, SQLite)**
**Escenario:** Una empresa quiere gestionar tareas con una API.  
**Requisitos:**  
- Crear un API con **FastAPI** que permita **crear, obtener y eliminar tareas**.  
- Utilizar **SQLite** como base de datos.  

## ✅ **Solución:**
### 🔹 **Instalar dependencias:**  
```bash
pip install fastapi uvicorn sqlite3
```

### 🔹 **Código con FastAPI:**
```python
from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Conectar a la base de datos
conn = sqlite3.connect("tareas.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tareas (id INTEGER PRIMARY KEY, nombre TEXT, estado TEXT)")
conn.commit()

@app.post("/tareas/")
def agregar_tarea(nombre: str):
    cursor.execute("INSERT INTO tareas (nombre, estado) VALUES (?, 'pendiente')", (nombre,))
    conn.commit()
    return {"mensaje": "Tarea agregada"}

@app.get("/tareas/")
def obtener_tareas():
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    return {"tareas": tareas}

@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
    conn.commit()
    return {"mensaje": "Tarea eliminada"}

# Correr el servidor con: uvicorn script:app --reload
```

---

# 🎥 **4. Descargador de Videos de YouTube (Automatización)**
**Escenario:** Un usuario quiere descargar videos de YouTube mediante un script de Python.  
**Requisitos:**  
- Pedir la URL de un video de YouTube.  
- Descargarlo en formato MP4 usando `pytube`.  

## ✅ **Solución:**
### 🔹 **Instalar pytube:**  
```bash
pip install pytube
```

### 🔹 **Código:**
```python
from pytube import YouTube

def descargar_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print(f"Video descargado: {yt.title}")

# Uso
url = input("Ingresa la URL del video de YouTube: ")
descargar_video(url)
```

---

# 🏥 **5. Análisis de Datos de Pacientes (Pandas, CSV)**
**Escenario:** Un hospital necesita analizar datos de pacientes almacenados en un CSV.  
**Requisitos:**  
- Cargar un archivo CSV con datos de pacientes.  
- Filtrar pacientes mayores de 60 años.  
- Calcular el promedio de presión arterial.  

## ✅ **Solución:**
### 🔹 **Instalar Pandas:**  
```bash
pip install pandas
```

### 🔹 **Código:**
```python
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("pacientes.csv")

# Filtrar pacientes mayores de 60 años
mayores_60 = df[df["edad"] > 60]

# Calcular el promedio de presión arterial
promedio_presion = df["presion_arterial"].mean()

print(f"Pacientes mayores de 60 años:\n{mayores_60}")
print(f"Promedio de presión arterial: {promedio_presion}")
```

---

# 📌 **¿Necesitas más desafíos?**  
Dime qué tipo de problemas te gustaría resolver: **IA, APIs, Web Scraping, Blockchain, Finanzas, Seguridad, Automatización, etc.** 🚀