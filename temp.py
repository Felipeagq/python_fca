alumnos = ["Felipe","Daniela","Michel","Daniela","Martin","Angelo"]
persona = input("¿como te llamas?")
persona = persona.lower().capitalize()
if persona in alumnos:
    print("entra")
    alumnos.remove(persona)
else:
    print("no puedes entrar")