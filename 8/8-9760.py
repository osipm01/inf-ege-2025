
import itertools

alph = "ABCX"
cnt = 0

for i in itertools.product(alph, repeat = 5):
    if i[0] == 'X' or i.count("X") == 0:
        cnt += 1

print(cnt)