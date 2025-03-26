# EJERCICIOS PYTHON FCS

## Ejercicios sencillos
---

### 🔹 **Condicionales (`if`)**  
1️⃣ **Verificación de número par o impar**  
   Escribe un programa que pida al usuario un número entero y use `if` para determinar si es par o impar.  

2️⃣ **Clasificación de edades**  
   Pide al usuario su edad e imprime si es un niño (0-12 años), un adolescente (13-17), un adulto (18-64) o un adulto mayor (65+).  

---

### 🔹 **Bucles `for`**  
3️⃣ **Suma de los primeros `N` números**  
   Solicita un número entero positivo `N` y usa un bucle `for` para sumar los primeros `N` números naturales.  

4️⃣ **Tablas de multiplicar**  
   Pide al usuario un número y usa `for` para imprimir su tabla de multiplicar del 1 al 10.  

---

### 🔹 **Bucles `while`**  
5️⃣ **Adivina el número**  
   Genera un número aleatorio entre 1 y 100 y usa `while` para permitir que el usuario intente adivinarlo hasta que lo logre.  

6️⃣ **Menú interactivo**  
   Crea un menú con `while` que tenga opciones como:  
   - 1️⃣ Ver mensaje  
   - 2️⃣ Repetir saludo  
   - 3️⃣ Salir  

   Si el usuario elige `3`, el programa debe terminar.  

---

### 🔹 **Funciones**  
7️⃣ **Conversión de temperatura**  
   Crea una función que convierta grados Celsius a Fahrenheit y viceversa. Debe recibir la temperatura y el tipo de conversión a realizar.  

8️⃣ **Calculadora de factorial**  
   Escribe una función que calcule el factorial de un número usando recursividad.  

---

### 🔹 **Manejo de excepciones (`try-except`)**  
9️⃣ **División segura**  
   Pide dos números al usuario y usa `try-except` para manejar una posible división por cero.  

🔟 **Validación de entrada numérica**  
   Crea un programa que pida un número al usuario y use `try-except` para asegurarse de que solo se ingresen valores numéricos.  

---

## Ejercicios complejos
Aquí tienes los **enunciados detallados** de los 4 ejercicios grandes, especificando dónde y cómo se deben aplicar **listas, diccionarios, for, while, funciones, try-except e if** en cada caso.  

---

## **Ejercicio 1: Sistema de Gestión de Inventario en una Tienda 🛒**  
### **Descripción del problema**  
Eres el dueño de una tienda y necesitas un programa para administrar tu inventario de productos. Tu sistema debe permitir:  
1. **Agregar productos** con los siguientes datos:  
   - Nombre del producto  
   - Precio  
   - Cantidad en stock  
2. **Actualizar el stock** cuando un cliente compra un producto.  
3. **Consultar la información de un producto específico.**  
4. **Mostrar el inventario completo.**  
5. **Salir del sistema.**  

### **Requisitos técnicos**  
✅ **Estructuras de datos:**  
   - Usar un **diccionario** donde la clave sea el nombre del producto y el valor sea otro diccionario con `precio` y `stock`.  

✅ **Uso de bucles:**  
   - Implementar un **bucle `while`** para mantener el programa en ejecución hasta que el usuario elija salir.  

✅ **Uso de `if`:**  
   - Validar si un producto ya existe antes de agregarlo.  
   - Verificar si hay stock disponible antes de actualizarlo por una compra.  

✅ **Uso de `for`:**  
   - Recorrer el diccionario para mostrar el inventario completo.  

✅ **Uso de `try-except`:**  
   - Capturar errores si el usuario ingresa un precio o cantidad no válidos.  

✅ **Uso de funciones:**  
   - `agregar_producto()`: Agrega productos al inventario.  
   - `actualizar_stock()`: Reduce la cantidad de un producto cuando se vende.  
   - `consultar_producto()`: Muestra los detalles de un producto específico.  
   - `mostrar_inventario()`: Lista todos los productos en stock.  

---

## **Ejercicio 2: Cajero Automático Simulado 💰**  
### **Descripción del problema**  
Diseñar un programa que simule un cajero automático con las siguientes funciones:  
1. **Crear una cuenta bancaria** con un saldo inicial.  
2. **Permitir al usuario depositar dinero en su cuenta.**  
3. **Permitir al usuario retirar dinero, validando que haya fondos suficientes.**  
4. **Mostrar el saldo actual.**  
5. **Salir del sistema.**  

