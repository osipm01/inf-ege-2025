
def f(x):
    res = set()
    k = 2
    while x**2 <= k:
        if x % k == 0:
            res.add(k)
            if x // k < x:
                res.add(x // k)
        k = k + 1
    return sorted(res)


for i in range(174457, 174505 + 1):
    if f(i) == 2:
        print(f(i))