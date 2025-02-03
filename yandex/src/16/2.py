
def f(n):
    if n < 2:
        return 1
    if n >= 2:
        return f(n - 2) + f(n - 1)

for n in range(1000):
    if f(n) == 34:
        print(n)