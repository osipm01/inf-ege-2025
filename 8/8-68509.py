
from itertools import product
count = 0
m = []
for p in product(sorted("ПАРУС"), repeat = 5):
    count += 1
    s = ''.join(p)
    if ("АА" not in s) and s.count("У") <= 1:
            m.append(count)
print(max(m))