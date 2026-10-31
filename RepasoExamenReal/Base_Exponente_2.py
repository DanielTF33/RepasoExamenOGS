def potencias_base(limite: int, base: int) -> str:
    # Escribe aquí debajo tu respuesta. No modifiques la definición de la funci
    resultado = 1
    algo = ""
    while resultado < limite:

        if resultado == 1:  # añado esto para el guion a la izq
            algo = algo + f"{resultado}"
            resultado = resultado * base

        algo = algo + f"-{resultado}" # quito un espacio
        resultado = resultado * base
    return algo


print(potencias_base(100, 3))
print(potencias_base(1000, 2))
print(potencias_base(27, 3))
print(repr(potencias_base(0, 2)))

# este ya salia bien pero con un guion a la izq
