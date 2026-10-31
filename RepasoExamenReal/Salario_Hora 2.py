def recibo_salarial(salario_hora: float, horas_trabajadas: int, es_domingo: bool):
# Escribe aquí debajo tu respuesta. No modifiques la definición de la funci
    if es_domingo == True:
        salario_hora = salario_hora * 2 #cambio 1 no puse el nombre bien

    if horas_trabajadas <= 8:
        salario = salario_hora * horas_trabajadas
    elif horas_trabajadas > 8:
        horas_restantes = horas_trabajadas - 8
        salario = salario_hora * 8 # cambio 2 un puto 8
        salario_extra = (salario_hora * horas_restantes) * 1.5
        salario = salario + salario_extra

    return f"Horas: {horas_trabajadas} | Tarifa Base: {salario_hora:.2f} | Total: {salario:.2f} €" # el format 2f


print(recibo_salarial(10.0, 8, False))
print(recibo_salarial(10.0, 10, False))
print(recibo_salarial(12.5, 9, True))