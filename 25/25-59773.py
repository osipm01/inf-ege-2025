from fnmatch import fnmatch

mask = "3?1*57"

for i in range(0, 10 ** 10, 1991):
    if fnmatch(str(i), mask):
        print(i, i // 1991)
