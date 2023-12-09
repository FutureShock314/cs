from main import add, subtract, multiply, div

calc = input('give calculation\n>> ')
funcs = ['+', '-', '/', '*']

for func in funcs:
    if func in calc:
        calc = calc.split(func)
        print('i didnt finish this lol')
