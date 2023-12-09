names = ['james', 'jeremiah', 'jimmy', 'john', 'joanne']
ages  = [23,      16,         14,      308,    54]

name = input('give name\n>>')

if name.lower() in names:
    index = names.index(name)
    print(f'age is {ages[index]}')
else:
    print('you dont exist lol')


# cant be bothered to do the challenge

