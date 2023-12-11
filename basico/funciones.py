'''
    RECUERDA:

    * Los parámetros solo existen dentro de las funciones (este es su entorno natural).
    * Los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.
    * Si una función no devuelve un cierto valor utilizando una cláusula de expresión return, se asume que devuelve implícitamente None.
'''
def helloWord() -> None:
    print('Hello World')

def message(text: str) -> None:
    print(text)

def sumNumber(num1: int, num2: int, verbose: bool = False) -> int:
    result = num1 +  num2
    if verbose: print(result)

    return result

def sumNumbers(*args: int, verbose: bool = True) -> int:
    result = 0

    for number in args:
        result += number
    if verbose: print(result)

    return result

def printUser(**kwargs) -> None:
    for user in kwargs:
        control = (
            ('name' in kwargs[user].keys())
            & ('age' in kwargs[user].keys())
        )
        if  control:
            print(f'Usuario {user}: {kwargs[user]["name"]} Edad: {kwargs[user]["age"]}')
        
        else:
            print('Error en los datos introducidos.')

if __name__ == '__main__':
    helloWord()
    message('Mensaje enviado')
    sumNumber(10, 4, verbose=True)
    sumNumbers(1, 5, 3, 9, 10)

    users = {
        '1': {
            'name': 'Jose',
            'age': 41
        },
        '2': {
            'name': 'Paula',
            'age': 48
        },
        '3': {
            'name': 'Ramón',
            'age': 29
        }
    }
    printUser(**users)
