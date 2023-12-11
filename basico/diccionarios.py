# Diccionario simple: clave-valor
simple = {
    'Nombre 1': 'Pedro',
    'Nombre 2': 'Luisa',
    'Nombre 3': 'Juan',
    'Nombre 4': 'Lucia',
    'Nombre 5': 'Damián',
}
print(simple.keys())
print(simple.values())

for clave, valor in simple.items():
    print(f'{clave}: {valor}')

# Diccionario anidado
anidado = {
    'Usuario 1': {
        'nombre': 'Pedro',
        'email': 'pedro@gmail.com'
    },
    'Usuario 2': {
        'nombre': 'Luisa',
        'email': 'luisa@gmail.com'
    },
    'Usuario 3': {
        'nombre': 'Juan',
        'email': 'juan@gmail.com'
    },
    'Usuario 4': {
        'nombre': 'Lucía',
        'email': 'lucia@gmail.com'
    }
}
for usuario in anidado.keys():
    print(f'{usuario}: {anidado[usuario]["nombre"]} - {anidado[usuario]["email"]}')

# Añadir elementos
anidado['Usuario 5'] = {
    'nombre': ['ubuntu', 'linux'],
    'url': 'https://ubuntu.com/'
}
print(anidado)

# Actualizar valores
anidado['Usuario 3']['email'] = 'nuevo_email.com'
print(anidado['Usuario 3'])

# Borrar clave-valor
del anidado['Usuario 3']
print(anidado.keys())

# Borrar último elemento
anidado.popitem()
print(anidado.keys())
