## Estructuras de control y flujo 

### **1. Estructura básica de `if`**

La estructura básica de una declaración `if` en Python es la siguiente:

```python
if condición:
    # Bloque de código que se ejecuta si la condición es True
```

```python
>>> x = 10
>>> if x > 5:
>>>     print("x es mayor que 5")
x es mayor que 5
```

### **2. Usando `else`**

Si deseas ejecutar un bloque de código alternativo cuando la condición `if` es `False`, puedes usar `else`:

```python
if condición:
    # Bloque de código si la condición es True
else:
    # Bloque de código si la condición es False
```

```python
>>> x = 3
>>> if x > 5:
>>>     print("x es mayor que 5")
>>> else:
>>>     print("x no es mayor que 5")
x no es mayor que 5
```

### **3. Usando `elif` (else if)**

Cuando tienes múltiples condiciones que deseas verificar, puedes usar `elif` para comprobar condiciones adicionales:

```python
if condición1:
    # Bloque de código si condición1 es True
elif condición2:
    # Bloque de código si condición2 es True
else:
    # Bloque de código si todas las condiciones son False
```

```python
>>> x = 10
>>> if x < 5:
>>>     print("x es menor que 5")
>>> elif x == 10:
>>>     print("x es igual a 10")
>>> else:
>>>     print("x es mayor que 5")
x es igual a 10
```

### **4. Anidamiento de `if`**

También puedes usar estructuras `if` dentro de otras estructuras `if` para comprobar condiciones más complejas:

```python
if condición1:
    if condición2:
        # Bloque de código si ambas condiciones son True
    else:
        # Bloque de código si condición1 es True pero condición2 es False
else:
    # Bloque de código si condición1 es False
```

```python
>>> x = 10
>>> y = 20
>>> if x > 5:
>>>     if y > 15:
>>>         print("x es mayor que 5 y y es mayor que 15")
>>>     else:
>>>         print("x es mayor que 5, pero y no es mayor que 15")
>>> else:
>>>     print("x no es mayor que 5")
x es mayor que 5 y y es mayor que 15
```

### **5. Condiciones con operadores lógicos**

Puedes combinar múltiples condiciones utilizando operadores lógicos como `and`, `or`, y `not`.

- **`and`**: Devuelve `True` si ambas condiciones son verdaderas.
- **`or`**: Devuelve `True` si al menos una de las condiciones es verdadera.
- **`not`**: Invierte el valor de la condición.

```python
>>> x = 10
>>> y = 20
>>> if x > 5 and y > 15:
>>>     print("Ambas condiciones son verdaderas")
>>> else:
>>>     print("Una o ambas condiciones son falsas")
Ambas condiciones son verdaderas
```

```python
>>> x = 10
>>> if x < 5 or x > 15:
>>>     print("x está fuera del rango 5-15")
>>> else:
>>>     print("x está dentro del rango 5-15")
x está dentro del rango 5-15
```

### **6. Condiciones con `in` y `not in`**

Puedes usar `in` para comprobar si un elemento está dentro de una secuencia, como una lista o una cadena:

```python
>>> fruits = ['manzana', 'banana', 'cereza']
>>> if 'manzana' in fruits:
>>>     print("La manzana está en la lista")
>>> else:
>>>     print("La manzana no está en la lista")
La manzana está en la lista
```

Y también puedes usar `not in` para comprobar si un elemento **no** está presente:

```python
>>> if 'pera' not in fruits:
>>>     print("La pera no está en la lista")
>>> else:
>>>     print("La pera está en la lista")
La pera no está en la lista
```

---

### **Resumen**
- Usa `if` para verificar una condición.
- Usa `else` para definir el bloque de código que se ejecutará si la condición es `False`.
- Usa `elif` para verificar condiciones adicionales.
- Usa operadores lógicos como `and`, `or`, y `not` para combinar condiciones.

---
---
---
-----

