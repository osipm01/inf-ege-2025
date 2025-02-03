
a = [int(x) for x in open('17-37341.txt', 'r')]

mx = 0
c = 0

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] - a[j]) % 2 == 0) and ((a[i] % 19 == 0) or (a[j] % 19 == 0)):
            c += 1
            mx = max(mx, a[i] + a[j])

print(c, mx)