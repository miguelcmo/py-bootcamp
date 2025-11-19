"""
Use of range and while in Python
"""

def ejemplo_range_basico():
	"""Ejemplo 1: range básico (0..4)"""
	print('\nEjemplo 1 — range básico:')
	for i in range(5):
		print('  i =', i)


def ejemplo_range_start_step():
	"""Ejemplo 2: range con start/stop/step (pares 2..10)"""
	print('\nEjemplo 2 — range con start/stop/step:')
	for i in range(2, 11, 2):
		print('  even =', i)


def ejemplo_range_inverso():
	"""Ejemplo 3: range inverso (cuenta regresiva)"""
	print('\nEjemplo 3 — range inverso (countdown):')
	for i in range(5, 0, -1):
		print('  countdown =', i)


def ejemplo_while_contador():
	"""Ejemplo 4: while simple con contador y condición de salida"""
	print('\nEjemplo 4 — while con contador:')
	n = 0
	while n < 5:
		print('  n =', n)
		n += 1


def ejemplo_while_else():
	"""Ejemplo 5: while-else — busca primer múltiplo de 7 en un rango

	El `else` se ejecuta si el `while` termina sin `break`.
	"""
	print('\nEjemplo 5 — while-else (buscar múltiplo de 7):')
	x = 1
	limit = 20
	while x <= limit:
		if x % 7 == 0:
			print('  → Encontrado múltiplo de 7:', x)
			break
		x += 1
	else:
		print('  → No se encontró ningún múltiplo de 7 hasta', limit)


if __name__ == '__main__':
	ejemplo_range_basico()
	ejemplo_range_start_step()
	ejemplo_range_inverso()
	ejemplo_while_contador()
	ejemplo_while_else()

