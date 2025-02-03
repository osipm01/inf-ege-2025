import sys

R = 0

for N in range(0, 10 ** 10):
    R = bin(N)[2:]
    R += str(R.count('1') % 2)
    R += str(R.count('1') % 2)
    if int(R, 2) > 97:
        print(N)
        sys.exit()

# for n in range(0, 1000000):
#     r=bin(n)[2:]
#     r+= str(r.count('1')%2)
#     r+= str(r.count('1')%2)
#     if int(r,2)>97:
#         print (n)
#         break