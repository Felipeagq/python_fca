### 🚀 **Creación de Interfaces con Streamlit en Python**  

Streamlit es una librería de Python diseñada para crear interfaces gráficas de usuario (GUI) **rápidamente** y con **pocas líneas de código**. Se usa principalmente para visualizar datos, construir dashboards y desarrollar aplicaciones web interactivas sin necesidad de conocimientos en HTML, CSS o JavaScript.  

---

## **📌 Instalación de Streamlit**  
Para instalar Streamlit, ejecuta en la terminal:  
```bash
pip install streamlit
```

Para verificar que la instalación fue exitosa, puedes ejecutar:
```bash
streamlit hello
```
Esto abrirá una demo interactiva en el navegador.

---

## **📝 1. Estructura Básica de un Script en Streamlit**  
Crea un archivo llamado `app.py` y agrega el siguiente código:

```python
import streamlit as st

# Título de la app
st.title("🚀 Mi Primera App con Streamlit")

# Texto normal
st.write("¡Bienvenido a mi aplicación interactiva!")

# Entrada de datos
nombre = st.text_input("Escribe tu nombre:")

# Botón para mostrar un mensaje
if st.button("Saludar"):
    st.write(f"Hola, {nombre}! 🎉")
```

### **Ejecutar la Aplicación**
Corre el siguiente comando en la terminal dentro del directorio donde creaste `app.py`:
```bash
streamlit run app.py
```
Esto abrirá la aplicación en el navegador.

---

## **🖼️ 2. Widgets en Streamlit**
Streamlit tiene varios elementos interactivos como **botones, deslizadores, casillas de verificación, selectores y más**.  

### 📌 **Ejemplo con múltiples widgets**  
```python
import streamlit as st

st.title("🌟 Widgets en Streamlit")

# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")

# Casilla de verificación
if st.checkbox("Mostrar saludo personalizado"):
    st.write(f"¡Hola, {nombre}! 🎉")

# Selector
color = st.selectbox("Escoge un color favorito:", ["Rojo", "Azul", "Verde"])
st.write(f"Has seleccionado: {color}")

# Deslizador
edad = st.slider("Selecciona tu edad:", 0, 100, 25)
st.write(f"Tu edad es: {edad}")

# Botón
if st.button("Presiona aquí"):
    st.success("¡Has presionado el botón! 🎈")
```

---

## **📊 3. Gráficos y Visualización de Datos**
Streamlit es compatible con **Matplotlib, Seaborn y Plotly**, lo que permite crear gráficos de forma sencilla.

### 📌 **Ejemplo con Matplotlib**
```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Gráfico de Función")

# Datos para la gráfica
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# Crear la figura
fig, ax = plt.subplots()
ax.plot(x, y, label="Seno", color="blue")
ax.legend()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)
```

---

## **📂 4. Subida y Manejo de Archivos**
Puedes permitir a los usuarios **subir archivos** como imágenes, PDFs o CSVs.

### 📌 **Ejemplo: Cargar y Mostrar una Imagen**
```python
import streamlit as st
from PIL import Image

st.title("📷 Subir Imagen")

# Subir un archivo
archivo = st.file_uploader("Elige una imagen", type=["jpg", "png", "jpeg"])

# Mostrar la imagen si se sube
if archivo is not None:
    imagen = Image.open(archivo)
    st.image(imagen, caption="Imagen cargada", use_column_width=True)
```

---

## **📢 5. Notificaciones y Mensajes**
Puedes mostrar mensajes emergentes como notificaciones, advertencias y errores.

### 📌 **Ejemplo de Mensajes de Estado**
```python
import streamlit as st

st.title("⚠️ Notificaciones en Streamlit")

st.success("✅ ¡Todo salió bien!")
st.warning("⚠️ Ten cuidado con esto.")
st.error("❌ Algo salió mal.")
st.info("ℹ️ Información importante.")
```

---

## **🔄 6. Sidebar (Menú Lateral)**
Puedes mover elementos a un **menú lateral** para mejorar la organización de tu app.

### 📌 **Ejemplo de Sidebar**
```python
import streamlit as st

# Título principal
st.title("🎨 Aplicación con Sidebar")

# Menú lateral
st.sidebar.title("🔧 Configuración")

# Opciones en la barra lateral
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Inicio", "Acerca de", "Contacto"])

st.write(f"Has seleccionado: {opcion}")
```

---

## **📍 7. Estado y Sesiones en Streamlit**
Para **guardar información entre interacciones**, puedes usar `st.session_state`.

### 📌 **Ejemplo con Sesiones**
```python
import streamlit as st

st.title("📌 Contador con Estado")

if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1

st.write(f"Contador: {st.session_state.contador}")
```

---

## **🚀 Conclusión**
**Streamlit** es una librería poderosa para construir **interfaces gráficas rápidas y elegantes** en Python sin necesidad de conocimientos avanzados de desarrollo web.

### **📌 Resumen de lo Aprendido**
✅ Creación de una app básica con `st.title()`, `st.write()`, `st.button()`.  
✅ Uso de **widgets interactivos** como `st.text_input()`, `st.checkbox()`, `st.selectbox()`.  
✅ Creación de **gráficos** con `matplotlib`.  
✅ Subida de archivos con `st.file_uploader()`.  
✅ Notificaciones y mensajes con `st.success()`, `st.warning()`, `st.error()`.  
✅ Uso de **sidebar** con `st.sidebar`.  
✅ Manejo del **estado de sesión** con `st.session_state`.  
