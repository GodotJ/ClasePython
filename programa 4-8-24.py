# Pedir datos
direccion_correo = input("Por favor ingresa tu dirección de correo: ")
nombre = input("Por favor ingresa tu nombre: ")
edad = input("Por favor ingresa tu edad: ")

# Definir códigos de color
color_verde = "\033[32m"
color_blanco = "\033[37m"
color_rojo = "\033[31m"
reset_color = "\033[0m"

# Imprimir
print("Hola, mi nombre es " + reset_color + color_verde + nombre + reset_color + ", mi dirección es " + reset_color + color_blanco + direccion_correo + reset_color + ", y mi edad es " + reset_color + color_rojo + edad + reset_color + ".")