### **1. Estructura básica de un ciclo `for`**

El ciclo `for` en Python se usa para iterar sobre una secuencia (como una lista, cadena, diccionario, etc.):

```python
for item in iterable:
    # Bloque de código que se ejecuta por cada elemento del iterable
```

#### Ejemplo con una lista:

```python
>>> fruits = ['manzana', 'banana', 'cereza']
>>> for fruit in fruits:
>>>     print(fruit)
manzana
banana
cereza
```

### **2. Uso de `range()` para generar una secuencia de números**

`range()` es una función que genera una secuencia de números, que se puede utilizar en el ciclo `for` para iterar un número específico de veces.

#### Sintaxis de `range(start, stop, step)`:
- `start`: El número donde comienza la secuencia (por defecto es 0).
- `stop`: El número donde termina la secuencia (no se incluye).
- `step`: El paso entre cada número (por defecto es 1).

```python
>>> for i in range(3):
>>>     print(i)
0
1
2
```

#### Ejemplo con `range()` y parámetros `start` y `step`:

```python
>>> for i in range(2, 10, 2):
>>>     print(i)
2
4
6
8
```

### **3. Iterar sobre un diccionario**

Cuando usas un `for` para iterar sobre un diccionario, puedes acceder a las claves, valores o ambos.

#### Iterar sobre las claves:

```python
>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> for key in my_dict:
>>>     print(key)
a
b
c
```

#### Iterar sobre los valores:

```python
>>> for value in my_dict.values():
>>>     print(value)
1
2
3
```

#### Iterar sobre claves y valores:

```python
>>> for key, value in my_dict.items():
>>>     print(key, value)
a 1
b 2
c 3
```

### **4. Uso de `break` para salir del ciclo**

Puedes usar la palabra clave `break` para salir de un ciclo `for` antes de que termine todas las iteraciones.

```python
>>> for i in range(5):
>>>     if i == 3:
>>>         break  # Sale del ciclo cuando i es igual a 3
>>>     print(i)
0
1
2
```

### **5. Uso de `continue` para saltar a la siguiente iteración**

La palabra clave `continue` permite saltar a la siguiente iteración del ciclo sin ejecutar el código restante dentro del ciclo.

```python
>>> for i in range(5):
>>>     if i == 3:
>>>         continue  # Salta la iteración cuando i es igual a 3
>>>     print(i)
0
1
2
4
```

### **6. Uso de `else` con el ciclo `for`**

Un ciclo `for` también puede tener una cláusula `else`, que se ejecutará **siempre que el ciclo termine normalmente** (es decir, no se interrumpa con `break`).

```python
>>> for i in range(5):
>>>     print(i)
>>> else:
>>>     print("El ciclo ha terminado correctamente.")
0
1
2
3
4
El ciclo ha terminado correctamente.
```

#### Ejemplo con `break` que evita la ejecución de `else`:

```python
>>> for i in range(5):
>>>     if i == 3:
>>>         break  # Sale del ciclo antes de completarlo
>>>     print(i)
>>> else:
>>>     print("El ciclo ha terminado correctamente.")
0
1
2
```
En este caso, la salida es:
```
0
1
2
```
Y **no se imprime** "El ciclo ha terminado correctamente", porque el ciclo fue interrumpido con `break`.

### **7. Iteración sobre una cadena**

Puedes usar un ciclo `for` para iterar sobre los caracteres de una cadena de texto.

```python
>>> word = "Hola"
>>> for letter in word:
>>>     print(letter)
H
o
l
a
```

---

### **Resumen de sintaxis:**

- **Ciclo `for` básico**: `for item in iterable:`
- **Iterar sobre un rango de números**: `for i in range(start, stop, step):`
- **Iterar sobre claves y valores en un diccionario**: `for key, value in my_dict.items():`
- **Uso de `break`**: Para salir del ciclo antes de que termine.
- **Uso de `continue`**: Para saltar la iteración actual.
- **Uso de `else`**: Para ejecutar código después de que el ciclo termine sin interrupciones.

