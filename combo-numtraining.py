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
num_words = 4

def get_rand_2didgit_word():
    x = str(random.randint(0,9)) + str(random.randint(0,9))
    return x, modifiers[int(x[0])] + " " + numbers[int(x[1])]



i = 'a'
while i != 'q':
    obj = [get_rand_2didgit_word() for _ in range(num_words)]
    #print(obj)
    #print(nums)
    #print(words)
    nums = "-".join([x[0] for x in obj])
    words = "-".join([x[1] for x in obj])

    print("what are the words for ", nums)
    _ = input()
    print(words)
    i = input()


