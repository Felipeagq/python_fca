
def agregar_producto(productos_lista):
    producto = input("escribe el producto: ")
    cantidad = int(input("escribe el cantidad: "))
    precio = int(input("escribe el precio: "))
    productos_lista[producto] = {"precio": precio, "stock":cantidad}
    print(productos_lista[producto])
    pass

def consultar_producto(productos_lista):
    producto = input("Producto a consultar: ")
    print(productos_lista[producto])
    

def mostrar_inventario(productos_lista):
    productos = productos_lista.keys()
    for p in productos:
        print(f"{p} cuesta {productos_lista[p]["precio"]} y hay {productos_lista[p]["stock"]}")
        

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