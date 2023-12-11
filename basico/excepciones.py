def dividirNumeros(num1: int, num2: int) -> None:
    try:
        result = num1 / num2
        print(result)

        if result % 2 == 0.0:
            raise Exception('Error provocado deliberadamente')

    except ZeroDivisionError as err:
        print('No puedes dividir un número entre 0')
        print(f'Información del error: {err.args}')
    
    except TypeError:
        print('Ambos argumentos tienen que ser números enteros')
    
    except Exception as err:
        # Error por defecto
        print(err)

dividirNumeros(30, 0)
dividirNumeros(30, 'texto')
dividirNumeros(8, 2)
