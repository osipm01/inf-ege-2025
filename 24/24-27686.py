f = open('24-27686.txt', 'r')
a = f.readline()

c = 0
mx = 0

for i in range(len(a)):
    if a[i] == 'X' and a[i + 1] == 'X':
        c += 1
        if c > mx: mx = c

    else: c = 1

print(max(c, mx))