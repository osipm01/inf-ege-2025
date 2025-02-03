
n = "1984"

def f(n):
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    s3 = int(n[2]) + int(n[3])

    s = [s1, s2, s3]
    s_min = min(s)

    s.remove(s_min)

    return s

def printf(n):
    s = ""

    s1 = min(n)
    s2 = max(n)

    s += str(s1)
    s += str(s2)

    return int(s)

# arr = f("1984")
# print(printf(arr))
for i in range(1000, 2000):
    arr = f(str(i))
    if printf(arr) == 613:
        print(i)
