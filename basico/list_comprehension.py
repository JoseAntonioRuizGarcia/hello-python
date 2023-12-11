# List Comprehension Simple
texto = '¡Hola mundo!'
nuevo_texto = []
_ = [nuevo_texto.append(ch + '-') for ch in texto]
print(nuevo_texto)

# List Comprehension con if
texto = '¡Hola mundo!'
nuevo_texto = []
_ = [nuevo_texto.append(ch + '-') for ch in texto if ch not in ['¡', '!']]
print(nuevo_texto)

# List Comprehension anidada
lista_anidada = [
    ['perro', 3, 5, '9', 'coche'],
    ['gato', 15.6, True, 'rojo']
]
numbers = [[int(is_number) for is_number in element if str(is_number).isnumeric()] for element in lista_anidada]
print(numbers)
