import fnmatch


mask = '12??1*56'

for x in range(0, 10 ** 8, 317):
    if fnmatch.fnmatch(str(x), mask): print(x)