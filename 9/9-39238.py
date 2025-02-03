
f = open('9-39238.txt')

cnt = 0

for line in f:
    a = [int(x) for x in line.split()]
    a.sort()
    if (a[0] ** 2 + a[1] ** 2 == a[2] ** 2) or (a[1] ** 2 + a[2] ** 2 == a[1] ** 2) or (a[1] ** 2 + a[2] ** 2 == a[0] ** 2):
        cnt += 1

print(cnt)