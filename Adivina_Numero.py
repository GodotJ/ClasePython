
import random

number = random.randrange(1,20)

guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 20)'))
count = 0

while guess != number:
    if guess<1 or guess>50:
        guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 50)'))
    else:
        count+= 1
        number = random.randrange(1,50)

String =  'La maquina tardo {} intentos en adivinar el numero'.format(count)
print(String)