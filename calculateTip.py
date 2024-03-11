check = float(input("¿Cuánto es la cuenta? "))
tip = input("¿Cuánto vamos a dejar de propina?\n 1) 18%\n 2) 20%\n 3) 25%\n")
persons = int(input("¿Cuantas personas hay en la mesa?"))

if tip == '1':
    percentage = 0.18
elif tip == '2':
    percentage = 0.20
elif tip == '3':
    percentage = 0.25
else:
    print("Opción inválida")
    exit()

total = (check * (1 + percentage)) / persons

print("El total a pagar entre ",persons," con una propina del", percentage * 100, "% es  de:", total)