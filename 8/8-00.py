
from itertools import product

alf = "АЛГОРИТМ"

cnt = 0

for word in product(alf, repeat=4):
    cnt += 1
    if word[2] == "И" and word[3] == "М":
        print(cnt)