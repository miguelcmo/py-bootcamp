# Use of keyword def to create or define a function
def funcion_suma(a, b):
    print("La suma es", a + b)

funcion_suma(3, 5)
# Salida: La suma es 8


# The return keyword is used to let a function give back a value
def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)
# Salida: La suma es 8


# The lambda keyword is used to create anonymous functions, also known as lambda functions. These functions do not have a declared name
print("La suma es", (lambda a, b: a + b)(3, 5))
# Salida: La suma es 8


# The pass keyword is used when we dont want to define the function itself or left it blank
def funcion_suma(a, b):
    pass

"""
Finally, yield is used in generators and coroutines. Generators produce values one at a time as we iterate over them, 
allowing the creation of potentially infinite sequences without storing everything in memory. This makes them very 
useful when working with very large datasets.
"""
def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)
# Salida: 1, 2, 3