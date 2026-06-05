# Ejecutar: uv run streamlit run http/rick_morthy_ui.py
# API: https://rickandmortyapi.com/documentation

import httpx
import streamlit as st

st.set_page_config(page_title="Rick and Morty", layout="centered")

st.title("Rick and Morty")

respuesta = httpx.get("https://rickandmortyapi.com/api/character")
personajes = respuesta.json()["results"]

# Una tarjeta por fila (se lee bien en celular, como una landing vertical)
for personaje in personajes:
    with st.container(border=True):
        st.image(personaje["image"], use_container_width=True)
        st.subheader(personaje["name"])
        st.write(f"{personaje['status']} · {personaje['species']}")
