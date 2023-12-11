'''
    TENER EN CUENTA:

    Una lista es un elemento MUTABLE, es decir, que se pude modificar en tiempo de ejecución.
    Se puede modificar sus valores, añadir o elimminar nuevos. Al contrario que los elementos
    inmutables, como es el caso de las tuplas.
'''
# Asignar lista
mi_lista = [1, 2, 3, 4, 5]
print(*mi_lista)

mi_lista[2] = 'coche'
print(mi_lista)

# Tamaño
print(len(mi_lista))

# Accediendo a los datos
print(mi_lista[0]) # Primer elemento
print(mi_lista[-1]) # Último elemento
print(mi_lista[:2]) # Desde el primero al elemento 2, no inclusive
print(mi_lista[2:]) # Desde el elemento 2 al último
print(mi_lista[1::2]) # Desde el elemento 1 de dos en dos

# Añadir elementos
mi_lista.append(99)
mi_lista.insert(0, 'perro') # Inserta un elemento en la posición indicada
print(mi_lista)

# Borrar elementos
mi_lista.remove('perro')
elemento = mi_lista.pop(0)
print(f'Se ha eliminado {elemento} del contenido de la lista: {mi_lista}')

# Cast a una lista
tuple_ = (3, 4, 6, 'rojo')
mi_lista = list(tuple_)
print(mi_lista)

# Conteo de un valor
n = mi_lista.count('rojo')
print(f'El valor "rojo" aparece en la lista {n} veces')

# Localizar posición de un valor
pos = mi_lista.index('rojo')
print(f'El valor "rojo" está en la posición {pos} de la lista')

# Ordenar lista
mi_lista = [4, 7, 2, 4, 9, 1]
mi_lista.sort()
print(mi_lista)

'''
    La inmensa mayoría de los métodos de una lista darán error si el valor o posición
    no está dentro de lista. Hay que tratar de evitar los posibles errores.
'''
borrar_elemento = 3
if borrar_elemento in mi_lista:
    mi_lista.remove(borrar_elemento)

else:
    print(f'El valor "{borrar_elemento}" no está dentro de la lista.')

'''
    Especial atención a cómo se trata en memoria las listas. Siempre que se vayan a copiar
    hay que hacerlo desde el método .copy(). Para evitar posibles errores en el tratamiento
'''
# Forma correcta
list_1 = [1]
list_2 = list_1.copy()
list_1[0] = 2
print(list_2)

# Forma incorrecta
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
