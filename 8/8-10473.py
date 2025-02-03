import itertools

counter = 0
alph = '1234'

for i in itertools.product(alph, repeat = 5):
    if i.count('1') == 2:
        counter += 1

print(counter)