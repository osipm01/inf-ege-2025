import fnmatch

mask = '1?3948*5'
for x in range(0, 10 ** 10, 3013):
    if fnmatch.fnmatch(str(x), mask):
        print(x)