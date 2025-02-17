import sys

R = 0

for N in range(0, 10 ** 10):
    R = bin(N)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    if int(R, 2) > 97:
        print(N)
        sys.exit()
