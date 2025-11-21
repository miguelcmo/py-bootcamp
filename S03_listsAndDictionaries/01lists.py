"""
Use of lists in Python and lists methods
"""

from typing import List


def ejemplo_creacion_acceso():
	"""Ejemplo 1: crear una lista y acceder a elementos"""
	frutas = ['manzana', 'banana', 'cereza', 'datil']
	print('\nEjemplo 1 — creación y acceso:')
	print('  lista completa:', frutas)
	print('  primer elemento:', frutas[1])
	print('  último elemento (index -1):', frutas[-2])
	print('  longitud:', len(frutas)) # metodos de listas len() - lenght=logitud
	print('  contiene "banana"?', 'banana' in frutas) # elemento in lista


def ejemplo_modificacion():
	"""Ejemplo 2: modificar una lista (append, extend, insert, pop, remove)"""
	nums = [1, 2, 3]
	print('\nEjemplo 2 — modificación:')
	print('  inicial:', nums)
	nums.append(4) # nombre_de_la_variable.metodo() notacion de OOP - POO
	print('  after append(4):', nums)
	nums.extend([5, 6])
	print('  after extend([5,6]):', nums)
	nums.insert(0, 0)
	print('  after insert(0,0):', nums)
	popped = nums.pop()  # quita y devuelve el último
	print('  pop ->', popped, '; ahora:', nums)
	nums.remove(2)  # elimina la primera ocurrencia de 2
	print('  after remove(2):', nums)


def ejemplo_slicing():
	"""Ejemplo 3: slicing (sublistas y pasos)"""
	letras = list('abcdefgh')
	print('\nEjemplo 3 — slicing:')
	print('  original:', letras)
	print('  letras[1:5]:', letras[1:5])
	print('  letras[:3]:', letras[:3])
	print('  letras[::2] (cada 2):', letras[::2])
	print('  reversed (::-1):', letras[::-1]) # reversar una lista completa
	print('  reversed (::-2):', letras[::-2])


def ejemplo_comprehension():
	"""Ejemplo 4: list comprehension (squares y filtrado)"""
	print('\nEjemplo 4 — list comprehension:')
	cuadrados = [x * x for x in range(6)] # [expresión for elemento in iterable if condición]
	print('  cuadrados 0..5:', cuadrados)
	pares = [x for x in range(20) if x % 2 == 0]
	print('  pares 0..19:', pares)


def ejemplo_anidada_iteracion():
	"""Ejemplo 5: listas anidadas y recorrido con índices"""
	matriz: List[List[int]] = [
		[1, 2, 3],
		[4, 5, 6],
	]
	print('\nEjemplo 5 — lista anidada e iteración:')
	for i, fila in enumerate(matriz):
		for j, val in enumerate(fila):
			print(f'  matriz[{i}][{j}] = {val}')


if __name__ == '__main__':
	ejemplo_creacion_acceso()
	ejemplo_modificacion()
	ejemplo_slicing()
	ejemplo_comprehension()
	ejemplo_anidada_iteracion()

