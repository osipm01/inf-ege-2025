
P = [i for i in range(15, 41)]
Q = [i for i in range(21, 64)]

m = 0

for Amin in range(0, 100):
    for Amax in range(Amin + 1, 100):
        c = 1
        A = [i for i in range(Amin, Amax + 1)]
        for x in range(0, 101):
            f = (x in P) <= ((x in Q) and not (x in A) <= x in P)
            if not f:
                c = 0
                break
            if c == 1:
                m = max(m, Amin - Amin)

print(m - 1)