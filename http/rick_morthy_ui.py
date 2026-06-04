# Ejecutar: uv run streamlit run interfaz.py
# API: https://rickandmortyapi.com/documentation

import httpx
import streamlit as st

st.title("Rick and Morty")

# Primera página = 20 personajes (la API pagina así)
respuesta = httpx.get("https://rickandmortyapi.com/api/character")
personajes = respuesta.json()["results"]

# Una tarjeta por personaje (3 por fila)
for i in range(0, len(personajes), 3):
    columnas = st.columns(3)
    for col, personaje in zip(columnas, personajes[i : i + 3]):
        with col:
            with st.container(border=True):
                st.image(personaje["image"])
                st.subheader(personaje["name"])
                st.write(f"{personaje['status']} · {personaje['species']}")
