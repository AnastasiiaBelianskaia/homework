import sys
import os

def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide( number_one, number_two):
    return number_one // number_two

if __name__ == '__main__':
    func_name = os.environ.get('FUNCTION', 'add')
    args = sys.argv[1:]

    if len(args) != 2:
        print('need 2 args')
        sys.exit(2)

    ARR_FIRST, ARR_SECOND= args
    try:
        ARR_FIRST = int(args[0])
        ARR_SECOND = int(args[1])
    except ValueError:
        print('need both int')
        sys.exit(2)

    functions = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
    }

    if func_name not in functions:
        print('wrong name')
        sys.exit(2)

    print(functions[func_name](ARR_FIRST, ARR_SECOND))
