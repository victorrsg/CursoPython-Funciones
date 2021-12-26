# Función recursiva: una función que se llama así misma durante su ejecución

print("Ejemplo 1: Cuenta atrás desde un 'num'")
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(11)


print("Ejemplo 2: Suma todos los numeros desde 'numero' hasta 1")

def sumatorio(numero):
    if numero > 0:
        numero += sumatorio(numero-1)
    return numero

sumatorio(5)
