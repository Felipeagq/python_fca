"""
Actividad previa a Streamlit: consumir la API con requests.

Documentación: https://rickandmortyapi.com/documentation
Ejecutar desde la raíz del proyecto:

    uv run python http/rick_morthy.py
"""

import requests

BASE = "https://rickandmortyapi.com/api"
URL_PERSONAJES = f"{BASE}/character"


def main() -> None:
    # --- 1. Primera página de personajes (20 por página) ---
    respuesta = requests.get(URL_PERSONAJES)
    respuesta.raise_for_status()  # Si la API falla, muestra el error

    datos = respuesta.json()
    personajes = datos["results"]

    print("=== Rick and Morty API ===\n")
    print(f"Total en la API: {datos['info']['count']}")
    print(f"Página 1 — mostrando {len(personajes)} personajes:\n")

    for p in personajes:
        print(f"  · {p['name']} | {p['status']} | {p['species']}")

    # --- 2. Un personaje por id ---
    print("\n--- Un personaje (GET /character/1) ---")
    rick = requests.get(f"{URL_PERSONAJES}/1").json()
    print(f"  Nombre: {rick['name']}")
    print(f"  Imagen: {rick['image']}")

    # --- 3. Filtrar por nombre (query params) ---
    print("\n--- Filtro: name=morty ---")
    filtro = requests.get(URL_PERSONAJES, params={"name": "morty"})
    filtro.raise_for_status()

    for p in filtro.json()["results"]:
        print(f"  · {p['name']}")


if __name__ == "__main__":
    main()
