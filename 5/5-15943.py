

def f(N):
    s = bin(N)[2:]
    if N % 2 == 0:
        s = s + '00'
        return s
    return s + '11'


for i in range(1, 1000):
    t = f(i)

    if int(t, 2) > 115:
        print(i)

