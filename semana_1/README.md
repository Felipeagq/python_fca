# Clase de Python - Semana 1

## Introducción

Bienvenidos a la primera semana del curso de Python. Durante esta clase, aprenderás los conceptos básicos necesarios para comenzar a programar en Python. Este lenguaje es conocido por su sencillez y potencia, lo que lo convierte en una excelente opción para principiantes y desarrolladores experimentados.

### Objetivos:

1. Instalar Python y configurar tu entorno de trabajo.
2. Entender la sintaxis básica de Python.
3. Declarar y utilizar variables.
4. Usar estructuras de control de flujo.
5. Trabajar con estructuras de datos básicas.

---

## Instalación de Python en Diferentes Sistemas Operativos

A continuación, se describen los pasos detallados para instalar Python en los sistemas operativos más comunes: **Windows**, **Linux** y **macOS**.

---

### **Instalación en Windows**

1. **Descargar Python**:
   - Accede al sitio oficial de Python: [https://www.python.org](https://www.python.org).
   - Dirígete a la sección de descargas y selecciona la versión recomendada para Windows.

2. **Iniciar el instalador**:
   - Ejecuta el archivo descargado (`python-X.X.X-amd64.exe`).
   - Antes de continuar, marca la opción **"Add Python to PATH"** en la parte inferior del instalador.

3. **Elegir opciones de instalación**:
   - Haz clic en "Customize Installation" para configurar opciones adicionales, o selecciona "Install Now" para usar la configuración predeterminada.
   - Si decides personalizar, incluye las opciones como `pip` (manejador de paquetes) y `tcl/tk` (para GUI).

4. **Completar la instalación**:
   - Una vez terminada, abre la consola de Windows (CMD o PowerShell) y verifica la instalación:
     ```bash
     python --version
     ```
   - También puedes verificar que `pip` esté disponible:
     ```bash
     pip --version
     ```

---

### **Instalación en Linux**

Python suele venir preinstalado en la mayoría de las distribuciones de Linux. Sin embargo, puede ser necesario instalar o actualizar a una versión más reciente.

#### **Distribuciones basadas en Debian (Ubuntu, Mint)**

1. **Actualizar repositorios**:
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Instalar Python**:
   - Para instalar la versión predeterminada:
     ```bash
     sudo apt install python3
     ```
   - Instalar `pip` (administrador de paquetes):
     ```bash
     sudo apt install python3-pip
     ```

3. **Verificar instalación**:
   ```bash
   python3 --version
   pip3 --version
   ```

#### **Distribuciones basadas en Red Hat (Fedora, CentOS)**

1. **Instalar Python y pip**:
   ```bash
   sudo dnf install python3 python3-pip
   ```

2. **Verificar instalación**:
   ```bash
   python3 --version
   pip3 --version
   ```

---

### **Instalación en macOS**

#### **Usando el Instalador Oficial**

1. **Descargar Python**:
   - Visita [https://www.python.org](https://www.python.org) y descarga la versión compatible con macOS.

2. **Ejecutar el instalador**:
   - Abre el archivo `.pkg` descargado y sigue las instrucciones del asistente.
   - Durante la instalación, asegúrate de que se añada Python al sistema.

3. **Verificar instalación**:
   - Abre la terminal y escribe:
     ```bash
     python3 --version
     ```
   - También verifica que `pip` esté disponible:
     ```bash
     pip3 --version
     ```

#### **Usando Homebrew**

1. **Instalar Homebrew** (si no lo tienes):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Instalar Python con Homebrew**:
   ```bash
   brew install python
   ```

3. **Verificar instalación**:
   ```bash
   python3 --version
   pip3 --version
   ```
---
---
---
---
## Sintaxis Básica

1. **Comentarios:**
   - Comentarios de una línea:
     ```python
     # Este es un comentario
     ```
   - Comentarios de múltiples líneas:
     ```python
     """
     Este es un comentario
     de varias líneas
     """
     ```
2. **Indentación:**
   - Python utiliza indentación para definir bloques de código. No usar la indentación correcta genera errores.
     ```python
     if True:
         print("Esto está dentro del bloque")
     ```
3. **Impresión en pantalla:**
   ```python
   print("Hola, mundo!")
   ```
   - **Separadores:** Puedes personalizar la salida usando `sep`.
     ```python
     print("Hola", "Mundo", sep="-")  # Salida: Hola-Mundo
     ```
   - **Fin de línea personalizado:**
     ```python
     print("Hola", end=" ")
     print("Mundo")  # Salida: Hola Mundo
     ```

---

## Declaración de Variables

1. **Asignación de valores:**
   ```python
   nombre = "Juan"
   edad = 25
   ```
   - Python permite reasignar variables a diferentes tipos de datos sin errores.
     ```python
     x = 10
     x = "Texto"
     ```

2. **Tipos de datos comunes:**
   - **Enteros (`int`):**
     ```python
     entero = 42
     ```
   - **Flotantes (`float`):**
     ```python
     flotante = 3.14159
     ```
   - **Cadenas (`str`):**
     ```python
     texto = "Python es genial"
     ```
     - Métodos comunes:
       ```python
       texto = "Hola Mundo"
       print(texto.capitalize())  # Primera letra mayúscula
       print(texto.replace("Hola", "Adios"))  # Reemplazar texto
       print(texto.split())  # Dividir en lista
       ```
   - **Booleanos (`bool`):**
     ```python
     es_mayor = True
     es_menor = False
     ```
3. **Entrada del usuario:**
   ```python
   nombre = input("¿Cómo te llamas? ")
   print(f"Hola, {nombre}!")
   ```

4. **Conversión de tipos:**
   ```python
   edad = input("¿Cuántos años tienes? ")
   edad = int(edad)
   print(edad + 5)  # Incrementar edad en 5
   ```

---

## Estructuras de Control

### **if - else**
Permiten tomar decisiones en función de una condición.

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

- **elif:**
  ```python
  nota = 85
  if nota >= 90:
      print("Sobresaliente")
  elif nota >= 70:
      print("Aprobado")
  else:
      print("Reprobado")
  ```

### **for**
Se utiliza para iterar sobre secuencias como listas, tuplas o cadenas.

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

- **Enumerar índices y elementos:**
  ```python
  for i, fruta in enumerate(frutas):
      print(f"Índice {i}: {fruta}")
  ```

- **Iterar sobre cadenas:**
  ```python
  for letra in "Python":
      print(letra)
  ```

### **while**
Repite un bloque de código mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

- **Evitar bucles infinitos:**
  ```python
  while True:
      respuesta = input("Escribe 'salir' para terminar: ")
      if respuesta == "salir":
          break
  ```

### **break, continue y pass**

- **break:** Sale del bucle actual.
  ```python
  for i in range(10):
      if i == 5:
          break
      print(i)
  ```
- **continue:** Salta a la siguiente iteración.
  ```python
  for i in range(10):
      if i % 2 == 0:
          continue
      print(i)
  ```
- **pass:** No hace nada; se utiliza como un marcador de lugar.
  ```python
  for i in range(5):
      pass
  ```

---

## Estructuras de Datos

### **String (Cadenas de texto)**

```python
texto = "Hola, mundo"
print(texto.upper())  # Convertir a mayúsculas
print(texto.lower())  # Convertir a minúsculas
print(texto[0])       # Acceder al primer carácter
print(texto[-1])      # Acceder al último carácter
print(len(texto))     # Longitud de la cadena
```

### **Números**

```python
entero = 10
flotante = 3.14
suma = entero + flotante
print(round(suma, 2))  # Redondear a 2 decimales
```

### **Listas y Tuplas**

- **Lista:** Colección ordenada y mutable.
  ```python
  frutas = ["manzana", "banana", "cereza"]
  frutas.append("naranja")
  frutas.remove("banana")
  frutas.sort()
  print(frutas)
  ```
- **Tupla:** Colección ordenada e inmutable.
  ```python
  numeros = (1, 2, 3)
  print(numeros[1])
  print(len(numeros))
  ```

### **Diccionarios y Conjuntos**

- **Diccionario:** Colección de pares clave-valor.
  ```python
  persona = {"nombre": "Ana", "edad": 30}
  persona["edad"] = 31  # Actualizar valor
  print(persona.get("nombre"))  # Obtener valor
  ```
- **Conjunto:** Colección no ordenada de elementos únicos.
  ```python
  numeros = {1, 2, 3, 3}
  numeros.add(4)
  numeros.discard(2)
  print(numeros)  # Salida: {1, 3, 4}
  ```

---

## Ejercicios

1. Escribe un programa que pida al usuario su edad y determine si es mayor o menor de edad.
2. Crea una lista de números del 1 al 10 e imprime sólo los números pares.
3. Dado un diccionario con nombres y edades, imprime el nombre de las personas mayores de 18 años.
4. Escribe un programa que invierta el contenido de una cadena usando un bucle.
5. Dada una lista de números, calcula la suma y el promedio de sus elementos.

---

¡Con esto concluye nuestra primera clase! Practica los conceptos y prepara tus dudas para la próxima sesión.

