word = input("Word: ")
tamanio = len(word)

uso = 28 - tamanio
restante = uso//2

print("*"*30)
#print("*"*restante+f"{word}"+"*"*restante)

#print(f"*{' '*restante}{word}{' '*restante}*")
print(f"*{word.center(28)}*")

print("*"*30)