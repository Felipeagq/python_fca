# 📌 **Módulos en Python: Creación y Manejo**  

Un **módulo en Python** es simplemente un archivo con extensión `.py` que contiene funciones, clases o variables reutilizables. Los módulos nos ayudan a organizar el código en archivos separados para hacerlo más estructurado y reutilizable.  

---

## **1️⃣ Creación de un Módulo**
Para crear un módulo en Python, simplemente creamos un archivo `.py` con funciones y variables.  

📌 **Ejemplo:** Creamos un archivo llamado `mi_modulo.py` con algunas funciones útiles.

📄 **Archivo:** `mi_modulo.py`
```python
# Este es nuestro módulo personalizado

def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido a Python."

def suma(a, b):
    return a + b

PI = 3.14159  # Una variable dentro del módulo
```

---

## **2️⃣ Importar un Módulo**
Una vez que tenemos un módulo, podemos **importarlo en otro script** y usar sus funciones.  

📌 **Ejemplo:** Usando `mi_modulo.py` en otro archivo.  

📄 **Archivo:** `main.py`
```python
import mi_modulo  # Importamos el módulo

# Usamos la función saludar
print(mi_modulo.saludar("Juan"))

# Usamos la función suma
resultado = mi_modulo.suma(5, 3)
print(f"La suma es: {resultado}")

# Accedemos a la variable PI
print(f"El valor de PI es: {mi_modulo.PI}")
```

### 🔹 **Salida esperada:**
```
¡Hola, Juan! Bienvenido a Python.
La suma es: 8
El valor de PI es: 3.14159
```

---

## **3️⃣ Importar Solo Elementos Específicos**
Si no queremos importar todo el módulo, podemos importar solo ciertas funciones o variables.  

📌 **Ejemplo:** Importamos solo `suma` y `PI` del módulo.
```python
from mi_modulo import suma, PI

print(suma(10, 5))  # 15
print(PI)  # 3.14159
```

---

## **4️⃣ Importar con un Alias (Renombrar el módulo)**
Si el nombre del módulo es muy largo, podemos darle un alias con `as`.  

📌 **Ejemplo:**
```python
import mi_modulo as mod  # Renombramos el módulo

print(mod.saludar("Ana"))  # ¡Hola, Ana! Bienvenido a Python.
```

---

## **5️⃣ Importar Todo con `*` (No recomendado)**
Podemos importar todo el contenido de un módulo con `from ... import *`, pero esto **no es recomendado** porque puede causar conflictos de nombres.

📌 **Ejemplo:**
```python
from mi_modulo import *

print(saludar("Carlos"))  # ¡Hola, Carlos! Bienvenido a Python.
print(suma(2, 3))  # 5
```

⚠️ **Problema:** No sabremos qué funciones o variables provienen del módulo, lo que puede generar confusión.

---

## **6️⃣ Módulos Propios vs. Módulos de Python**
Python viene con **módulos estándar** como `math`, `random`, `os`, etc.  
📌 **Ejemplo con `math`**:
```python
import math

print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
```

---

## **7️⃣ Crear un Paquete con Múltiples Módulos**
Un **paquete** en Python es una carpeta que contiene varios módulos. Para que Python lo reconozca como un paquete, debe incluir un archivo especial llamado `__init__.py`.

📄 **Estructura de archivos:**
```
mi_paquete/
│── __init__.py
│── calculadora.py
│── mensajes.py
```

📄 **Archivo `calculadora.py`**
```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
```

📄 **Archivo `mensajes.py`**
```python
def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido."
```

📄 **Archivo `__init__.py`**
```python
# Indica que esta carpeta es un paquete
```

📄 **Cómo Importar desde el Paquete**
```python
from mi_paquete import calculadora, mensajes

print(calculadora.suma(10, 5))  # 15
print(mensajes.saludar("Lucía"))  # ¡Hola, Lucía! Bienvenido.
```

---

## **8️⃣ Módulos Personalizados vs. Módulos de Terceros**
- ✅ **Módulos Personalizados**: Creación propia (`mi_modulo.py`).
- ✅ **Módulos Estándar de Python**: `math`, `os`, `random`, etc.
- ✅ **Módulos de Terceros**: Librerías externas como `numpy`, `pandas`, `requests`.  
  📌 Se instalan con `pip`:
  ```bash
  pip install requests
  ```
  📌 **Ejemplo:**
  ```python
  import requests
  respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
  print(respuesta.json())
  ```

---

## **🎯 Resumen**
✅ Un **módulo** es un archivo `.py` con funciones reutilizables.  
✅ Se importa con `import nombre_modulo`.  
✅ Podemos importar funciones específicas con `from modulo import funcion`.  
✅ Podemos crear **paquetes** organizando módulos en carpetas con `__init__.py`.  
✅ Python tiene módulos estándar (`math`, `random`, `os`, etc.).  
✅ También hay **módulos de terceros** (`requests`, `numpy`, `pandas`).  

---
## **📌 Diferentes Modulos**
Python ofrece una **gran cantidad de módulos estándar** que facilitan tareas comunes como:
- 📊 **Matemáticas y estadísticas** (`math`, `random`, `statistics`)
- 📅 **Fechas y tiempo** (`datetime`, `time`, `calendar`)
- 📂 **Manejo de archivos** (`os`, `shutil`, `pathlib`)
- 🌍 **Redes e Internet** (`socket`, `urllib`, `http`)
- 🔑 **Seguridad y cifrado** (`hashlib`, `secrets`)
- 🔄 **Procesos y concurrencia** (`threading`, `asyncio`, `multiprocessing`)
- 🧪 **Pruebas y depuración** (`unittest`, `logging`)