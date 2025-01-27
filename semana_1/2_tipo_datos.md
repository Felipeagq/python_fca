# Tipos de Datos en Python

Python cuenta con una variedad de tipos de datos incorporados que permiten manejar diferentes clases de información. A continuación, se describen los principales tipos de datos, junto con sus métodos y funciones asociadas.



---

## **1. Tipo de Dato: Números (Numbers)**

Los tipos de datos numéricos en Python son:

### 1. **Enteros (`int`)**
- Representan números enteros, positivos o negativos, sin parte decimal.
  ```python
  numero_entero = 10
  ```
- **Funciones y métodos útiles:**
  - `abs(x)`: Devuelve el valor absoluto de un número.
    ```python
    print(abs(-10))  # Salida: 10
    ```
  - `int(x)`: Convierte un número o cadena en un entero.
    ```python
    print(int(3.14))  # Salida: 3
    ```
  - `bin(x)`: Devuelve la representación binaria de un número entero.
    ```python
    print(bin(10))  # Salida: '0b1010'
    ```
  - `hex(x)`: Devuelve la representación hexadecimal de un número entero.
    ```python
    print(hex(255))  # Salida: '0xff'
    ```
  - `oct(x)`: Devuelve la representación octal de un número entero.
    ```python
    print(oct(8))  # Salida: '0o10'
    ```
  - `pow(x, y)`: Calcula `x` elevado a la potencia `y`.
    ```python
    print(pow(2, 3))  # Salida: 8
    ```

---

### 2. **Flotantes (`float`)**
- Representan números con parte decimal.
  ```python
  numero_flotante = 3.14
  ```
- **Funciones y métodos útiles:**
  - `round(x, n)`: Redondea `x` a `n` decimales.
    ```python
    print(round(3.14159, 2))  # Salida: 3.14
    ```
  - `float(x)`: Convierte un número o cadena a un flotante.
    ```python
    print(float("10.5"))  # Salida: 10.5
    ```
  - `is_integer()`: Comprueba si un número flotante es un entero.
    ```python
    print(10.0.is_integer())  # Salida: True
    ```

---

### 3. **Números Complejos (`complex`)**
- Representan números en la forma `a + bj`, donde `a` es la parte real y `b` es la parte imaginaria.
  ```python
  numero_complejo = 3 + 4j
  ```
- **Funciones y métodos útiles:**
  - `complex(real, imag)`: Crea un número complejo.
    ```python
    print(complex(3, 4))  # Salida: (3+4j)
    ```
  - `numero.real`: Devuelve la parte real del número complejo.
    ```python
    print((3+4j).real)  # Salida: 3.0
    ```
  - `numero.imag`: Devuelve la parte imaginaria del número complejo.
    ```python
    print((3+4j).imag)  # Salida: 4.0
    ```
  - `abs(x)`: Devuelve la magnitud del número complejo.
    ```python
    print(abs(3+4j))  # Salida: 5.0
    ```

---

### Operaciones Numéricas Comunes
- **Suma:** `+`
  ```python
  resultado = 5 + 3  # Salida: 8
  ```
- **Resta:** `-`
  ```python
  resultado = 10 - 2  # Salida: 8
  ```
- **Multiplicación:** `*`
  ```python
  resultado = 4 * 2  # Salida: 8
  ```
- **División:** `/` (Siempre devuelve un flotante).
  ```python
  resultado = 9 / 2  # Salida: 4.5
  ```
- **División Entera:** `//`
  ```python
  resultado = 9 // 2  # Salida: 4
  ```
- **Módulo:** `%`
  ```python
  resultado = 9 % 2  # Salida: 1
  ```
- **Potencia:** `**`
  ```python
  resultado = 2 ** 3  # Salida: 8
  ```

---

## **2. Tipo de Dato: Cadenas (Strings)**

### Strings (`str`)
- **Descripción:** Secuencia inmutable de caracteres, utilizada para representar texto.

### Métodos de Strings

#### Manipulación Básica
- `capitalize()`: Devuelve una copia de la cadena con el primer carácter en mayúscula.
  ```python
  print("python".capitalize())  # Salida: Python
  ```
- `casefold()`: Devuelve una cadena en minúsculas, útil para comparaciones sin sensibilidad a mayúsculas/minúsculas.
  ```python
  print("ß".casefold())  # Salida: ss
  ```
- `lower()`: Convierte todos los caracteres a minúsculas.
  ```python
  print("HELLO".lower())  # Salida: hello
  ```
