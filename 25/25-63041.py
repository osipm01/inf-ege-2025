from fnmatch import fnmatch

mask = '1*4302?1'

for i in range(0, 10**10, 3147):
    if fnmatch(str(i), mask):
        print(i, i // 3147)