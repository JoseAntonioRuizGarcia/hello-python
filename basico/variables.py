'''
    PEP 8 -- Style Guide for Python Code recomienda la siguiente convención de nomenclatura para variables y funciones en Python:

    Los nombres de las variables deben estar en minúsculas, con palabras separadas por guiones bajos para mejorar la legibilidad
    (por ejemplo: var, mi_variable).

    Los nombres de las funciones siguen la misma convención que los nombres de las variables (por ejemplo: fun, mi_función).
    También es posible usar letras mixtas (por ejemplo: miVariable), pero solo en contextos donde ese ya es el estilo predominante,
    para mantener la compatibilidad retroactiva con la convención adoptada.
'''

# Palabras reservadas
_ = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
    'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

# En caso de querer usar alguna palabra reservada
list_ = 'Nombre variable reservada + _'

# Números Enteros
a = 3
b = -1000
c = 1_000_000
print(a, b, c)

# Números decimales
a = .3
b = -1000.
c = 1_000_000.23
print(a, b, c)

# Octales, Hexadecimales y notación científica
a = 0o123
b = -0x123
c = 3E-8
print(a, b, c)

# Texto
a = 'Hello, world'
b = '8' * 15
c = '-'.join('Hello, world')
print(a, b, c)

# Booleanos
a = True
b = False
c = a == 1
print(a, b, c)
