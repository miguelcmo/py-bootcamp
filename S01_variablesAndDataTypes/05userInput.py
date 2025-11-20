"""
Use of input to get data from user through the terminal
"""

from typing import Optional


def ejemplo_basico(nombre: Optional[str] = None) -> None:
    """Leer una cadena simple y saludar.

    Si `nombre` es None, se pedirá interactivamente.
    """
    if nombre is None:
        nombre = input('¿Cómo te llamas? ')
    print(f'Hola, {nombre}!')


def ejemplo_numerico(valor: Optional[str] = None) -> None:
    """Pedir un número, convertir a entero y mostrar el doble.

    Si la conversión falla informa el error.
    """
    if valor is None:
        valor = input('Introduce un número: ')
    try:
        n = int(valor)
        print(f'Has introducido {n}. El doble es {2 * n}.')
    except ValueError:
        print(f"'{valor}' no es un entero válido.")


def ejemplo_opcion(op: Optional[str] = None) -> None:
    """Ejemplo simple de elección: (a)ceptar, (r)echazar.

    Si `op` es None pedirá la opción; acepta 'a' o 'r' (insensible a mayúsculas).
    """
    if op is None:
        op = input("Elige una opción — (a)ceptar / (r)echazar: ")
    o = op.strip().lower()
    if o == 'a' or o == 'aceptar':
        print('Has aceptado.')
    elif o == 'r' or o == 'rechazar': # else if
        print('Has rechazado.')
    else:
        print('Opción no reconocida:', op)


if __name__ == '__main__':
    # Demostración no interactiva — pasar valores de muestra
    ejemplo_basico()
    ejemplo_numerico()
    ejemplo_opcion()
