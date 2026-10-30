# Write your solution here

limit = int(input("Limit:"))
resultado = 0
string = ""
total = 0

while total < limit:

    resultado = resultado + 1
    total = total + resultado

    # if total + resultado > limit:
    #    string = string + f"= {total}"
    #    break

    if resultado == 1:
        string = f"{resultado} "
        #total = total + resultado
    else:
        string = string + f"+ {resultado} "
        #total = total + resultado

string = string + f"= {total}"

print(f"The consecutive sum: {string}")