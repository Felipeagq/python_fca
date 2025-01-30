# 📂 **Manejo de Archivos, Rutas y Sistema en Python**  

El manejo de archivos y rutas en Python es fundamental para trabajar con datos, generar reportes, administrar configuraciones y muchas otras tareas. Python ofrece módulos como `os`, `pathlib`, y `shutil` para manipular archivos y rutas de manera eficiente.

---

# **1️⃣. Manejo de Archivos en Python**  

Python permite trabajar con archivos de texto (`.txt`, `.csv`, `.json`, etc.) y archivos binarios (`.jpg`, `.pdf`, etc.).  

## 🔹 **Apertura y Escritura de Archivos (`open()`)**  
El método `open()` permite abrir un archivo en diferentes modos:  
| Modo  | Descripción |
|--------|------------|
| `"r"`  | Lectura (por defecto) |
| `"w"`  | Escritura (sobrescribe el archivo) |
| `"a"`  | Escritura (agrega al final) |
| `"x"`  | Crea un archivo nuevo |
| `"b"`  | Modo binario (`"wb"`, `"rb"`) |
| `"t"`  | Modo texto (por defecto) |

### **📌 Ejemplo 1: Crear y Escribir un Archivo**
```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de prueba.\n")
    archivo.write("Segunda línea del archivo.")
```
📌 **Explicación**:  
✅ `with open(...)` asegura que el archivo se cierre automáticamente.  
✅ `"w"` crea o sobrescribe el archivo si ya existe.  

### **📌 Ejemplo 2: Leer un Archivo**
```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

### **📌 Ejemplo 3: Leer Línea por Línea**
```python
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # Elimina saltos de línea extra
```

### **📌 Ejemplo 4: Agregar Datos a un Archivo**
```python
with open("archivo.txt", "a") as archivo:
    archivo.write("\nNueva línea agregada al archivo.")
```

---

# **2️⃣. Manejo de Archivos JSON**  
El módulo `json` permite leer y escribir datos en formato JSON.  

### **📌 Ejemplo 5: Guardar un Diccionario en JSON**
```python
import json

datos = {"nombre": "Carlos", "edad": 30, "ciudad": "Bogotá"}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)
```

### **📌 Ejemplo 6: Leer un Archivo JSON**
```python
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print(datos_cargados)
```

---

# **3️⃣. Manejo de Rutas y Archivos con `os` y `pathlib`**  

El módulo `os` y `pathlib` permiten trabajar con rutas y archivos de manera más flexible.  

## 🔹 **Verificar y Crear Directorios**
### **📌 Ejemplo 7: Comprobar si una Carpeta Existe**
```python
import os

if os.path.exists("mi_carpeta"):
    print("La carpeta ya existe.")
else:
    os.mkdir("mi_carpeta")  # Crea la carpeta
    print("Carpeta creada.")
```

## 🔹 **Listar Archivos en un Directorio**
### **📌 Ejemplo 8: Obtener Todos los Archivos de una Carpeta**
```python
import os

archivos = os.listdir(".")  # Obtiene archivos del directorio actual
print(archivos)
```

## 🔹 **Eliminar Archivos y Carpetas**
### **📌 Ejemplo 9: Eliminar un Archivo**
```python
import os

if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")  # Elimina el archivo
    print("Archivo eliminado.")
else:
    print("El archivo no existe.")
```

### **📌 Ejemplo 10: Eliminar una Carpeta**
```python
import shutil

if os.path.exists("mi_carpeta"):
    shutil.rmtree("mi_carpeta")  # Borra la carpeta y su contenido
    print("Carpeta eliminada.")
```

## 🔹 **Obtener Información de Archivos**
### **📌 Ejemplo 11: Obtener el Tamaño de un Archivo**
```python
import os

archivo = "datos.json"
if os.path.exists(archivo):
    tamaño = os.path.getsize(archivo)  # En bytes
    print(f"El archivo {archivo} pesa {tamaño} bytes.")
```

---

# **4️⃣. Ejercicios Prácticos**
✍️ **Ejercicio 1:**  
📌 Escribe un programa que cree un archivo llamado `notas.txt`, solicite al usuario ingresar varias notas y las guarde en el archivo. Luego, debe leer y mostrar las notas guardadas.  

✍️ **Ejercicio 2:**  
📌 Crea un programa que lea un archivo JSON con una lista de tareas pendientes y agregue una nueva tarea ingresada por el usuario.  

✍️ **Ejercicio 3:**  
📌 Crea una función que reciba el nombre de un directorio y liste todos los archivos `.txt` que contiene.  

✍️ **Ejercicio 4:**  
📌 Escribe un programa que elimine todos los archivos con más de 1MB en un directorio específico.  

---

### 🚀 **Conclusión**  
✅ Python ofrece múltiples herramientas (`open()`, `os`, `pathlib`, `shutil`) para manejar archivos y rutas.  
✅ Con `json`, se pueden manejar datos estructurados fácilmente.  
✅ Es fundamental validar si los archivos existen antes de manipularlos.  
