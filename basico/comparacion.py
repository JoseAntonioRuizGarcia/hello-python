# Igual ==
print(2 == 2)

# Distinto
print(1 != 2)

# Mayor
print(3 > 5)

# Mayor o igual
print(3 >= 5)

# Menor
print(3 < 5)

# Menor o igual
print(3 >= 5)

# Negación
if 'rojo' not in ['verde', 'azul', 'amarillo']:
    print('Añadir el color rojo')
'''
    Recomendable usar el not después la variable y no antes

    No usar así, aunque funciona correctamente:
    if not 'rojo' in ['verde', 'azul', 'amarillo']:
        print('Añadir el color rojo')

'''
if ~('rojo' in ['verde', 'azul', 'amarillo']):
    print('Añadir el color rojo')

# And
if 3 > 1 and 5 < 10:
    print('Bucle and')

if (3 > 1) & (5 < 10):
    print('Bucle and')

# Or
if 3 > 1 or 5 < 10:
    print('Bucle or')

if (3 > 1) | (5 < 10):
    print('Bucle or')
