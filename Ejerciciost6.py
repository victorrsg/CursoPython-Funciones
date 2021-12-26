print("Ejercicio 1: Área de un rectángulo")
def area_rectangulo(base,altura):
    return base*altura
    area=base*altura
    print(area)

print(area_rectangulo(15,10))

print("===================================")
print("Ejercicio 2: Área de un círculo")

import math
def area_circulo(radio):
    return radio**2*math.pi

print(area_circulo(5))

print("===================================")
print("Ejercicio 3: A partir de dos números cumpla lo siguiente:")
print("si n1>n2 -- pintar 1") 
print("si n1<n2 -- pintar -1")
print("si n1=n2 -- pintar 0")

def relacion(n1,n2):
    if n1>n2:
        print("1")
    elif n1<n2:
        print("-1")
    else:
        print("0")

relacion(3,2)
 
print("===================================")
print("Ejercicio 4: A partir de dos números saca punto intermedio:")

def intermedio(n1,n2):
    return (n1+n2)/2

print(intermedio(-12,24))

print("===================================")
print("Ejercicio 5: ")

def recortar(num,min,max):
    if num<min:
        return min
    elif num>max:
        return max
    else:
        return num

print(recortar(15,0,10))

print("===================================")
print("Ejercicio 6: Dos listas ordenadas separadas, una de pares y otra de impares: ")

def separar(numeros):
    
    numeros.sort        # ordenar lista
    
    pares =[]
    impares= []
    for num in numeros:
        if num%2==0:
           pares.append(num)
        else:
            impares.append(num)
    return pares,impares
          
pares,impares =separar([-12,84,13,20,-33,101,9])
print("Los pares son:",pares)
print("Los impares son:",impares)



