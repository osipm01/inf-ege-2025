# 245690;245756

for a in range(245690, 245756 + 1):
    c = []
    for x in range(1, a // 2):
        if a % x == 0:
            c.append(x)

    if len(c) == 3:
        print(a, c)