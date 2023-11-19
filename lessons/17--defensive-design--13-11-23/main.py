grades = {
    'Ted': 6,
    'Bob': 7,
    'Poppy': 7,
    'Casey': 8,
    'Phil': 8,
    'Karlie': 6
}

name = ''
while name not in grades.keys():
    name = input('give name\n>> ').capitalize()
    if name not in grades.keys():
        print('you dont exist')
print(grades[name])
