
count = 0
m = 0

try:
    s = [int(i) for i in open('demo_2025_17.txt')]
except Exception as e:
    print(f'error of read file{e}')


min_val = min(s)
mx = -10 ** 9

for j in range(0, len(s) - 1):
    if s[j] % 16 == min_val or s[j + 1] % 16 == min_val:
        mx = max(mx, s[j + 1] + s[j])
        count += 1

print(f'counter: {count}, max_value: {mx}')


# for j in range(0, len(s) - 1):
#     if s[j] < s[j + 1]:
#         print(s[j] % 16)
#         if s[j + 1] % 16 == s[j]:
#             count += 1
#             m = max(m, s[j] + s[j + 1])
#     else:
#         if s[j] % 16 == s[j + 1]:
#             count += 1
#             m = max(m, s[j] + s[j + 1])
#
# print(f'counter{count}, max {m}')


# for j in range(0, len(s) - 1):
#     pars = []
#     pars.append(s[j])
#     pars.append(s[j + 1])
#     min_val = min(pars)
#
#     if pars[0] < pars[1]:
#         if pars[1] % 16 == pars[0]:
#             count += 1
#         elif pars[1] < pars[0]:
#             if pars[0] % 16 == pars[1]:
#                 count += 1
#         else:
#             pass
#     pars.clear()
#
# print(count)
