def calcular_salario(salario_hora, horas, es_domingo):

    if  es_domingo:
        salario_hora *= 2

    if horas <= 8:
        salario = salario_hora * horas

    elif horas > 8 and es_domingo == True:
        salario = salario_hora * horas

    elif horas > 8:
        horas_restantes = horas - 8
        salario_extra = salario_hora * 8
        salario = (salario_hora * horas_restantes) * 1.5

        salario = salario + salario_extra

    return f"HORAS {horas} | SALARIO_HORA {salario_hora} | TOTAL {salario:.2f}"


if __name__ == '__main__':
    print(calcular_salario(10, 9, True))