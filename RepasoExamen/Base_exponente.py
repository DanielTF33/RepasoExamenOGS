def base_exponente(base, limite):

    resultado = 1
    string = ""

    while resultado <= limite:

        if  resultado * base > limite:
            string = string + f"{resultado}"
            return string

        string = string + f"{resultado}-"
        resultado = resultado * base

    return string


if __name__ == '__main__':
    print(base_exponente(3,26))