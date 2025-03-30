P = [i for i in range(10, 30)]
Q = [i for i in range(13, 19)]

# if (((x in A) <= (x in P)) or (x in Q)):
res = set()

for Amin in range(1, 100):
    for Amax in range(Amin + 1, 100):
        flag = True
        A = [i for i in range(Amin, Amax)]
        for x in range(-300, 300):
            f = ((x in A) <= (x in P)) or (x in Q)
            if not f:
                flag = False
                break
        if flag:
            res.add((Amax - Amin) - 1)

print(min(res))