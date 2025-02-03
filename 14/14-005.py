

for x in range(12):
    for y in range(12):
        a = x * 11 ** 4 + 3 * 11 ** 3 + 4 * 11 ** 2 + 1 * 11 + y
        b = 5 * 19 ** 4 + 6 * 19 ** 3 + 7 * 19 ** 2 + 8 * 19 + y

        c = a + b

        if c % 80 == 0:
            print(c // 80)

# result_search = []
# for x in '0123456789A':
#     for y in '0123456789A':
#         t = int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)
#         if t % 305 == 0:
#             result_search.append(t)
# if result_search:         
#     print(min(result_search) // 305)