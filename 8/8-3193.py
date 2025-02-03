import itertools

words = []
alph= 'АОУ'
current = 210

for i in itertools.product(alph, repeat = 5):
    words.append(i)

print(words[current - 1])
