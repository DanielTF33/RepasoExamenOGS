string = input("Please type in a string:")
string_invertido= string[::-1]

contador = 0

while contador < len(string):

    print(string_invertido[contador])
    contador+=1


# string = input("Please type in a string:")

# for caracter in string[::-1]:
#    print(caracter)