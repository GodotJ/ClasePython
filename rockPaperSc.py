import random

def game(user):
    opt = ["piedra", "papel", "tijeras"]
    optPc = random.choice(opt)
    
    print("Tu elección:", user)
    print("Elección de la computadora:", optPc)
    
    if user == optPc:
        print("¡Empate!")
    elif (user == "piedra" and optPc == "tijeras") or \
         (user == "papel" and optPc == "piedra") or \
         (user == "tijeras" and optPc == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

count = True
while count== True:
    user = input("Elige piedra, papel o tijeras: ").lower()

    if user in ["piedra", "papel", "tijeras"]:
        game(user)
        repeat= input("Quieres volver a jugar? (y/n): ")
        if(repeat == "n"):
            count = False
    else:
        print("Por favor, elige una opción válida: piedra, papel o tijeras.")
        repeat= input("Quieres volver a jugar? (y/n): ")
        if(repeat == "n"):
           count = False