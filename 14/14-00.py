
alph = '0123456789ABCDEFGHI'

for x in alph:
    s = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if s % 18 == 0:
        print(x, s // 18)


# for x in range(19):
#     a = 3 * 19 ** 4 + 2 * 19 ** 3 + 1 * 19 ** 2 + x * 19 + 4
#     b = 4 * 19 ** 4 + 9 * 19 ** 3 + 8 * 19 ** 2 + x * 19 + 9
#     c = a + b

#     if c % 23 == 0:
#         print(c // 23)