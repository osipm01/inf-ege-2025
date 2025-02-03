
s = [int(x) for x in open('17-37336.txt', 'r')]

cnt = 0
m = -20 ** 10

for i in range(len(s) - 1):
    if s[i] % 3 == 0 or s[i + 1] % 3 == 0:
        cnt += 1
        m = max(m, s[i] + s[i - 1])
print(cnt, m)
