# pin = "1234"
# saldo = 5000

# persona = input("digite su pin: ") # "1234"
# if pin == persona:
#     print("El pin es valido")
#     monto = int(input("¿cuanto va a retirar?"))
#     if monto < saldo:
#         print(f"usted a retirado ${monto} COP")
        
#         saldo = saldo - monto
#         print(f"su nuevo saldo es de $ {saldo} COP")
        
#     else:
#         print("Su saldo es insuficiente")
# else:
#     print("PIN incorrecto")
    
    
    
    
    
# colores = {
#     "rojo": "red",
#     "azul": "blue",
#     "verde": "green",
#     "amarillo": "yellow",
#     "negro": "black"
# }
# color = input("ingresa un color: ") # morado
# color_in = colores.get(color, False)
# if color_in == False:
#     print(f"el color {color} no se encuentra")
# else:
#     print(color_in)
    
    


# 10 - 20 - 30 - 40 - 50 
# bajo, medio, intermedio, alto 
# calificacion = int(input("Calificación del estudiante"))
# if calificacion<10:
#     print("bajo")
# if calificacion<20:
#     print("medio")
# if calificacion<30:
#     print("intermedio")
# if calificacion<40:
#     print("alto")
    
    

persona  = {
    "nombre": "Felipe",
    "edad": 25,
    "dinero":20000.5,
    "padres":["patricia","anibal"]
}
# print(persona.keys())
# print(persona.values())
# print(persona.items())
    
# continue y break
estudiantes = ["daniela v","daniela","javier","felipe","michel"]
for e in estudiantes:
    print("antes")
    print(e)
    if e == "daniela":
        break
    print("despues")
    print(" ")
    
    

    