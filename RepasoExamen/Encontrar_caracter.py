from pip._internal import self_outdated_check

def validar_trama(trama):

    inicio = trama.find("[")
    final = trama.rfind("]")

    # print(f"{inicio}  --  {final}")

    if inicio < final and inicio != -1:
        return (f"El [ esta en la pos {inicio} y el ] en la pos {final}")
    elif final < inicio and final != -1:
        return ("INVALIDO EL ] NO PUEDE IR PRIMERO")
    elif final==-1 and inicio ==-1:
        return ("NO ESTAN")
    elif final == -1 or inicio == -1:
        return ("INVALIDO FALTA ALGO")


if __name__ == '__main__':

    print(validar_trama("Ho]la["))
    print(validar_trama("Hola"))
    print(validar_trama("Ho[]la"))