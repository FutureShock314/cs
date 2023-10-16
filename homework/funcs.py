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
