def potencias_base(limite: int, base: int) -> str:
# Escribe aquí debajo tu respuesta. No modifiques la definición de la funci
    resultado = 1
    algo = ""
    while resultado < limite:

        if resultado == 1:
            algo = algo + f"{resultado}"
            resultado = resultado * base

        algo = algo + f"-{resultado}"
        resultado = resultado * base

    return algo

print(potencias_base(100, 3))