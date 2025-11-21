"""
Gestor de Contactos Simple (listas, diccionarios, funciones)

Descripción:
Crear un programa que permita registrar contactos con nombre y número de teléfono.

El usuario debe poder (operaciones):
    *Agregar un contacto (hecho)
    *Mostrar todos los contactos (hecho)
    *Buscar un contacto por nombre (hecho)
    *Salir

Debe usarse:
    *Una lista de diccionarios para almacenar los contactos
    *Ciclos while
    *Condicionales if
    *Funciones para cada operación
"""
def agregar_contacto(contactos):
    nombre = input("Nombre: ")
    cedula = input("Cedula: ")
    telefono = input("Telefono: ")
    contactos.append({"nombre": nombre, "cedula": cedula, "telefono": telefono})

def mostrar_contactos(contactos):
    print("\nLista de contactos:")
    for c in contactos:
        print(f'Nombre: {c['nombre']} - Telefono: {c['telefono']}') # format (formato de texto)
    print()

def buscar_contacto(contactos):
    pass

def menu():
    # lista de diccionarios para almacenar los contactos
    contactos = [] 

    while True:
        print("##### Agenda de contactos #####")
        print("-------------------------------")
        print("1. Agregar un contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un contacto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            print("Saliendo de la app!")
            break
        else:
            print("Opción no disponible.\n")

menu()