### **Requisitos técnicos**  
✅ **Estructuras de datos:**  
   - Usar un **diccionario** con claves `saldo` y `transacciones`.  

✅ **Uso de bucles:**  
   - Implementar un **bucle `while`** para mantener el sistema activo hasta que el usuario elija salir.  

✅ **Uso de `if`:**  
   - Verificar que el monto a retirar no exceda el saldo disponible.  
   - No permitir depósitos negativos.  

✅ **Uso de `for`:**  
   - Recorrer la lista de transacciones cuando el usuario consulte su historial de movimientos.  

✅ **Uso de `try-except`:**  
   - Capturar errores si el usuario ingresa un monto no válido.  

✅ **Uso de funciones:**  
   - `crear_cuenta()`: Inicia la cuenta con un saldo inicial.  
   - `depositar()`: Permite añadir dinero a la cuenta.  
   - `retirar()`: Permite retirar dinero, validando el saldo.  
   - `consultar_saldo()`: Muestra el saldo actual.  

---

## **Ejercicio 3: Control de Asistencia para un Curso 📚**  
### **Descripción del problema**  
Eres profesor y necesitas un programa para llevar el control de asistencia de tus estudiantes. El sistema debe permitir:  
1. **Registrar nuevos estudiantes en la lista de asistencia.**  
2. **Marcar asistencia diaria de los estudiantes registrados.**  
3. **Mostrar un resumen de asistencia de cada estudiante.**  
4. **Ver la lista completa de estudiantes.**  
5. **Salir del sistema.**  

### **Requisitos técnicos**  
✅ **Estructuras de datos:**  
   - Usar un **diccionario** donde las claves sean los nombres de los estudiantes y los valores el número de asistencias.  

✅ **Uso de bucles:**  
   - Implementar un **bucle `while`** para mantener el programa activo.  

✅ **Uso de `if`:**  
   - Verificar si un estudiante ya está registrado antes de agregarlo.  
   - No permitir marcar asistencia para un estudiante que no existe.  

✅ **Uso de `for`:**  
   - Recorrer el diccionario para mostrar el resumen de asistencias.  

✅ **Uso de `try-except`:**  
   - Capturar errores si el usuario ingresa un nombre vacío o incorrecto.  

✅ **Uso de funciones:**  
   - `registrar_estudiante()`: Agrega un estudiante a la lista.  
   - `marcar_asistencia()`: Suma una asistencia a un estudiante.  
   - `mostrar_asistencias()`: Muestra la asistencia de cada estudiante.  

---

## **Ejercicio 4: Cálculo de Factura para un Restaurante 🍽️**  
### **Descripción del problema**  
Un restaurante necesita un sistema para calcular la factura de sus clientes.  
El programa debe permitir:  
1. **Agregar productos al pedido** (nombre y precio).  
2. **Mostrar el total de la cuenta antes de impuestos y propina.**  
3. **Aplicar automáticamente un impuesto del 8% sobre el total.**  
4. **Permitir al usuario elegir una propina (10%, 15% o 20%).**  
5. **Mostrar el monto final con impuestos y propina.**  
6. **Salir del sistema.**  

### **Requisitos técnicos**  
✅ **Estructuras de datos:**  
   - Usar una **lista de diccionarios**, donde cada diccionario representa un producto con `nombre` y `precio`.  

✅ **Uso de bucles:**  
   - Implementar un **bucle `while`** para permitir agregar productos hasta que el usuario elija terminar.  

✅ **Uso de `if`:**  
   - Verificar que el usuario ingrese un porcentaje de propina válido (10%, 15%, 20%).  
   - Asegurar que los precios ingresados sean positivos.  

✅ **Uso de `for`:**  
   - Recorrer la lista de productos para calcular el total.  

✅ **Uso de `try-except`:**  
   - Capturar errores si el usuario ingresa un precio incorrecto o una opción inválida.  

✅ **Uso de funciones:**  
   - `agregar_producto()`: Añade productos al pedido.  
   - `calcular_total()`: Suma los precios de todos los productos.  
   - `calcular_factura()`: Aplica impuestos y propina.  

---


