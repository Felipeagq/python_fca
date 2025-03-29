def agregar_producto(productos_lista):
    producto = input("escribe el producto: ")
    cantidad = int(input("escribe el cantidad: "))
    precio = int(input("escribe el precio: "))
    productos_lista[producto] = {"precio": precio, "stock":cantidad}
    print(productos_lista[producto])