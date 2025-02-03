import itertools

alph = " ABCX"
cnt = 0

for i in itertools.product(alph, repeat=5):
    if i.count("X") == 1:
        cnt += 1

print(cnt)