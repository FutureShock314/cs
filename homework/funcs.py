# for hw3
import statistics
def getMean():
    nums = []
    inp = ''
    while inp.lower() != 'done':
        inp = input('give num or say \'done\' to finish\n>> ')
        try:
            nums.append(int(inp))
            print(nums)
        except ValueError:
            if inp.lower() == 'done':
                break
            print('invalid input')
            continue
    print(statistics.mean(nums))


# for hw4

def cipher():
    inp = input('give me a string to enchipher\n>> ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cipher = int(input('what num should i increase by\n>> '))
    out = ''
    for char in inp:
        if char == ' ':
            out += char
            continue
        start = alphabet.index(char)
        shifted = start + cipher
        while shifted > 26:
            shifted -= 26
        out += alphabet[shifted]
    print(out)

# for hw5

def salaryCalc():
    
