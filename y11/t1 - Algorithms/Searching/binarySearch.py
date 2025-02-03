from math import floor

ls = list(range(1, 100))
fn = int(input())
comp = 0
index = floor(len(ls) / 2)

while comp != fn:
    index = floor(index / 2)

    comp = ls[index]
    if comp > fn:
        ls = ls[:index]
    elif comp < fn:
        ls = ls[index:]
    elif comp == fn:
        print(f"index of {fn} is something")
    if len(ls) == 1:
        print("not found")
