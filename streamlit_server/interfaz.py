import streamlit as st
import requests

st.title("API de usuarios")
st.write("Esta es una API de usuarios")


st.write("Ingrese los datos del usuario")
name = st.text_input("Nombre")
email = st.text_input("Email")
password = st.text_input("Password")

# if True:
if st.button("Crear usuario"):
    response = requests.post("http://localhost:8000/", json={"name": name, "email": email, "password": password})
    st.write(response.json())

col1, col2 = st.columns(2)

with col1:
    st.title("eliminar usuario")
    user_id = st.number_input("ID del usuario")
    if st.button("Eliminar usuario"):
        response = requests.delete(f"http://localhost:8000/{user_id}")
        st.write(response.json())

