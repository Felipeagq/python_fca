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

## Instalación de Python

1. **Descargar Python:** Ve al sitio oficial [https://www.python.org](https://www.python.org) y descarga la versión más reciente para tu sistema operativo.
2. **Instalación:** Sigue las instrucciones de instalación y asegúrate de marcar la opción "Add Python to PATH".
3. **Verificar la instalación:** Abre la terminal o consola y escribe:
   ```bash
   python --version
   ```
   o
   ```bash
   python3 --version
   ```
   Deberías ver la versión instalada.

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
   - Python utiliza indentación para definir bloques de código.
     ```python
     if True:
         print("Esto está dentro del bloque")
     ```
3. **Impresión en pantalla:**
   ```python
   print("Hola, mundo!")
   ```

---

## Declaración de Variables

1. **Asignación de valores:**
   ```python
   nombre = "Juan"
   edad = 25
   ```
2. **Tipos de datos comunes:**
   - Enteros (`int`): `edad = 25`
   - Flotantes (`float`): `pi = 3.14`
   - Cadenas (`str`): `saludo = "Hola"`
   - Booleanos (`bool`): `activo = True`
3. **Cambiar el tipo de una variable:**
   ```python
   numero = "123"
   numero = int(numero)
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

### **for**

Se utiliza para iterar sobre secuencias.

```python
for i in range(5):
    print(i)
```

### **while**

Repite un bloque de código mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
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
```

### **Números**

```python
entero = 10
flotante = 3.14
suma = entero + flotante
print(suma)
```

### **Listas y Tuplas**

- **Lista:** Colección ordenada y mutable.
  ```python
  frutas = ["manzana", "banana", "cereza"]
  frutas.append("naranja")
  print(frutas)
  ```
- **Tupla:** Colección ordenada e inmutable.
  ```python
  numeros = (1, 2, 3)
  print(numeros[1])
  ```

### **Diccionarios y Conjuntos**

- **Diccionario:** Colección de pares clave-valor.
  ```python
  persona = {"nombre": "Ana", "edad": 30}
  print(persona["nombre"])
  ```
- **Conjunto:** Colección no ordenada de elementos únicos.
  ```python
  numeros = {1, 2, 3, 3}
  print(numeros)  # Salida: {1, 2, 3}
  ```

---

## Ejercicios

1. Escribe un programa que pida al usuario su edad y determine si es mayor o menor de edad.
2. Crea una lista de números del 1 al 10 e imprime sólo los números pares.
3. Dado un diccionario con nombres y edades, imprime el nombre de las personas mayores de 18 años.

---

¡Con esto concluye nuestra primera clase! Practica los conceptos y prepara tus dudas para la próxima sesión.

profundiza más en cada tema, agrega funciones y metodos

