import itertools

alph = "0123456789AB"

cnt = 0

for i in itertools.product(alph, repeat = 5):
    t = i.count("9") + i.count("A") + i.count("B")
    if t <= 3 and i.count("7") == 1:
        cnt += 1
print(cnt)
