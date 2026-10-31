def extraer_datos(trama: str) -> str:
# Escribe aquí debajo tu respuesta. No modifiques la definición de la función
    princi = trama.find("[")
    fin = trama.rfind("]")

    if fin != -1 and fin < princi:
        return "TRAMA INVÁLIDA"

    elif fin == -1 or princi == -1:
        return "TRAMA INVÁLIDA"

    elif fin != -1 and princi != -1 and fin > princi and trama.find("ERROR") == -1:
        return trama[princi+1 : fin] # este +1 me habria hecho suspender o por lo menos probar unas veces

    elif trama.find("ERROR"):
        return "SENSOR FALLIDO"
    else:
        return trama


print(extraer_datos("basura[secreto]masbasura"))
print(extraer_datos("start[a]b[c]end"))
print(extraer_datos("info[data_ERROR_01]end"))
print(extraer_datos("texto_sin_inicio]"))

# este solo intente rascar nota ya que ya estaba suspenso