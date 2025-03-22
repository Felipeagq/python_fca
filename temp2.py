palabras_prohibidas = ["java","php","c++"]
palabras_magicas = ["python","js"]
interacciones = range(5)

for i in interacciones:
    frase = input("ingresa tu frase: ")
    for f in frase.split():
        if f in palabras_prohibidas:
            print("si esta")
