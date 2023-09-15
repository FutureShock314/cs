print('enter a number')
num1 = input()
print('enter another number')
num2 = input()
print( int(num1) + int(num2) )


print(132 + 112)
print(35.4 - 3.7)
print(45 / 6)
print(9.5 * 4.3)
print(3 ** 3)
print(112.5 - 34.72 + 233)
print(7 / 3 + 14)
print(8.5 + 2 ** 6)
print(8.4 * 2.3 * 1.1)
print(2.3 / 1.2 + 4)

# Import Module
from PySimpleGUI import *

# GUI Layout
layout = [[Txt(''  * 10)],
          [Text('', size = (15, 1), font = ('Helvetica', 18),
                text_color = 'black', key = 'input')],
          [Txt(''  * 10)],
          [ReadFormButton('c'), ReadFormButton('«')],
          [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
          [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
          [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
          [ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
          ]

# Set PySimpleGUI
form = FlexForm('CALCULATOR', default_button_element_size = (5, 2),
                auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)

# Result Value
Result = ''

# Make Infinite Loop
while True:
    # Button Values
    button, value = form.Read()

    # Check Press Button Values
    if button == 'c':
        Result = ''
        form.FindElement('input').Update(Result)
    elif button=='«':
        Result = Result[:-1]
        form.FindElement('input').Update(Result)
    elif len(Result) == 16 :
        pass

   # Results
    elif button == '=':
        Answer = eval(Result)
        Answer = str(round(float(Answer),3))
        form.FindElement('input').Update(Answer)
        Result = Answer

    # close the window
    elif button == 'Quit'  or button == None:
        break
    else:
        Result += button
        form.FindElement('input').Update(Result)

