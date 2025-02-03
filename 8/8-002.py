
from itertools import product

alph = 'ABCX'
cnt = 0

for i in product(alph, repeat=5):
    if i[0] == 'X' or i[-1] == 'X':
        if i.count('X') == 1:
            cnt += 1

print(cnt)