- `upper()`: Convierte todos los caracteres a mayúsculas.
  ```python
  print("hello".upper())  # Salida: HELLO
  ```
- `swapcase()`: Cambia mayúsculas por minúsculas y viceversa.
  ```python
  print("Python".swapcase())  # Salida: pYTHON
  ```
- `title()`: Convierte la primera letra de cada palabra a mayúscula.
  ```python
  print("python programming".title())  # Salida: Python Programming
  ```

#### Búsqueda y Reemplazo
- `find(sub)`: Devuelve el índice de la primera aparición de `sub`. Si no se encuentra, devuelve `-1`.
  ```python
  print("hello world".find("world"))  # Salida: 6
  ```
- `index(sub)`: Similar a `find()`, pero lanza una excepción si no encuentra `sub`.
  ```python
  print("hello world".index("world"))  # Salida: 6
  ```
- `replace(old, new)`: Reemplaza todas las apariciones de `old` con `new`.
  ```python
  print("hello world".replace("world", "Python"))  # Salida: hello Python
  ```
- `count(sub)`: Devuelve el número de veces que `sub` aparece en la cadena.
  ```python
  print("banana".count("a"))  # Salida: 3
  ```

#### Dividir y Unir
- `split(sep)`: Divide la cadena en una lista de subcadenas usando el separador `sep`.
  ```python
  print("a,b,c".split(","))  # Salida: ['a', 'b', 'c']
  ```
- `join(iterable)`: Une los elementos de un iterable usando la cadena como separador.
  ```python
  print(",".join(["a", "b", "c"]))  # Salida: a,b,c
  ```
- `partition(sep)`: Divide la cadena en tres partes: antes, el separador y después.
  ```python
  print("hello world".partition(" "))  # Salida: ('hello', ' ', 'world')
  ```

#### Verificación
- `startswith(prefix)`: Verifica si la cadena comienza con `prefix`.
  ```python
  print("hello".startswith("he"))  # Salida: True
  ```
- `endswith(suffix)`: Verifica si la cadena termina con `suffix`.
  ```python
  print("hello".endswith("lo"))  # Salida: True
  ```
- `isalpha()`: Verifica si todos los caracteres son alfabéticos.
  ```python
  print("hello".isalpha())  # Salida: True
  ```
- `isdigit()`: Verifica si todos los caracteres son dígitos.
  ```python
  print("123".isdigit())  # Salida: True
  ```
- `isalnum()`: Verifica si todos los caracteres son alfanuméricos.
  ```python
  print("hello123".isalnum())  # Salida: True
  ```
- `isspace()`: Verifica si todos los caracteres son espacios en blanco.
  ```python
  print("   ".isspace())  # Salida: True
  ```

#### Formateo
- `strip(chars)`: Elimina caracteres al inicio y final de la cadena.
  ```python
  print("  hello  ".strip())  # Salida: hello
  ```
- `ljust(width)`, `rjust(width)`: Justifica la cadena a la izquierda o derecha.
  ```python
  print("hello".ljust(10))  # Salida: 'hello     '
  ```
- `zfill(width)`: Rellena la cadena con ceros a la izquierda hasta alcanzar la longitud `width`.
  ```python
  print("42".zfill(5))  # Salida: 00042
  ```


---

## **3. Tipo de Dato: Listas (`list`)**

### **Definición:**
Una lista es una colección ordenada y mutable.

### **Métodos comunes:**



### **1. `append()` - Añadir un elemento al final de la lista**
```python
>>> my_list = [1, 2, 3]
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
```

### **2. `extend()` - Añadir todos los elementos de un iterable al final de la lista**
```python
>>> my_list.extend([5, 6])
>>> my_list
[1, 2, 3, 4, 5, 6]
```

### **3. `insert()` - Insertar un elemento en una posición específica**
```python
>>> my_list.insert(1, 99)
>>> my_list
[1, 99, 2, 3, 4, 5, 6]
```

### **4. `remove()` - Eliminar la primera aparición de un valor**
```python
>>> my_list.remove(99)
>>> my_list
[1, 2, 3, 4, 5, 6]
```

### **5. `pop()` - Eliminar y devolver el elemento en la posición especificada**
```python
>>> my_list.pop(2)
>>> my_list
[1, 2, 4, 5, 6]
```

