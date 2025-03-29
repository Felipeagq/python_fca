import json

def consultar_producto(productos_lista):
    producto = input("Producto a consultar: ")
    print(productos_lista[producto])


def mostrar_inventario():
    with open("datos.json", "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
    return productos