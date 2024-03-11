def Acronimo(sentencia):
    pal = sentencia.split()
    Acronimo = ""
    for word in pal:     
        Acronimo += word[0].upper()
    return Acronimo
sentencia = input("Ingresa una frase para generar un acrónimo: ")
acro = Acronimo(sentencia)
print("El acrónimo de la frase es:", acro)