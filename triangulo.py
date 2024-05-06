def imprimir_triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)


altura = int(input("Ingresa el tamaño del triangulo: "))
imprimir_triangulo(altura)
