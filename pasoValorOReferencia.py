# Paso por valor: Se crea una copia local de la variable dentro de la función.
# Los tipos simples se pasan por valor (int, float, double, String, boolean...)

print("Paso por valor:")
def doblar_valor(numero):
    numero*=2
    
n = 10
doblar_valor(n)
print(n)


# Paso por referencia: Se maneja directamente la variable,
# los cambios realizados dentro le afectarán también fuera.
# Los tipos compuestos se pasan por referencia (listas, diccionarios, conjuntos, tuplas...)

print("Paso por referencia:")
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns)
print(ns)

# TRUCO: para pasar un dato de tipo simple for referencia debemos retornarlos y reasginarlos:

def doblar_valor(numero):
    return numero*2
n = 10
n = doblar_valor(n)
print(n) 