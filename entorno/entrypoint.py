import streamlit as st
from agregar import agregar_producto
from consultar import  consultar_producto, mostrar_inventario

col1, col2, col3 = st.columns([1,1,1])

with col1:
    nombre = st.text_input("nombre")

with col2:
    precio = st.text_input("precio")
    
with col3:
    cantidad = st.text_input("cantidad")

if  st.button("Aceptar"):
    st.write(nombre)
    st.write(precio)
    st.write(cantidad)