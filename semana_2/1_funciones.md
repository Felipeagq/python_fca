# Funciones
En Python, las funciones son bloques de código reutilizables que se ejecutan cuando se llaman. Se pueden dividir en tres tipos principales:

1. **Funciones definidas por el usuario**: Son aquellas que el programador crea según sus necesidades.
2. **Funciones lambda (anónimas)**: Son funciones pequeñas y rápidas que se definen en una sola línea.
3. **Funciones integradas (built-in)**: Vienen predefinidas en Python.


---

### **1. Funciones Definidas por el Usuario**
Los programadores pueden definir sus propias funciones usando la palabra clave `def`.

```python
def nombre_de_la_funcion(parametros):
    """Docstring opcional: Explica qué hace la función"""
    # Bloque de código
    return resultado  # (Opcional) Devuelve un valor
```

#### **Ejemplo de una función simple**
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")  # Salida: Hola, Juan!
```

#### **Ejemplo con parámetros y retorno de valor**
```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)  # Salida: 8
```

#### **Valores por defecto en parámetros**
```python
def presentacion(nombre="Invitado"):
    print(f"Bienvenido, {nombre}!")

presentacion()  # Salida: Bienvenido, Invitado!
presentacion("Carlos")  # Salida: Bienvenido, Carlos!
```

#### **Funciones con múltiples argumentos (`*args`)**
```python
def suma_total(*numeros):
    return sum(numeros)

print(suma_total(1, 2, 3, 4))  # Salida: 10
```

#### **Funciones con argumentos clave (`**kwargs`)**
```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Bogotá")
```
**Salida**:
```
nombre: Ana
edad: 25
ciudad: Bogotá
```

## **2️⃣ Elementos de una Función**
1. **`def`**: Palabra clave para definir una función.
2. **Nombre**: Identificador de la función, siguiendo las reglas de nombres de Python.
3. **Parámetros (Opcional)**: Valores que la función puede recibir.
4. **Docstring (Opcional)**: Comentario en `"""triple comillas"""` explicando su propósito.
5. **Cuerpo**: Código que se ejecuta dentro de la función.
6. **`return` (Opcional)**: Devuelve un valor (si no se usa, la función devuelve `None`).

---

### **2. Funciones Lambda (Anónimas)**
Son funciones pequeñas y rápidas que se escriben en una sola línea.

#### **Ejemplo de función lambda simple**
```python
doblar = lambda x: x * 2
print(doblar(5))  # Salida: 10
```

#### **Lambda con múltiples parámetros**
```python
suma = lambda a, b: a + b
print(suma(3, 7))  # Salida: 10
```

#### **Uso con `map()`**
```python
numeros = [1, 2, 3, 4]
doblados = list(map(lambda x: x * 2, numeros))
print(doblados)  # Salida: [2, 4, 6, 8]
```

#### **Uso con `filter()`**
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]
```

---

Python proporciona una serie de **funciones integradas** (*built-in functions*) que están disponibles sin necesidad de importar módulos adicionales. A continuación, te presento una lista completa de todas las funciones integradas en Python con su descripción y ejemplos.

---

## **Funciones de Conversión de Tipos**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `bool(x)` | Convierte `x` a booleano (`True` o `False`). | `bool(0)  # False` |
| `int(x)` | Convierte `x` a un entero. | `int("10")  # 10` |
| `float(x)` | Convierte `x` a flotante. | `float("3.14")  # 3.14` |
| `complex(real, imag)` | Crea un número complejo. | `complex(1, 2)  # (1+2j)` |
| `str(x)` | Convierte `x` en cadena de texto. | `str(100)  # "100"` |
| `list(iterable)` | Convierte `iterable` en lista. | `list("abc")  # ['a', 'b', 'c']` |
| `tuple(iterable)` | Convierte `iterable` en tupla. | `tuple([1, 2, 3])  # (1, 2, 3)` |
| `set(iterable)` | Convierte `iterable` en un conjunto (elimina duplicados). | `set([1, 2, 2, 3])  # {1, 2, 3}` |
| `dict(iterable)` | Convierte `iterable` en un diccionario. | `dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}` |
| `frozenset(iterable)` | Crea un conjunto inmutable. | `frozenset([1, 2, 3])` |
| `bytes(iterable)` | Convierte `iterable` en bytes. | `bytes("hola", "utf-8")` |
| `bytearray(iterable)` | Crea un `bytearray` modificable. | `bytearray("hola", "utf-8")` |
| `memoryview(obj)` | Crea una vista de memoria de un objeto. | `memoryview(b"hola")` |

