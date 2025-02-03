import fnmatch

mask = '1?2711*0'

for i in range(0, 10**10, 4891):
    if fnmatch.fnmatch(str(i), mask):
        print(i)