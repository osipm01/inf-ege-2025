
def f(n):
    if n <= 10:
        return n
    if n > 10 and n < 36:
        return n // 4 + f(n - 10)


print(f(18))