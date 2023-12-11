'''
    TENER EN CUENTA:

    Una tupla es un elemento INMUTABLE, es decir, que NO se puede modificar en tiempo de ejecución.
    Al contrario que los elementos mutables, como es el caso de las listas.
'''
mi_tupla = ()
mi_tupla = (1, 2, True, 'rojo')
mi_tupla = 'verde', 3.3, False, 8, 14 

# Accediendo a los datos
print(mi_tupla[0]) # Primer elemento
print(mi_tupla[-1]) # Último elemento
print(mi_tupla[:2]) # Desde el primero al elemento 2, no inclusive
print(mi_tupla[2:]) # Desde el elemento 2 al último
print(mi_tupla[1::2]) # Desde el elemento 1 de dos en dos
