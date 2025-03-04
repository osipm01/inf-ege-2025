

def f(N):
    b_n = bin(N)[2:]
    if N % 2 == 0:
        b_n = '10' + b_n
    else:
        b_n = '1' + b_n + '01'
    return int(b_n, 2)

for N in range(100):
    R = f(N)
    if R > 516:
        print(N)
        break