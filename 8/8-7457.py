import itertools

words = []
current = 67 - 1
alph = 'КЛРТ'

for i in itertools.product(alph, repeat = 4):
    words.append(i)

print(*words[current])