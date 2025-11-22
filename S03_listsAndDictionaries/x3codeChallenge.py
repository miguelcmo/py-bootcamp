"""
Sistema de Inventario con Conjuntos (sets)

Descripción:
Crear un pequeño sistema para administrar un inventario de productos usando un set.

El programa debe permitir:
    *Agregar un producto
    *Eliminar un producto
    *Verificar si un producto existe
    *Mostrar el inventario completo

Debe usar:
    *Set
    *If
    *Ciclo while
    *Funciones para las operaciones

Objetivo: practicar sets, validación de duplicados y pertenencia.
"""
def agregar_producto(inventario):
    producto = input("Ingreso el nombre del producto: ").lower()
    inventario.add(producto)
    print("Producto guardado.\n")

def eliminar_producto(inventario):
    producto = input("Ingreso el nombre del producto a eliminar: ").lower()
    if producto in inventario:
        inventario.remove(producto)
        print("Producto eliminado.\n")
    else:
        print("El producto solicitado no esta en el inventario.\n")

def buscar_producto(inventario):
    producto = input("Ingreso el nombre del producto a buscar: ").lower()
    if producto in inventario:
        print("El producto se encuentra disponible.\n")
    else:
        print("El producto no esta disponible.\n")

def mostar_productos(inventario):
    print("\nInventario de la tienda")
    for p in inventario:
        print(f"- {p}")
    print()

def menu():
    inventario = set()

    print("------------------------------------------")
    print("|     Sistema de Inventario Tienda       |")
    print("------------------------------------------")

    while True:
        print("1. Agregar producto(a)")
        print("2. Eliminar producto(d)")
        print("3. Buscar producto(f)")
        print("4. Mostrar productos(s)")
        print("5. Salir(e)\n")

        opcion = input("Selecione una opción: ") # devuelve la entrada del usuario como un cadena de texto String

        if opcion == "1" or opcion == "a":
            agregar_producto(inventario)
        elif opcion == "2" or opcion == "d":
            eliminar_producto(inventario)
        elif opcion == "3" or opcion == "f":
            buscar_producto(inventario)
        elif opcion == "4" or opcion == "s":
            mostar_productos(inventario)
        elif opcion == "5" or opcion == "e":
            print("Saliendo el sistema...")
            break
        else:
            print("La opción elegida no es valida.")

menu()