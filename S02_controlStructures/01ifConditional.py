"""
Use of `if`, `else`, `elif`, logical operators, and the ternary operator in Python.
"""

def example_basic_if():
	"""Example 1: simple `if`"""
	x = 5
	print('\nExample 1 — basic if:')
	print('x =', x)
	if x > 0:
		print('  → x is positive')


def example_if_else():
	"""Example 2: `if` with `else`"""
	n = 4
	print('\nExample 2 — if / else:')
	print('n =', n)
	if n % 2 == 0:
		print('  → n is even')
	else:
		print('  → n is odd')


def example_elif():
	"""Example 3: `if` / `elif` / `else` chain"""
	score = 85
	print('\nExample 3 — if / elif / else:')
	print('score =', score)
	if score >= 90:
		grade = 'A'
	elif score >= 80:
		grade = 'B'
	elif score >= 70:
		grade = 'C'
	else:
		grade = 'F'
	print(f'  → grade = {grade}')


def example_logical_operators():
	"""Example 4: combining conditions with `and` / `or`"""
	age = 20
	has_id = True
	print('\nExample 4 — logical operators (and / or):')
	print(f'age = {age}, has_id = {has_id}')
	if age >= 18 and has_id:
		print('  → Entry allowed')
	else:
		print('  → Entry denied')


def example_ternary():
	"""Example 5: ternary conditional expression (inline)"""
	temp = 15
	print('\nExample 5 — ternary operator:')
	print('temp =', temp)
	status = 'warm' if temp > 20 else 'cold'
	print(f'  → status = {status}')

"""
¿Qué significa if __name__ == '__main__':?
Cuando un archivo Python se ejecuta directamente (por ejemplo, python archivo.py):
La variable especial __name__ toma el valor '__main__'.
Cuando el archivo se importa desde otro archivo:
__name__ toma el nombre del módulo (por ejemplo, 'mi_modulo').
Por eso se usa este condicional: permite que cierto código solo corra cuando el archivo es ejecutado directamente.
"""
if __name__ == '__main__':
	# Run all examples when executed as a script
	example_basic_if()
	example_if_else()
	example_elif()
	example_logical_operators()
	example_ternary()

