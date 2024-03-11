import random
num = random.randrange(1,50)
adi = int(input("Adivina el numero entre 1 - 50:  "))
cont = 0

while adi != num:  
    if (adi < num):
        print("Elije un numero mas alto. Intentalo otra vez")
        adi = int(input("\nAdivina un numero entre 1 - 50:  "))
        cont = cont + 1
    else:
        print("Elije un numero mas bajo. Intentalo otra vez")
        adi = int(input("\nAdivina un numero entre 1 - 50:  "))
        cont = cont + 1
print("Adivinaste el numero felicidades!!!")
print("Te costo ", cont, " intentos")