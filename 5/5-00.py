
res = set()

for n in range(1, 12):
    if n % 2 == 0:
        s = bin(n)[2:]
        s = '1' + s
        i = int(s, 2)
        res.add(i)
    else:
        s = bin(n)[2:]
        s = '1' + s + '01'
        i = int(s, 2)
        res.add(i)

print(max(res))