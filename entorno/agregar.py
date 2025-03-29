import json

def agregar_producto(
    producto:str,
    precio:int,
    cantidad:int 
) -> dict:
    with open("datos.json", "r", encoding="utf-8") as archivo:
        diccionario = json.load(archivo)
        
    diccionario[producto] = {"precio": precio, "stock":cantidad}
    
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(diccionario, archivo, indent=4, ensure_ascii=False)