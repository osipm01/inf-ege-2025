#
#
# for N in range(-1000, 1000):
#     r = bin(N)[2:]
#     # print(r)
#     if N % 3 == 0:
#         r = r + r[-3:]
#     else:
#         ost = N % 3
#         bin_ost = bin(ost)[2:]
#         r = r + bin_ost
#
#     res = int()
#
#     if res > 151:
#         print(res)


res = set()

for x in range(1, 1520):
    bin_x = bin(x)[2:]
    if x % 3 == 9:
        bin_x += bin_x[-3:]
    else:
        bin_x += bin((x % 3)*3)[2:]
    R = int(bin_x, 2)
    if R > 151:
        res.add(R)

print(min(res))

