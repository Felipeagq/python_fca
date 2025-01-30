### 🚀 **Programación Orientada a Objetos (POO) en Python**  

La **Programación Orientada a Objetos (POO)** es un paradigma de programación basado en el uso de **clases** y **objetos**. En Python, todo es un objeto, lo que hace que POO sea un enfoque natural para el desarrollo.  

---

## **📌 Conceptos Claves de POO**
Antes de ver código, entendamos algunos conceptos fundamentales:

🔹 **Clase**: Es un molde o plantilla que define la estructura y comportamiento de los objetos.  
🔹 **Objeto**: Es una instancia de una clase, con sus propios datos y comportamiento.  
🔹 **Atributos**: Son las variables dentro de una clase, definen el estado del objeto.  
🔹 **Métodos**: Son funciones dentro de una clase que definen el comportamiento del objeto.  
🔹 **Encapsulamiento**: Controla el acceso a los atributos y métodos de un objeto.  
🔹 **Herencia**: Permite que una clase herede atributos y métodos de otra.  
🔹 **Polimorfismo**: Permite que un mismo método tenga diferentes implementaciones.  

---

## **📝 1. Creación de Clases y Objetos**  

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)

print(persona1.saludar())  # Output: Hola, mi nombre es Juan y tengo 25 años.
print(persona2.saludar())  # Output: Hola, mi nombre es Ana y tengo 30 años.
```

✅ **Explicación**:  
- `__init__`: Es el **constructor**, inicializa los atributos del objeto.  
- `self`: Hace referencia a la instancia del objeto.  
- `nombre` y `edad`: Son **atributos de instancia**.  
- `saludar()`: Es un **método** que usa los atributos de la clase.  

---

## **🔒 2. Encapsulamiento (Público, Protegido y Privado)**  

El **encapsulamiento** oculta detalles internos del objeto, controlando su acceso con convenciones:  

| Tipo de Atributo | Convención | Accesible desde fuera de la clase? |
|-----------------|------------|---------------------------------|
| Público        | `self.atributo`  | ✅ Sí |
| Protegido      | `self._atributo` | ⚠️ Sí (pero no recomendado) |
| Privado        | `self.__atributo` | ❌ No (pero se puede acceder con `_Clase__atributo`) |

### 📌 **Ejemplo de Encapsulamiento**  
```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self._saldo = saldo     # Protegido
        self.__clave = "1234"   # Privado

    def mostrar_saldo(self):
        return f"Saldo: ${self._saldo}"

    def cambiar_clave(self, nueva_clave):
        self.__clave = nueva_clave

# Crear objeto
cuenta = CuentaBancaria("Carlos", 5000)

# Acceso a atributos
print(cuenta.titular)   # ✅ Acceso permitido
print(cuenta._saldo)    # ⚠️ Se puede acceder, pero no es recomendable
# print(cuenta.__clave) # ❌ Error: no se puede acceder directamente

# Acceso forzado a privado (no recomendado)
print(cuenta._CuentaBancaria__clave)  # ✅ Acceso forzado
```

---

## **🧬 3. Herencia (Reutilización de Código)**  

La **herencia** permite que una clase **hija** herede atributos y métodos de una clase **padre**.  

```python
# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Hace un sonido"

# Clase hija
class Perro(Animal):
    def sonido(self):  # Sobreescribimos el método
        return "Ladra"

class Gato(Animal):
    def sonido(self):  # Sobreescribimos el método
        return "Maulla"

# Crear objetos
perro = Perro("Firulais")
gato = Gato("Mishi")

print(perro.nombre, ":", perro.sonido())  # Firulais : Ladra
print(gato.nombre, ":", gato.sonido())    # Mishi : Maulla
```

✅ **Explicación**:  
- `Animal` es la clase base.  
- `Perro` y `Gato` son clases hijas y **heredan** de `Animal`.  
- Se **sobreescribe** el método `sonido()` en cada clase hija.  

---

## **🎭 4. Polimorfismo (Mismo Método, Diferentes Clases)**  

El **polimorfismo** permite que un método tenga diferentes comportamientos según la clase.  

```python
class Ave:
    def volar(self):
        return "Algunas aves vuelan"

class Aguila(Ave):
    def volar(self):
        return "El águila vuela alto"

class Pinguino(Ave):
    def volar(self):
        return "El pingüino no vuela"

# Función que usa polimorfismo
def describir_ave(ave):
    print(ave.volar())

# Usamos la misma función para diferentes clases
describir_ave(Aguila())   # El águila vuela alto
describir_ave(Pinguino()) # El pingüino no vuela
```

✅ **Explicación**:  
- `describir_ave()` recibe cualquier objeto de la clase `Ave` y ejecuta `volar()`.  
- Cada clase define `volar()` de manera diferente.  

---

## **📝 Ejercicios de Programación Orientada a Objetos**  

💡 **Ejercicio 1:**  
Crea una clase `Vehiculo` con atributos `marca`, `modelo` y `año`. Luego, crea una clase `Coche` que herede de `Vehiculo` y añada un atributo `puertas`. Implementa un método para mostrar toda la información del coche.  

💡 **Ejercicio 2:**  
Crea una clase `Empleado` con atributos `nombre` y `salario`. Luego, crea una clase `Gerente` que herede de `Empleado` y tenga un atributo adicional `departamento`. Implementa un método que muestre si el `Gerente` gana más de $5000.  

💡 **Ejercicio 3:**  
Crea una clase `Figura` con un método `area()`. Luego, crea dos clases `Rectangulo` y `Circulo` que hereden de `Figura` y sobreescriban `area()` para calcular el área según su fórmula matemática.  

---

### 🚀 **Conclusión**
✅ Clases y objetos en Python permiten estructurar mejor el código.  
✅ El **encapsulamiento** protege los datos del objeto.  
✅ La **herencia** permite reutilizar código.  
✅ El **polimorfismo** permite definir métodos con el mismo nombre pero con diferentes comportamientos.  

---
