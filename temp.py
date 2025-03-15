pin = "1234"
saldo = 5000

persona = input("digite su pin: ") # "1234"
if pin == persona:
    print("El pin es valido")
    monto = int(input("¿cuanto va a retirar?"))
    if monto < saldo:
        print(f"usted a retirado ${monto} COP")
        
        saldo = saldo - monto
        print(f"su nuevo saldo es de $ {saldo} COP")
        
    else:
        print("Su saldo es insuficiente")
else:
    print("PIN incorrecto")
    