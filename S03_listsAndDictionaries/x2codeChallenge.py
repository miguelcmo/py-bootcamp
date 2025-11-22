"""
Análisis de Notas de Estudiantes (listas, tuplas, funciones)

Descripción:
Pedir al usuario ingresar varias notas entre 0 y 5.
Guardar las notas en una lista.

Luego:
    *Mostrar el promedio
    *Mostrar la nota más alta y la más baja
    *Devolver los resultados como una tupla: (promedio, mayor, menor)

El programa debe validar que cada nota ingresada sea correcta.
"""

# Pasos lógicos para resolver el problema:
# 1. Inicializar una lista vacía `notas = []` para almacenar las notas. ####hecho
# 2. Pedir al usuario que ingrese una nota en un bucle repetitivo (por ejemplo, hasta que
#    el usuario escriba una palabra clave como "fin" o deje la entrada vacía).
# 3. Para cada entrada:
#    - Validar que la entrada pueda convertirse a número (float) y esté entre 0 y 5.
#    - Si la entrada es inválida, mostrar un mensaje de error y pedir de nuevo.
#    - Si es válida, convertirla a `float` y agregarla a la lista `notas`.
# 4. Repetir el paso 3 hasta que el usuario indique que no desea ingresar más notas.
# 5. Al terminar, verificar si la lista `notas` está vacía:
#    - Si está vacía, informar al usuario y terminar o pedir al menos una nota.
# 6. Calcular el promedio: `promedio = sum(notas) / len(notas)`.####hecho
# 7. Obtener la nota máxima y mínima: `mayor = max(notas)` y `menor = min(notas)`.####hecho
# 8. Empaquetar los resultados en una tupla: `resultado = (promedio, mayor, menor)` y devolverla
#    desde una función o imprimirla formateada.####hecho
# 9. (Opcional) Redondear el promedio a la cantidad de decimales deseada antes de mostrar.
#10. (Opcional) Añadir pruebas o casos límite: notas en los extremos (0 y 5), entradas no numéricas,
#    y comportamiento con una sola nota.


def menu():
    notas = []

    print("-----------------------------------------")
    print("--- Sistema de notas para estudiantes ---")
    print("-----------------------------------------")

    while True:
        entradaNota = input("Ingrese la nota del estudiante (marque 'x' para terminar): ")
        # print(entradaNota)

        if entradaNota.lower() == "x":
            break

        entrada = float(entradaNota)

        if 0 <= entrada <= 5:
            #codigo que ejecuta el si
            notas.append(entrada)
        else:
            print("Su nota no corresponde con el rango de notas de la universidad.")
        
        #print(notas)

    return notas

def calcular_notas(notas):
    promedioNotas = sum(notas) / len(notas)
    notaMayor = max(notas)
    notaMenor = min(notas)
    return (promedioNotas, notaMayor, notaMenor)

conjuntoNotas = menu()

if len(conjuntoNotas) > 0:
    resultadoNotas = calcular_notas(conjuntoNotas)
    print("El promedio de notas del estudiante es: ", resultadoNotas[0])
    print("La nota mas alta del estudiante es: ", resultadoNotas[1])
    print("la nota mas baja del estudiante es: ", resultadoNotas[2])
    print(resultadoNotas)
else: 
    print("No se ingresaron notas.")
