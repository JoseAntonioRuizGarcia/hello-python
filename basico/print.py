# Básico
print('Hello World')

# Con salto de línea
print('Primera línea.\nSegunda línea.')

# Varios argumentos con textos y/o variables
texto = 'argumento'
print('Primer argumento,', 'Segundo argumento,', 3, texto)

# Distinto separador
print(1, 2, 3, 4, sep='-')

# Distinto fin, por defecto python usa  \n salto de línea
print(1, 2, end='\t')
print(3, 4)

# Repetición de caracteres
print('#' * 20)

# Incluir variables dentro de la cadena de texto
name = 'Jose'
print(f'Mi nombre es {name}')

# Usando tuplas para formatear
number = 13.14159
pi = 'π'
print('El número %s = %.3f' % (pi, number))

# Imprimir los elementos de una lista
my_list = [0, 1, 2, 3, 4, 5]
print(*my_list)
