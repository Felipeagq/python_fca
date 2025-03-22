Simulación de cajero automático
Crea un programa que simule un cajero automático:

- Pide al usuario un PIN (el correcto es "1234").
- Si el PIN es incorrecto, muestra "Acceso denegado" y termina el programa.
- Si el PIN es correcto, permite ingresar un monto a retirar.
- El saldo inicial es $5000. Si el monto solicitado es mayor que el saldo disponible, muestra "Fondos insuficientes".
- Si hay suficiente saldo, descuéntalo y muestra el saldo restante.


---
### **📌 Ejercicio: Traductor de colores**  
Crea un programa que use un **diccionario** para traducir colores del español al inglés.  

#### **Requisitos:**  
1. Crea un diccionario con al menos 5 colores en español como claves y su traducción en inglés como valores.  
2. Pide al usuario que ingrese un color en español.  
3. Si el color está en el diccionario, muestra su traducción.  
4. Si el color no está en el diccionario, muestra un mensaje diciendo `"Color no encontrado"`.  

---

### **🔹 Diccionario de ejemplo**
```python
colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green",
    "amarillo": "yellow",
    "negro": "black"
}
```

---

### **🔹 Ejemplo de entrada y salida**  

✅ **Caso 1: El color existe en el diccionario**  
```
Ingrese un color en español: rojo
Traducción en inglés: red
```

❌ **Caso 2: El color no está en el diccionario**  
```
Ingrese un color en español: morado
Color no encontrado.
```


## Ejercicio 1: Detector de número secreto 🔢
Crea un programa que pida al usuario adivinar un número secreto (por ejemplo, 7).
- Solo tiene 5 intentos
- Si el usuario acierta, muestra un mensaje de victoria y termina el bucle con break.
- Si el usuario ingresa un número incorrecto, sigue pidiendo otro intento.
- Si el usuario ingresa un número negativo, ignora esa entrada con continue.

---

## Ejercicio 2: Contador de palabras prohibidas 🚫
El usuario ingresa una frase y el programa verifica si contiene palabras prohibidas como "maldición" o "odio".
- cada iteración el usuario debe ingresar frases
- Si encuentra una palabra prohibida, muestra una advertencia y detiene el programa.
- Si no hay palabras prohibidas, sigue preguntando.

