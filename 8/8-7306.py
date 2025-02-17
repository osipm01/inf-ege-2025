import itertools

alph = 'УЧЕНИК'
counter = 0

for i in itertools.product(alph, repeat = 5):
    if i[0] == 'У' and i[4] == 'К':
        counter += 1

print(counter)