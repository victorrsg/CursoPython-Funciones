# Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. 
# En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre:

# Por posición (tupla):
def indeterminados_posicion(*args):     # args: argumentos
    for arg in args:
        print(arg)
    
indeterminados_posicion(5,"Hola",[1,2,3,4,5])
print("*********************************")

# Por nombre (diccionario):
print("En forma de diccionario:")
def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])

print("------------------")

def indeterminados_nombre(**kwargs):     # kwargs: keywords arguments
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])

print("==========================================")

# Por posición y nombre a la vez: 
def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es",t)
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])

super_funcion(10,50,-1,1.56,10,20,300,nombre="Hector",edad=27)