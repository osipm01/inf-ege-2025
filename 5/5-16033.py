

for N in range(0, 100):
    s = bin(N)[2:]
    s = str(s)
    # print(R)
    if N % 2 == 0:
        s += '01'
    else:
        s += '10'
    R = int(s, 2)
    if R > 102:
        print(R)
        break

