def is_palindromo(word):
    return word == word[::-1]

words = []
for i in range(5):
    word = input(f"Ingrese la palabra #{i + 1}: ")
    words.append(word.lower()) 

palindromes = []
no_palindromes = []
for word in words:
    if is_palindromo(word):
        palindromes.append(word)
    else:
        no_palindromes.append(word)

print("\nPalíndromos:")
for palindrome in palindromes:
    print(palindrome)

print("\nNo palíndromos:")
for no_palindrome in no_palindromes:
    print(no_palindrome)