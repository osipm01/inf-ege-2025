import itertools

# def checker(val):
#     for j in range(0, len(val)):
#         if int(val[j]) % 2 != 0 and int(val[j + 1]) % 2 != 0:
#             return True
#     return False
#
# def cheker_ret(val):
#     pass
#
#
# slovar = '01234567'
#
# res = set()
#
# for i in itertools.product(slovar, repeat = 5):
#     if i.count('1') == 0:
#         if checker(i):
#             print(
#                 i
#             )

cnt = 0
col = itertools.product('01234567', repeat = 5)
for w in col:
    numb = ''.join(w)
    if '1' not in numb and numb[0] != '0' and len(set(numb)) == 5 and \
        all(int(numb[i]) % 2 != int(numb[i+ 1]) % 2 for i in range(len(numb)-1)):
        cnt += 1

print(cnt)