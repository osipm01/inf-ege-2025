
# 1 вариант ркшкния
# for i in range(0, 10**10, 3013):
#     s = str(i)
#     if s[0] == '1' and s[2:6] == '6961' and s[-1] == '5':
#         print(s)

#2 вариант решения

import fnmatch

for i in range(0, 10**10, 3013):
    if fnmatch.fnmatch(str(i), '1?6961*5'):
        print(i)