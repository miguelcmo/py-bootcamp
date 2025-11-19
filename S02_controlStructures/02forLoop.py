"""
Use of for loop in Python
"""

def ejemplo_basico_lista():
	"""Ejemplo 1: for sobre una lista"""
	frutas = ['manzana', 'banana', 'cereza']
	print('\nEjemplo 1 — for básico sobre lista:')
	for fruta in frutas:
		print('  -', fruta)


def ejemplo_range_pasos():
	"""Ejemplo 2: usar `range(start, stop, step)`"""
	print('\nEjemplo 2 — range con pasos:')
	for i in range(0, 10, 2):
		print('  i =', i)


def ejemplo_enumerate():
	"""Ejemplo 3: obtener índices con `enumerate()`"""
	palabras = ['hola', 'mundo', 'python']
	print('\nEjemplo 3 — enumerate para índices y valores:')
	for idx, palabra in enumerate(palabras, start=1):
		print(f'  {idx}: {palabra}')


def ejemplo_zip():
	"""Ejemplo 4: iterar varias secuencias con `zip()`"""
	nombres = ['Ana', 'Luis', 'Marta']
	edades = [23, 30, 28]
	print('\nEjemplo 4 — zip para recorrer varias listas a la vez:')
	for nombre, edad in zip(nombres, edades):
		print(f'  {nombre} tiene {edad} años')


def ejemplo_for_anidado():
	"""Ejemplo 5: for anidado — recorrer una 'matriz' de coordenadas"""
	matriz = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9],
	]
	print('\nEjemplo 5 — for anidado (matriz):')
	for fila_idx, fila in enumerate(matriz):
		for col_idx, valor in enumerate(fila):
			print(f'  fila {fila_idx}, col {col_idx} -> {valor}')

"""
¿Qué significa if __name__ == '__main__':?
Cuando un archivo Python se ejecuta directamente (por ejemplo, python archivo.py):
La variable especial __name__ toma el valor '__main__'.
Cuando el archivo se importa desde otro archivo:
__name__ toma el nombre del módulo (por ejemplo, 'mi_modulo').
Por eso se usa este condicional: permite que cierto código solo corra cuando el archivo es ejecutado directamente.
"""
if __name__ == '__main__':
	ejemplo_basico_lista()
	ejemplo_range_pasos()
	ejemplo_enumerate()
	ejemplo_zip()
	ejemplo_for_anidado()

