'''
    pass
    Simplemente ejecuta el código sin ninguna función adicional

    break
    Deteniene la ejecución del bucle por completo
    
    continue
    Interrumpe la ejecución de esa interación del bucle, pero se siguen ejecuntado el resto
    de las iteraciones que resten para terminar
'''
# while con pasos
steps = 10
while steps > 0:
    print(steps)
    steps -= 1

# while con una condición
run = True
while run:
    answer = input('Si quieres salir introduce exit: ')
    if answer == 'exit':
        run = False

# while con else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
