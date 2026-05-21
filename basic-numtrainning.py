import random

modifiers = ['space',
             'religious',
             'cyberpunk',
             'rainbow',
             'goth',
             'ocean',
             'barbie',
             'art deco',
             'forest',
             'steampunk',
             ]

numbers = ['tire',
           'book',
           'tower',
           'cup',
           'stool',
           'trophy',
           'hex nut',
           'slot machine', 
           'desktop',
           'dumbbell',
           ]
i = 'a'
while i != 'q':
    x = str(random.randint(0,9)) + str(random.randint(0,9))
    print('what is the associated object for ', x)
    _ = input()
    obj = modifiers[int(x[0])] + " " + numbers[int(x[1])]
    print(obj)
    i = input()


