"""
Use od dictionaries in Python, methods and looping methods
"""

from typing import Dict


def ejemplo_creacion_acceso():
	"""Ejemplo 1: crear un diccionario y acceder a sus elementos"""
	persona = {'nombre': 'Ana', 'edad': 28, 'pais': 'ES'}
	print('\nEjemplo 1 — creación y acceso:')
	print('  diccionario:', persona)
	print("  nombre:", persona['nombre'])
	print("  edad (get):", persona.get('edad'))
	print("  ciudad (get con default):", persona.get('ciudad', 'Desconocida'))


def ejemplo_agregar_actualizar_eliminar():
	"""Ejemplo 2: añadir, actualizar y eliminar claves"""
	d = {'a': 1, 'b': 2}
	print('\nEjemplo 2 — añadir/actualizar/eliminar:')
	print('  inicial:', d)
	d['c'] = 3  # añadir
	print('  after add c=3:', d)
	d['a'] = 10  # actualizar
	print('  after update a=10:', d)
	v = d.pop('b')  # eliminar y devolver
	print('  pop b ->', v, '; ahora:', d)
	# eliminar con del
	del d['c']
	print('  after del c:', d)


def ejemplo_iteracion():
	"""Ejemplo 3: iterar por claves, valores y pares (items)"""
	stock = {'manzana': 10, 'pera': 5, 'naranja': 8}
	print('\nEjemplo 3 — iteración:')
	print('  claves:')
	for k in stock.keys():
		print('   -', k)
	print('  valores:')
	for val in stock.values():
		print('   -', val)
	print('  items (clave, valor):')
	for k, v in stock.items():
		print(f'   - {k}: {v}')


def ejemplo_anidado():
	"""Ejemplo 4: diccionarios anidados (estructuras más complejas)"""
	agenda: Dict[str, Dict[str, str]] = { # type annotations or type hints
		'juan': {'telefono': '111-222', 'email': 'juan@example.com'},
		'maria': {'telefono': '333-444', 'email': 'maria@example.com'},
	}
	print('\nEjemplo 4 — diccionarios anidados:')
	for nombre, info in agenda.items():
		print(f'  {nombre} -> telefono: {info["telefono"]}, email: {info["email"]}')


def ejemplo_comprehension():
	"""Ejemplo 5: dict comprehension (ej: cuadrados)"""
	print('\nEjemplo 5 — dict comprehension:')
	cuadrados = {x: x * x for x in range(6)}
	print('  cuadrados 0..5:', cuadrados)


def ejemplo_get_setdefault_merge():
	"""Ejemplo 6: uso de get, setdefault y fusión/merge de diccionarios"""
	a = {'x': 1}
	b = {'y': 2}
	print('\nEjemplo 6 — get, setdefault, merge:')
	print('  a:', a)
	print('  b:', b)
	print("  a.get('z') ->", a.get('z'))
	a.setdefault('z', 99)
	print("  after setdefault('z',99):", a)
	# Merge (Python 3.9+): use | or dict unpacking
	merged = a | b
	print('  merged (a | b):', merged)


if __name__ == '__main__':
	ejemplo_creacion_acceso()
	ejemplo_agregar_actualizar_eliminar()
	ejemplo_iteracion()
	ejemplo_anidado()
	ejemplo_comprehension()
	ejemplo_get_setdefault_merge()

