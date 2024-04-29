import random

def shuffle(list):
    copy_list = list[:]  # Copia de la lista
    for i in range(len(copy_list)):
        # Intercambia el elemento en la posición i con un elemento en una posición aleatoria
        rand = random.randint(0, len(copy_list) - 1)
        copy_list[i], copy_list[rand] = copy_list[rand], copy_list[i]
    return copy_list

# Ejemplo de uso
list = [1, 2, 3, 4, 5]
copy_list = shuffle(list)
print("Lista original:", list)
print("Lista mezclada:", copy_list)