---

## **Funciones Matemáticas**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `abs(x)` | Devuelve el valor absoluto de `x`. | `abs(-5)  # 5` |
| `round(x, n)` | Redondea `x` a `n` decimales. | `round(3.14159, 2)  # 3.14` |
| `pow(x, y, mod)` | Calcula `x` elevado a `y` con módulo opcional. | `pow(2, 3)  # 8` |
| `min(iterable)` | Devuelve el mínimo de una secuencia. | `min([3, 1, 4])  # 1` |
| `max(iterable)` | Devuelve el máximo de una secuencia. | `max([3, 1, 4])  # 4` |
| `sum(iterable)` | Suma los elementos de un iterable. | `sum([1, 2, 3])  # 6` |
| `divmod(x, y)` | Retorna `(x // y, x % y)`. | `divmod(10, 3)  # (3, 1)` |

---

## **Funciones sobre Iterables**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `len(iterable)` | Retorna la longitud de un iterable. | `len("Hola")  # 4` |
| `sorted(iterable, key, reverse)` | Retorna una lista ordenada. | `sorted([3, 1, 2])  # [1, 2, 3]` |
| `reversed(iterable)` | Retorna un iterador en orden inverso. | `list(reversed([1, 2, 3]))  # [3, 2, 1]` |
| `enumerate(iterable, start)` | Retorna un iterador con índice y valor. | `list(enumerate("abc"))  # [(0, 'a'), (1, 'b'), (2, 'c')]` |
| `zip(*iterables)` | Une múltiples iterables en tuplas. | `list(zip([1, 2], ["a", "b"]))  # [(1, 'a'), (2, 'b')]` |
| `map(func, iterable)` | Aplica una función a cada elemento. | `list(map(str.upper, "abc"))  # ['A', 'B', 'C']` |
| `filter(func, iterable)` | Filtra los elementos según una función. | `list(filter(lambda x: x > 2, [1, 2, 3]))  # [3]` |
| `all(iterable)` | Retorna `True` si todos los elementos son `True`. | `all([True, True, False])  # False` |
| `any(iterable)` | Retorna `True` si al menos un elemento es `True`. | `any([False, False, True])  # True` |

---

## **Funciones de Entrada y Salida**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `print(*objetos, sep, end)` | Muestra los objetos en pantalla. | `print("Hola", "Mundo", sep="-")  # Hola-Mundo` |
| `input(prompt)` | Captura la entrada del usuario. | `nombre = input("Tu nombre: ")` |
| `open(archivo, modo)` | Abre un archivo. | `f = open("datos.txt", "r")` |

---

## **Funciones para Objetos y Atributos**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `type(objeto)` | Devuelve el tipo del objeto. | `type(5)  # <class 'int'>` |
| `isinstance(objeto, tipo)` | Verifica si un objeto es de un tipo. | `isinstance(5, int)  # True` |
| `id(objeto)` | Retorna el identificador único del objeto. | `id(5)` |
| `hash(objeto)` | Retorna el hash del objeto (si es inmutable). | `hash("Hola")` |
| `dir(objeto)` | Lista los atributos y métodos de un objeto. | `dir([])` |

---

## **Funciones Avanzadas**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `eval(expresión)` | Evalúa una expresión en formato string. | `eval("5 + 5")  # 10` |
| `exec(código)` | Ejecuta código en formato string. | `exec("print('Hola')")` |
| `globals()` | Retorna el diccionario de variables globales. | `globals()` |
| `locals()` | Retorna el diccionario de variables locales. | `locals()` |
| `callable(objeto)` | Verifica si un objeto es invocable (función). | `callable(print)  # True` |

---

## **Funciones para Manipulación de Bytes**
| **Función** | **Descripción** | **Ejemplo** |
|------------|----------------|------------|
| `ord(caracter)` | Retorna el código Unicode de un carácter. | `ord('A')  # 65` |
| `chr(código)` | Retorna el carácter Unicode de un código. | `chr(65)  # 'A'` |
| `bin(x)` | Convierte un número a binario. | `bin(10)  # '0b1010'` |
| `hex(x)` | Convierte un número a hexadecimal. | `hex(255)  # '0xff'` |
| `oct(x)` | Convierte un número a octal. | `oct(8)  # '0o10'` |

---


## **5️⃣ Buenas Prácticas**
✅ Usa **nombres descriptivos** para las funciones.  
✅ Incluye **docstrings** para documentar la función.  
✅ Evita funciones demasiado largas; divide en funciones más pequeñas.  
✅ Usa `return` si la función necesita devolver datos.  
