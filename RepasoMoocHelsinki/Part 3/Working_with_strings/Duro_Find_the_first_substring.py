palabra = input("Please type in a word:")
caracter = input("Please type in a character:")

index = palabra.find(caracter)

if index + 3 > len(palabra):
    print()
else:
    print(palabra[index : index + 3])