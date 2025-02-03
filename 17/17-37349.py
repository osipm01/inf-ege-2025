
a = [int(x) for x in open('17-37349.txt','r')]

c = 0
mx = 0

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] * a[j] % 26 == 0:
            c += 1
            mx = max(mx, a[i] + a[j])

print(c, mx
      )