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

if st.button("Agregar"):
    lista_de_productos = agregar_producto(
        producto=nombre,
        precio=precio,
        cantidad=cantidad
    )
    print(lista_de_productos)
    st.write(lista_de_productos)
st.divider()
if st.button("consultar  todo"):
    inventario = mostrar_inventario()
    st.write(inventario)