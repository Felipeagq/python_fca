from consultar import (consultar_producto,mostrar_inventario)
from agregar import agregar_producto
from datetime  import datetime

lista_de_productos = {
    "empanada":{
        "precio":3000,
        "stock":3
    },
    "arepa":{
        "precio":4000,
        "stock":2
    },
}

while True: 
    choice = input(""""
===== MENU =====
1. ver productos
2. agregar producto
3.consultar producto

salir
                   """)
    if choice == "1":
        mostrar_inventario(lista_de_productos)
    if choice == "2":
        agregar_producto(lista_de_productos)
    if choice == "3":
        consultar_producto(lista_de_productos)
    if choice == "salir":
        break