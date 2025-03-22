# # pin = "1234"
# # saldo = 5000

# # persona = input("digite su pin: ") # "1234"
# # if pin == persona:
# #     print("El pin es valido")
# #     monto = int(input("¿cuanto va a retirar?"))
# #     if monto < saldo:
# #         print(f"usted a retirado ${monto} COP")
        
# #         saldo = saldo - monto
# #         print(f"su nuevo saldo es de $ {saldo} COP")
        
# #     else:
# #         print("Su saldo es insuficiente")
# # else:
# #     print("PIN incorrecto")
    
    
    
    
    
# # colores = {
# #     "rojo": "red",
# #     "azul": "blue",
# #     "verde": "green",
# #     "amarillo": "yellow",
# #     "negro": "black"
# # }
# # color = input("ingresa un color: ") # morado
# # color_in = colores.get(color, False)
# # if color_in == False:
# #     print(f"el color {color} no se encuentra")
# # else:
# #     print(color_in)
    
    


# # 10 - 20 - 30 - 40 - 50 
# # bajo, medio, intermedio, alto 
# # calificacion = int(input("Calificación del estudiante"))
# # if calificacion<10:
# #     print("bajo")
# # if calificacion<20:
# #     print("medio")
# # if calificacion<30:
# #     print("intermedio")
# # if calificacion<40:
# #     print("alto")
    
    

# persona  = {
#     "nombre": "Felipe",
#     "edad": 25,
#     "dinero":20000.5,
#     "padres":["patricia","anibal"]
# }
# # print(persona.keys())
# # print(persona.values())
# # print(persona.items())
    
# # continue y break
# # estudiantes = ["daniela v","daniela","javier","felipe","michel"]
# # for e in estudiantes:
# #     print("antes")
# #     print(e)
# #     if e == "daniela":
# #         break
# #     print("despues")
# #     print(" ")
    
# def godofredo(
#     a:int,b:int,c:int) -> int:
#     """Calcula el perimetro de un triangulo
#     Args:
#         a (int): lado a
#         b (int): lado b
#         c (int): lado c
#     Returns:
#         int: perimetro
#     """   
#     try:
#         p = a+b+c
#         return f"el perimetro de mi triangulo es {p}"
#     except Exception as e:
#         return f"Ha ocurrido un error: {e}"


# # palabras_prohibidas = ["java","php","c++"]
# # palabras_magicas = ["python","js"]
# # interacciones = range(5)
# # pp_in = 0 

# # for i in interacciones:
    
# #     frase = input("ingresa tu frase: ")
# #     for p_p in palabras_prohibidas:
# #         if p_p in frase:
# #             print(f"ñe, ese lenguaje {p_p} no me gusta")
# #             pp_in = 1
# #     for p_m in palabras_magicas:
# #         if p_m in frase:
# #             print(f"SI, ese lenguaje {p_m}  me gusta")
# #             break 
# #     if pp_in == 1:
# #             break





# p = godofredo("felipe",1,2)
# print(p)

# # def viaje(partida, llegada):
# #     print(f"felipe va a viajar de {partida} hasta {llegada}")
# # viaje(llegada="santa marta", partida="Barranquilla")





def mayor_de_edad(edad:int) ->bool:
    """Me devuelve si tiene mayoria de edad
    Args:
        edad (int): edad de la persona

    Returns:
        bool: true si es mayor de edad
    """
    if edad >= 18:
        return True
    elif edad < 0:
        return False
    else: 
        return False



while True:
    try:
        edad = int(input("cual es tu edad: "))
        mayoria_de_edad = mayor_de_edad(edad)
        if mayoria_de_edad:
            print("tienes permiso")
            break
        else:
            print(mayoria_de_edad)
    except Exception as e:
         print(f"Ocurrio un error con la edad:: {e}")