### **6. `clear()` - Eliminar todos los elementos de la lista**
```python
>>> my_list.clear()
>>> my_list
[]
```

### **7. `index()` - Devolver el índice de la primera aparición de un valor**
```python
>>> my_list = [1, 2, 3, 4, 2, 5]
>>> my_list.index(2)
1
```

### **8. `count()` - Contar el número de apariciones de un valor**
```python
>>> my_list.count(2)
2
```

### **9. `sort()` - Ordenar los elementos de la lista**
```python
>>> my_list.sort()
>>> my_list
[1, 2, 2, 3, 4, 5]
```

### **10. `reverse()` - Invertir el orden de los elementos**
```python
>>> my_list.reverse()
>>> my_list
[5, 4, 3, 2, 2, 1]
```

### **11. `copy()` - Hacer una copia superficial de la lista**
```python
>>> my_copy = my_list.copy()
>>> my_copy
[5, 4, 3, 2, 2, 1]
```

### **12. `list()` - Convertir un iterable a lista**
```python
>>> list("abc")
['a', 'b', 'c']
```

### **13. List Comprehension - Crear una lista con una expresión**
```python
>>> [x * 2 for x in range(5)]
[0, 2, 4, 6, 8]
```

---

## **4. Tipo de Dato: Tuplas (`tuple`)
### **1. `tuple()` - Crear una tupla a partir de un iterable**
```python
>>> my_tuple = tuple([1, 2, 3])
>>> my_tuple
(1, 2, 3)
```

### **2. `count()` - Contar el número de apariciones de un valor en la tupla**
```python
>>> my_tuple = (1, 2, 2, 3, 2)
>>> my_tuple.count(2)
3
```

### **3. `index()` - Encontrar el índice de la primera aparición de un valor en la tupla**
```python
>>> my_tuple.index(2)
1
```

### **4. Desempaquetado de tupla - Asignar los elementos de la tupla a variables**
```python
>>> my_tuple = (1, 2, 3)
>>> a, b, c = my_tuple
>>> a, b, c
(1, 2, 3)
```

### **5. Acceso a elementos de la tupla por índice**
```python
>>> my_tuple = (1, 2, 3)
>>> my_tuple[1]
2
```

### **6. Slicing (Rebanado) - Obtener una sub-tupla**
```python
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple[1:4]
(2, 3, 4)
```

### **7. Concatenación de tuplas**
```python
>>> tuple1 = (1, 2)
>>> tuple2 = (3, 4)
>>> tuple1 + tuple2
(1, 2, 3, 4)
```

### **8. Repetición de tupla**
```python
>>> my_tuple = (1, 2)
>>> my_tuple * 3
(1, 2, 1, 2, 1, 2)
```

### **9. Longitud de la tupla**
```python
>>> my_tuple = (1, 2, 3)
>>> len(my_tuple)
3
```

### **10. Verificación de pertenencia (`in` y `not in`)**
```python
>>> my_tuple = (1, 2, 3)
>>> 2 in my_tuple
True
>>> 5 not in my_tuple
True
```

### **11. Tuplas anidadas - Tuplas dentro de tuplas**
```python
>>> my_tuple = (1, (2, 3), 4)
>>> my_tuple[1]
(2, 3)
>>> my_tuple[1][0]
2
```

### **12. Rebanado negativo - Obtener elementos desde el final de la tupla**
```python
>>> my_tuple = (1, 2, 3, 4, 5)
>>> my_tuple[-2:]
(4, 5)
```



---

## **5. Tipo de Dato: Diccionarios (`dict`)


### **1. `dict()` - Crear un diccionario**
```python
>>> my_dict = dict(a=1, b=2, c=3)
>>> my_dict
{'a': 1, 'b': 2, 'c': 3}
```

### **2. `get()` - Obtener el valor de una clave (si no existe, devuelve `None` o un valor predeterminado)**
```python
>>> my_dict.get('b')
2
>>> my_dict.get('d', 'Clave no encontrada')
'Clave no encontrada'
```

### **3. `keys()` - Obtener las claves del diccionario**
```python
>>> my_dict.keys()
dict_keys(['a', 'b', 'c'])
```

### **4. `values()` - Obtener los valores del diccionario**
```python
>>> my_dict.values()
dict_values([1, 2, 3])
```

### **5. `items()` - Obtener los pares clave-valor del diccionario**
```python
>>> my_dict.items()
dict_items([('a', 1), ('b', 2), ('c', 3)])
```

