# Completa el ejercicio
def recortar(numero, minimo, maximo):
    # Si el número es menor que el minimo
    if numero < minimo:
        # Devolvemos el minimo
        return minimo
    # Si el número es mayor que el máximo
    elif numero > maximo:
        # Devolvemos el máximo
        return maximo
    # En cualquier otro caso devolvemos el número
    return numero

recortar(5,3,10)