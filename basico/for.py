'''
    pass
    Simplemente ejecuta el código sin ninguna función adicional

    break
    Deteniene la ejecución del bucle por completo
    
    continue
    Interrumpe la ejecución de esa interación del bucle, pero se siguen ejecuntado el resto
    de las iteraciones que resten para terminar
'''
# for simple
for number in range(10):
    print(number)

# for con indicador de pasos
for iter, number in enumerate(range(18, 25)):
    print(iter, number)

# for con else
for i in range(5):
    print(i)
else:
    print("else:", i)
    