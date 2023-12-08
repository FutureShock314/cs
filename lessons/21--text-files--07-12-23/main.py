file = open('/workspaces/CS/lessons/21--text-files--07-12-23/main.txt', 'a')
for i in range(1_000_001):
    file.write('Howdy!')
    if i % 10000 == 0:
        print(i)
file.close()
