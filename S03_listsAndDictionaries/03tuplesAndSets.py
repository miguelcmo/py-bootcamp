
"""
Use of Tuples and Sets in Python, methods, and iteration
"""

from typing import Tuple, Set


def ejemplo_tuple_creacion_acceso():
	"""Ejemplo 1: crear una tupla y acceder a sus elementos"""
	t: Tuple[str, ...] = ('rojo', 'verde', 'azul')
	print('\nEjemplo 1 — tupla creación y acceso:')
	print('  tupla:', t)
	print('  primer elemento:', t[0])
	print('  último elemento:', t[-1])
	print('  longitud:', len(t))


def ejemplo_tuple_unpack_immutabilidad():
	"""Ejemplo 2: desempaquetado y mostrar inmutabilidad"""
	point: Tuple[int, int] = (10, 20)
	x, y = point  # unpacking
	print('\nEjemplo 2 — unpacking y inmutabilidad:')
	print('  point =', point)
	print('  x =', x, ', y =', y)
	try:
		# las tuplas son inmutables; esto causará TypeError si se intenta asignar
		point[0] = 5  # type: ignore
	except Exception as e:
		print('  intentar modificar tupla ->', type(e).__name__, ':', e)


def ejemplo_tuple_metodos():
	"""Ejemplo 3: métodos útiles de tupla: count() y index()"""
	t = (1, 2, 2, 3, 2)
	print('\nEjemplo 3 — métodos de tupla (count / index):')
	print('  tupla:', t)
	print('  count(2):', t.count(2))
	print('  index(3):', t.index(3))


def ejemplo_set_creacion_membresia():
	"""Ejemplo 4: crear un set y comprobar membresía"""
	s: Set[str] = {'manzana', 'pera', 'naranja'}
	print('\nEjemplo 4 — set creación y membresía:')
	print('  set:', s)
	print("  'pera' in s?", 'pera' in s)
	print("  'banana' in s?", 'banana' in s)


def ejemplo_set_operaciones():
	"""Ejemplo 5: operaciones entre sets — unión, intersección, diferencia"""
	a = {1, 2, 3, 4}
	b = {3, 4, 5, 6}
	print('\nEjemplo 5 — operaciones de sets:')
	print('  a:', a)
	print('  b:', b)
	print('  union (a | b):', a | b)
	print('  intersección (a & b):', a & b)
	print('  diferencia (a - b):', a - b)


def ejemplo_set_mutacion_frozenset():
	"""Ejemplo 6: mutación (add/remove) y uso de frozenset (inmutable)"""
	s = set([10, 20])
	print('\nEjemplo 6 — mutación de set y frozenset:')
	print('  inicial:', s)
	s.add(30)
	print('  after add(30):', s)
	s.discard(20)
	print('  after discard(20):', s)
	fs = frozenset(s)
	print('  frozenset(s):', fs)
	try:
		fs.add(40)  # frozenset no permite add -> AttributeError
	except Exception as e:
		print('  intentar modificar frozenset ->', type(e).__name__, ':', e)


if __name__ == '__main__':
	ejemplo_tuple_creacion_acceso()
	ejemplo_tuple_unpack_immutabilidad()
	ejemplo_tuple_metodos()
	ejemplo_set_creacion_membresia()
	ejemplo_set_operaciones()
	ejemplo_set_mutacion_frozenset()
