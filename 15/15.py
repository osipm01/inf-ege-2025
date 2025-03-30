# ((x ∈ P) ∧ (x ∈ Q)) → (x ∈ A)
# P = [4, 15]
# Q = [12, 20].

P = [i for i in range(4, 16)]
Q = [i for i in range(12, 21)]

res = set()

for Amin in range(1, 100):
    for Amax in range(Amin + 1, 100):
        flag = True
        A = [i for i in range(Amin, Amax)]
        for x in range(-300, 300):
            f = ((x in P) and (x in Q)) <= (x in A)
            if not f:
                flag = False
                break
        if flag:
            res.add((Amax - Amin) - 1)

print(min(res))