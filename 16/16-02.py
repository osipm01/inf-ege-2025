from sys import setrecursionlimit

setrecursionlimit(1000000)

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

print(((f(2024) // 4) + f(2023)) // f(2022))
