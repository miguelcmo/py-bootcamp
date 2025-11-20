"""
Python have a bunch of reserved keywords that we cannot use to name variables beacuase Python uses them internally.

If we use any of them, Python throws an error.
"""

# def True():
#     pass
# SyntaxError: invalid sintax


# Use of Python function list() to create a list from the string
a = list("Letras") # list o listas en Python es lo mismo que un array[] en otro lenguajes de programación
print(a)

# Python let us use of 'list' as a fucntion name; in that case, the built-in function list is shadowed by our own function declaration
def list():
    print("Function list")

# a = list("Letras")
# TypeError: list() takes 0 positional arguments but 1 was given


#----------------------
#   Python keywords
#----------------------
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']