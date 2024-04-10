from colorama import Fore, Style


direccion_correo = input("Por favor ingresa tu dirección de correo: ")
nombre = input("Por favor ingresa tu nombre: ")
edad = input("Por favor ingresa tu edad: ")


print("Hola, mi nombre es", Fore.YELLOW + nombre + ",", "mi dirección es", Fore.MAGENTA + direccion_correo + ",", "y mi edad es", Fore.BLUE + edad + ".", Style.RESET_ALL)
