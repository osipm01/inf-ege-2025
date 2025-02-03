
def f(n):
    s = ''
    k1 = int(n[0]) + int(n[1])
    k2 = int(n[1]) + int(n[2])
    s = s + str(k2)
    s = s + str(k1)
    return s

for i in range(100, 1000):
    c = f(str(i))
    if c == '159':
        print(i)