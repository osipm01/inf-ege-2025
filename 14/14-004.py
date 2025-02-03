import sys
# yAAx x02y

for x in range(12):
    for y in range(12):
        a = y * 12 ** 3 + 10 * 12 ** 2 + x * 12 + y
        b = x * 14 ** 3 + 0 + 2 * 14 + y

        c = a + b

        if c % 80 == 0:
            print(c // 80)
            sys.exit()

# result_search = []
# for x in '0123456789AB':
#     for y in '0123456789AB':
#         t = int(y + 'AA' + x, 12) + int(x + '02' + y, 14)
#         if t % 80 == 0:
#             result_search.append(t)
# if result_search:         
#     print(min(result_search) // 80)

        
