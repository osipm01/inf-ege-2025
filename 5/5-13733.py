import sys


def calc_summ(bin_val) -> int:
    summ = 0
    for i in range(len(bin_val)):
        summ += int(bin_val, 2)
    return summ

for N in range(0, 10 ** 10):
    r = bin(N)[2:]
    r = str(r)
    sm = calc_summ(r)
    r = r + str(sm % 2)
    r = str(r)
    sm = calc_summ(r)
    r = r + str(sm % 2)

    if int(r, 2) > 83:
        print(N)
        sys.exit()

