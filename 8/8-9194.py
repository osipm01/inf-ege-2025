import itertools

alph = 'ГОД'
counter = 0

for i in itertools.product(alph, repeat = 6):
    if (i[0] == 'Г' or i[0] == 'Д') and (i[5] == 'Г' or i[5] == 'Д'):
        counter += 1

print(counter)