¡Claro! Aquí tienes ejemplos detallados sobre cómo usar el ciclo `while` en Python:

## ** Estructura básica del ciclo `while`**

El ciclo `while` se ejecuta mientras la condición que se evalúa sea **True**. Cuando la condición es **False**, el ciclo se detiene.

```python
while condición:
    # Bloque de código que se ejecuta mientras la condición sea True
```

#### Ejemplo básico:

```python
>>> count = 0
>>> while count < 5:
>>>     print(count)
>>>     count += 1  # Incrementa el contador
0
1
2
3
4
```

### **2. Uso de `break` para salir del ciclo `while`**

Puedes usar la palabra clave `break` para salir de un ciclo `while` antes de que se cumpla la condición que lo detendría normalmente.

```python
>>> count = 0
>>> while count < 5:
>>>     if count == 3:
>>>         break  # Sale del ciclo cuando count es igual a 3
>>>     print(count)
>>>     count += 1
0
1
2
```

### **3. Uso de `continue` para saltar a la siguiente iteración**

La palabra clave `continue` se usa para saltar el resto del código dentro del ciclo y continuar con la siguiente iteración.

```python
>>> count = 0
>>> while count < 5:
>>>     count += 1
>>>     if count == 3:
>>>         continue  # Salta la iteración cuando count es igual a 3
>>>     print(count)
1
2
4
5
```

### **4. Uso de `else` con el ciclo `while`**

Al igual que con el ciclo `for`, un ciclo `while` puede tener una cláusula `else`. El bloque de código bajo `else` se ejecutará si el ciclo termina de manera natural (es decir, no con un `break`).

```python
>>> count = 0
>>> while count < 5:
>>>     print(count)
>>>     count += 1
>>> else:
>>>     print("El ciclo ha terminado correctamente.")
0
1
2
3
4
El ciclo ha terminado correctamente.
```

#### Ejemplo con `break` que evita la ejecución de `else`:

```python
>>> count = 0
>>> while count < 5:
>>>     if count == 3:
>>>         break  # Sale del ciclo cuando count es igual a 3
>>>     print(count)
>>>     count += 1
>>> else:
>>>     print("El ciclo ha terminado correctamente.")
0
1
2
```

En este caso, la salida es:

```
0
1
2
```

Y **no se imprime** "El ciclo ha terminado correctamente", porque el ciclo fue interrumpido con `break`.

### **5. Uso de ciclos `while` con condiciones complejas**

Puedes combinar múltiples condiciones dentro de un ciclo `while` usando operadores lógicos.

```python
>>> count = 0
>>> while count < 10 and count % 2 == 0:
>>>     print(count)
>>>     count += 2  # Solo imprime números pares
0
2
4
6
8
```

### **6. Ciclo infinito `while`**

Un ciclo `while` puede ejecutarse infinitamente si la condición siempre se evalúa como **True**. Puedes usar un ciclo infinito con un `break` para controlarlo.

```python
>>> while True:
>>>     name = input("¿Cuál es tu nombre? (Escribe 'salir' para terminar): ")
>>>     if name == "salir":
>>>         break  # Sale del ciclo si el usuario escribe 'salir'
>>>     print(f"Hola, {name}!")
```

Este ejemplo pedirá al usuario que ingrese su nombre hasta que escriba "salir".

---

### **Resumen**

- El ciclo `while` se ejecuta mientras una condición sea **True**.
- Usa `break` para salir del ciclo antes de que la condición sea **False**.
- Usa `continue` para saltar una iteración y continuar con la siguiente.
- La cláusula `else` se ejecuta si el ciclo termina de manera natural (sin `break`).
- El ciclo `while` se puede usar con condiciones complejas y en situaciones donde no se sabe cuántas iteraciones se requieren.