### **6. `update()` - Actualizar el diccionario con otro diccionario o con pares clave-valor**
```python
>>> my_dict.update({'d': 4, 'e': 5})
>>> my_dict
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

### **7. `pop()` - Eliminar una clave y devolver su valor**
```python
>>> my_dict.pop('b')
2
>>> my_dict
{'a': 1, 'c': 3, 'd': 4, 'e': 5}
```

### **8. `popitem()` - Eliminar y devolver el último par clave-valor (en versiones anteriores de Python, eliminaba un par aleatorio)**
```python
>>> my_dict.popitem()
('e', 5)
>>> my_dict
{'a': 1, 'c': 3, 'd': 4}
```

### **9. `clear()` - Eliminar todos los elementos del diccionario**
```python
>>> my_dict.clear()
>>> my_dict
{}
```

### **10. `setdefault()` - Obtener el valor de una clave, o establecerlo si no existe**
```python
>>> my_dict = {'a': 1, 'b': 2}
>>> my_dict.setdefault('b', 99)
2
>>> my_dict.setdefault('c', 3)
3
>>> my_dict
{'a': 1, 'b': 2, 'c': 3}
```

### **11. `del` - Eliminar una clave del diccionario**
```python
>>> del my_dict['a']
>>> my_dict
{'b': 2, 'c': 3}
```

### **12. `copy()` - Crear una copia superficial del diccionario**
```python
>>> my_copy = my_dict.copy()
>>> my_copy
{'b': 2, 'c': 3}
```

### **13. `fromkeys()` - Crear un nuevo diccionario con claves especificadas y un valor predeterminado**
```python
>>> my_dict = dict.fromkeys(['a', 'b', 'c'], 0)
>>> my_dict
{'a': 0, 'b': 0, 'c': 0}
```

### **14. Comprobación de existencia de clave**
```python
>>> my_dict = {'a': 1, 'b': 2}
>>> 'a' in my_dict
True
>>> 'c' not in my_dict
True
```

### **15. Acceso a valores mediante claves**
```python
>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> my_dict['b']
2
```


---

## **6. Tipo de Dato: Conjuntos (`set`)

### **Definición:**
Un conjunto es una colección no ordenada de elementos únicos.

### **1. `set()` - Crear un conjunto a partir de un iterable**
```python
>>> my_set = set([1, 2, 3, 4])
>>> my_set
{1, 2, 3, 4}
```

### **2. `add()` - Añadir un elemento al conjunto**
```python
>>> my_set.add(5)
>>> my_set
{1, 2, 3, 4, 5}
```

### **3. `remove()` - Eliminar un elemento del conjunto (lanza un error si no existe)**
```python
>>> my_set.remove(3)
>>> my_set
{1, 2, 4, 5}
```

### **4. `discard()` - Eliminar un elemento del conjunto (no lanza error si no existe)**
```python
>>> my_set.discard(2)
>>> my_set
{1, 4, 5}
>>> my_set.discard(10)  # No lanza error si el elemento no existe
>>> my_set
{1, 4, 5}
```

### **5. `pop()` - Eliminar y devolver un elemento aleatorio del conjunto**
```python
>>> my_set.pop()
1  # El valor que devuelve depende del orden interno del set
>>> my_set
{4, 5}
```

### **6. `clear()` - Eliminar todos los elementos del conjunto**
```python
>>> my_set.clear()
>>> my_set
set()
```

### **7. `union()` - Obtener la unión de dos conjuntos (elementos únicos de ambos conjuntos)**
```python
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> set1.union(set2)
{1, 2, 3, 4, 5}
```

### **8. `|` - Operador de unión de conjuntos**
```python
>>> set1 | set2
{1, 2, 3, 4, 5}
```

### **9. `intersection()` - Obtener la intersección de dos conjuntos (elementos comunes)**
```python
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> set1.intersection(set2)
{3}
```

### **10. `&` - Operador de intersección de conjuntos**
```python
>>> set1 & set2
{3}
```

### **11. `difference()` - Obtener la diferencia entre dos conjuntos (elementos de un conjunto que no están en el otro)**
```python
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> set1.difference(set2)
{1, 2}
```

### **12. `-` - Operador de diferencia de conjuntos**
```python
>>> set1 - set2
{1, 2}
```

### **13. `symmetric_difference()` - Obtener la diferencia simétrica entre dos conjuntos (elementos que están en uno u otro, pero no en ambos)**
```python
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> set1.symmetric_difference(set2)
{1, 2, 4, 5}
```

### **14. `^` - Operador de diferencia simétrica de conjuntos**
```python
>>> set1 ^ set2
{1, 2, 4, 5}
```

### **15. `issubset()` - Comprobar si el conjunto es un subconjunto de otro**
```python
>>> set1 = {1, 2}
>>> set2 = {1, 2, 3, 4}
>>> set1.issubset(set2)
True
```

### **16. `<=` - Operador de subconjunto**
```python
>>> set1 <= set2
True
```

### **17. `issuperset()` - Comprobar si el conjunto es un superconjunto de otro**
```python
>>> set2.issuperset(set1)
True
```

### **18. `>=` - Operador de superconjunto**
```python
>>> set2 >= set1
True
```

### **19. `isdisjoint()` - Comprobar si dos conjuntos no tienen elementos en común**
```python
>>> set1 = {1, 2, 3}
>>> set2 = {4, 5, 6}
>>> set1.isdisjoint(set2)
True
```

### **20. `len()` - Obtener la cantidad de elementos en el conjunto**
```python
>>> len(my_set)
3
```

### **21. `in` - Verificar si un elemento está en el conjunto**
```python
>>> 3 in my_set
True
>>> 6 in my_set
False
```

### **22. `copy()` - Crear una copia superficial del conjunto**
```python
>>> set1 = {1, 2, 3}
>>> set_copy = set1.copy()
>>> set_copy
{1, 2, 3}
```


---

## **7. Tipo de Dato: Booleanos (`bool`)

### **Definición:**
El tipo de datos `bool` en Python es muy sencillo y se usa para representar valores de verdad: `True` y `False`. Las operaciones lógicas y las comparaciones son la base para trabajar con este tipo de datos.

### **1. `bool()` - Convertir un valor a tipo booleano**
```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool("Hello")
True
>>> bool("")
False
>>> bool(None)
False
```

### **2. Comparaciones - Operaciones que devuelven un valor booleano**
```python
>>> 5 > 3
True
>>> 5 == 3
False
>>> 5 != 3
True
>>> 5 <= 3
False
>>> 5 >= 3
True
```

### **3. `and` - Operador lógico "y" (devuelve `True` solo si ambos son `True`)**
```python
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
```

### **4. `or` - Operador lógico "o" (devuelve `True` si al menos uno es `True`)**
```python
>>> True or True
True
>>> True or False
True
>>> False or False
False
```

### **5. `not` - Operador lógico "no" (invierte el valor booleano)**
```python
>>> not True
False
>>> not False
True
```

### **6. Verificación de igualdad con `==`**
```python
>>> True == True
True
>>> False == True
False
>>> False == False
True
```

### **7. Negación con `!=`**
```python
>>> True != False
True
>>> False != False
False
```

---
---
---

En Python, la declaración de variables es muy sencilla, ya que no se requiere especificar el tipo de datos, ya que Python es un lenguaje de tipado dinámico. Aquí te dejo un resumen con ejemplos de cómo declarar y trabajar con variables en Python:

### **1. Asignación de una variable**
```python
>>> x = 5  # Asignación de un número entero a una variable
>>> name = "John"  # Asignación de una cadena de texto
>>> is_active = True  # Asignación de un valor booleano
```

### **2. Asignación múltiple en una sola línea**
```python
>>> a, b, c = 1, 2, 3  # Asignación de valores a múltiples variables
>>> a, b = b, a  # Intercambio de valores de variables
```

### **3. Asignación de un valor por defecto con `None`**
```python
>>> result = None  # Asignación de None como valor por defecto
>>> print(result)
None
```

### **4. Reasignación de valores a variables**
```python
>>> x = 10  # Reasignación de valor a una variable existente
>>> x = "Nuevo valor"
>>> x
'Nuevo valor'
```

### **5. Declaración de variables de tipo contenedor**
```python
>>> my_list = [1, 2, 3]  # Lista
>>> my_dict = {"key": "value"}  # Diccionario
>>> my_tuple = (1, 2, 3)  # Tupla
>>> my_set = {1, 2, 3}  # Conjunto (set)
```


### **6. Tipo dinámico de las variables**
```python
>>> x = 42  # Variable de tipo entero
>>> type(x)
<class 'int'>

>>> x = "Hola"  # Ahora, x es una cadena de texto
>>> type(x)
<class 'str'>
```

---
