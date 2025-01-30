### **Manejo de Excepciones en Python: `try` y `except`**  

En Python, las excepciones ocurren cuando hay un error en la ejecución del programa. Para evitar que el programa se detenga abruptamente, se usa el manejo de excepciones con `try` y `except`.

---

## **1️⃣ Estructura Básica de `try` y `except`**  
```python
try:
    # Código que puede causar un error
    resultado = 10 / 0  # Error: División por cero
except:
    # Código que se ejecuta si hay un error
    print("Ocurrió un error.")
```
🔹 **Salida:** `Ocurrió un error.`  
(El programa no se detiene, sino que maneja la excepción.)

---

## **2️⃣ Capturando un Tipo de Excepción Específico**
Cada error en Python tiene su propia clase de excepción. Podemos capturar errores específicos para manejarlos mejor.

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes ingresar un número válido.")
```
🔹 **Ejemplo de ejecución:**  
- Si el usuario introduce `0` → `No puedes dividir entre cero.`  
- Si el usuario introduce `"abc"` → `Debes ingresar un número válido.`  

---

## **3️⃣ Capturando Múltiples Excepciones en una Línea**
Puedes capturar varios tipos de errores en una sola línea usando una tupla `()`.

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except (ZeroDivisionError, ValueError):
    print("Error: Entrada inválida o división por cero.")
```

---

## **4️⃣ Obteniendo Detalles del Error (`as e`)**
Si queremos ver detalles del error, usamos `as e`.

```python
try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice fuera de rango
except IndexError as e:
    print(f"Error: {e}")
```
🔹 **Salida:** `Error: list index out of range`

---

## **5️⃣ Uso de `else` y `finally`**
- `else`: Se ejecuta solo si **NO** ocurre ningún error.  
- `finally`: Se ejecuta **siempre**, haya error o no.

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print("Todo salió bien, resultado:", resultado)
finally:
    print("Fin del programa.")
```
🔹 **Ejemplo de ejecución:**  
- Si el usuario introduce `2` → `Todo salió bien, resultado: 5.0`  
- Siempre se ejecuta → `Fin del programa.`  

---

## **6️⃣ Creando Excepciones Personalizadas (`raise`)**
Puedes lanzar errores manualmente con `raise`.

```python
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    return "Acceso permitido"

try:
    print(verificar_edad(16))
except ValueError as e:
    print(f"Error: {e}")
```
🔹 **Salida:** `Error: Debes ser mayor de edad.`  

---

✅ **Resumen**  
📌 `try` → Código que puede fallar.  
📌 `except` → Captura y maneja errores.  
📌 `else` → Se ejecuta si no hay errores.  
📌 `finally` → Se ejecuta siempre.  
📌 `raise` → Genera errores personalizados.  

## Ejemplos de Try-Except
Aquí tienes ejemplos de cómo capturar cada excepción en Python usando `try-except`:  

---

## **📌 Errores de Sintaxis y Ejecución**
### **1. TypeError** (Ocurre cuando se usa un tipo de dato incorrecto)
```python
try:
    suma = "5" + 5  # No se puede sumar un str con un int
except TypeError as e:
    print(f"Error: {e}")
```

### **2. ValueError** (Conversión inválida de tipo de dato)
```python
try:
    numero = int("Hola")  # No se puede convertir "Hola" a entero
except ValueError as e:
    print(f"Error: {e}")
```

### **3. NameError** (Variable no definida)
```python
try:
    print(variable_no_definida)
except NameError as e:
    print(f"Error: {e}")
```

### **4. IndexError** (Acceder a un índice fuera de rango)
```python
try:
    lista = [1, 2, 3]
    print(lista[5])  # La lista tiene solo 3 elementos
except IndexError as e:
    print(f"Error: {e}")
```

### **5. KeyError** (Clave inexistente en un diccionario)
```python
try:
    diccionario = {"nombre": "Juan"}
    print(diccionario["edad"])  # No existe la clave "edad"
except KeyError as e:
    print(f"Error: {e}")
```

### **6. ZeroDivisionError** (División entre cero)
```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### **7. AttributeError** (Intentar acceder a un atributo inexistente)
```python
try:
    numero = 10
    numero.append(5)  # Los enteros no tienen el método append()
except AttributeError as e:
    print(f"Error: {e}")
```

