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
