## Ejercicio Salario:

Enunciado: Crea una función llamada calcular_salario(salario_hora, horas, es_domingo) que calcule el salario total de un trabajador siguiendo estas reglas:
- Las primeras 8 horas se pagan a la tarifa normal (salario_hora).
- Las horas que superen las 8 se pagan a 1,5 veces la tarifa normal.
- Si trabaja en domingo (es_domingo = True), todas las horas trabajadas se pagan al doble de la tarifa normal.
  La función debe devolver el salario total que le corresponde al trabajador.

Añade al enunciado que la función debe devolver un string con este formato:

"HORAS x | SALARIO_HORA x | TOTAL x"

Los valores numéricos deben mostrarse con dos decimales, usando :.2f en Python. Por ejemplo, :.2f formatea 12 como 12.00.


## Base_exponente

Enunciado: Crea una función llamada base_exponente(base, limite) que reciba una base y un límite.

La función debe generar una cadena de texto con las potencias de la base, empezando por \(base^0 = 1\), y continuar mientras el resultado sea menor o igual que el límite.
- Cada potencia debe separarse de la siguiente mediante un guion (-).
- Debe incluirse la última potencia cuyo valor sea menor o igual que el límite.
- La función debe devolver la cadena de texto resultante, sin un guion al final.