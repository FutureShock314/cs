def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def div(a, b):
    if 0 in (a, b):
        print('no')
        return
    print(a / b)

if __name__ == '__main__':
    num1 = int(input('give num\n>> '))
    num2 = int(input('give num\n>> '))

    add(num1, num2)
    add(num1, 0)
    subtract(num1, num2)
    subtract(num1, 0)
    multiply(num1, num2)
    multiply(num1, 0)
    div(num1, num2)
    div(num1, 0)
