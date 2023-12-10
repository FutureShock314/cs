import os

def rw(mode: str, filepath: str, message: str):
        if mode == 'r':
            if os.path.exists(filepath):
                with open(filepath, mode) as f:
                    print(f.read())
            else:
                print(f'Failed to read file \'{ filepath }\', no such file')
        else:
            with open(filepath, mode) as f:
                f.write(message)

filepath = input('What is the path of the file you wish to create, or edit?\n>> ')

while filepath == '':
    print('i need a filepath mate')
    filepath = input('What is the path of the file you wish to create, or edit?\n>> ')

mode = input('How would you like to open your file? (r, a, w) \n>> ')
message = input('What would you like to write? (leave blank if read)\n>> ')
rw(mode = mode, filepath = filepath, message = message)
