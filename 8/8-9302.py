import itertools

counter = 0
alph = 'МЕТРО'

for i in itertools.product(alph, repeat = 4):
    print(i)
    if (i[0] != 'О' or i[0] != 'Е') and (i[3] == 'О' or i[3] == 'Е'):
        counter += 1

print(counter)