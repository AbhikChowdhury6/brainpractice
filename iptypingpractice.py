import random

i = 'a'
while i != 'q':
    val = '.'.join([str(random.randint(0,255)) for _ in range(4)])
    print(val)
    i = input()
    if i == val:
        print("correct!")
    else:
        print("wrong")
    print()