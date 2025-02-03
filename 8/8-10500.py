import itertools

alph = '12345'
counter = 0

for i in itertools.product(alph, repeat = 5):
    if i.count('1') == 3:
        counter += 1

print(counter)