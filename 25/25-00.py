import fnmatch

mask = '3?12?14*5'

for x in range(0, 10 ** 10, 1917):
    if fnmatch.fnmatch(str(x), mask):
        print(x, x / 1917)