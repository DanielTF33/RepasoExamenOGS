# string = input("Please type in a string: ")
# c = string[1]


# if string[1] == string[len(string)-2]:
#    letra = string[1]
#    print(f"The second and the second to last characters are {letra}")
#
# else:
#    print(f"The second and the second to last characters are different")


string = input("Please type in a string:")

primero = string[1]
ultimo = string[len(string)-2]

if primero == ultimo:
    print(f"The second and the second to last characters are {primero}")
else:
    print("The second and the second to last characters are different")