### **8. ModuleNotFoundError** (Módulo no encontrado)
```python
try:
    import modulo_inexistente
except ModuleNotFoundError as e:
    print(f"Error: {e}")
```

### **9. ImportError** (Error al importar una función específica)
```python
try:
    from math import raiz_cuadrada  # No existe en el módulo math
except ImportError as e:
    print(f"Error: {e}")
```

### **10. UnboundLocalError** (Usar una variable local antes de asignarla)
```python
try:
    def funcion():
        print(variable)  # Se usa antes de declararla
        variable = 5
    funcion()
except UnboundLocalError as e:
    print(f"Error: {e}")
```

---

## **📌 Errores del Sistema y Archivos**
### **11. OSError** (Error de sistema operativo)
```python
try:
    archivo = open("/ruta/inexistente/archivo.txt", "r")
except OSError as e:
    print(f"Error: {e}")
```

### **12. FileNotFoundError** (Archivo inexistente)
```python
try:
    archivo = open("archivo_no_existe.txt", "r")
except FileNotFoundError as e:
    print(f"Error: {e}")
```

### **13. PermissionError** (No hay permisos para acceder al archivo)
```python
try:
    archivo = open("/etc/shadow", "r")  # Archivo protegido en Linux
except PermissionError as e:
    print(f"Error: {e}")
```

### **14. IsADirectoryError** (Intentar abrir un directorio como archivo)
```python
try:
    archivo = open("C:/Users", "r")  # En Windows, "Users" es un directorio
except IsADirectoryError as e:
    print(f"Error: {e}")
```

### **15. NotADirectoryError** (Intentar acceder a un archivo como si fuera un directorio)
```python
try:
    import os
    os.listdir("archivo.txt")  # archivo.txt no es un directorio
except NotADirectoryError as e:
    print(f"Error: {e}")
```

### **16. MemoryError** (Cuando el sistema se queda sin memoria)
```python
try:
    lista = [1] * (10**10)  # Lista gigante
except MemoryError as e:
    print(f"Error: {e}")
```

### **17. SystemError** (Error interno de Python)
```python
try:
    raise SystemError("Ocurrió un error interno")
except SystemError as e:
    print(f"Error: {e}")
```

### **18. EOFError** (Entrada inesperada de fin de archivo)
```python
try:
    dato = input()  # Si se ejecuta en un entorno sin entrada, dará EOFError
except EOFError as e:
    print(f"Error: {e}")
```

---

## **📌 Errores en Iteraciones y Generadores**
### **19. StopIteration** (Finalización de un iterador)
```python
try:
    iterador = iter([1, 2, 3])
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)  # No hay más elementos
except StopIteration as e:
    print(f"Error: {e}")
```

### **20. GeneratorExit** (Cuando un generador es cerrado)
```python
try:
    def generador():
        try:
            yield 1
        except GeneratorExit:
            print("El generador fue cerrado")
    g = generador()
    next(g)
    g.close()  # Llama a GeneratorExit
except GeneratorExit as e:
    print(f"Error: {e}")
```

---

## **📌 Errores del Usuario y del Entorno**
### **21. KeyboardInterrupt** (Interrupción manual del usuario)
```python
try:
    while True:
        pass  # Presiona Ctrl+C para lanzar KeyboardInterrupt
except KeyboardInterrupt as e:
    print(f"Error: {e}")
```

### **22. SystemExit** (Salir del programa con exit())
```python
try:
    import sys
    sys.exit("Saliendo del programa")  # Provoca SystemExit
except SystemExit as e:
    print(f"Error: {e}")
```

### **23. RecursionError** (Demasiadas llamadas recursivas)
```python
try:
    def recursiva():
        return recursiva()
    recursiva()
except RecursionError as e:
    print(f"Error: {e}")
```

### **24. FloatingPointError** (Error en operaciones de punto flotante)
```python
import sys
try:
    sys.seterr(all="raise")  # Configura Python para que lance excepciones de punto flotante
    resultado = 1.0 / 0.0
except FloatingPointError as e:
    print(f"Error: {e}")
```

---

## **📌 Capturar Todas las Excepciones (No recomendado)**
```python
try:
    x = 1 / 0
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
```

---