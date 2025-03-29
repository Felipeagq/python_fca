def consultar_producto(productos_lista):
    producto = input("Producto a consultar: ")
    print(productos_lista[producto])


def mostrar_inventario(productos_lista):
    productos = productos_lista.keys()
    for p in productos:
        print(f"{p} cuesta {productos_lista[p]["precio"]} y hay {productos_lista[p]["stock"]}")