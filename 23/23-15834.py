
def f(x, y):
    if x > y or x == 31:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)

print(f(2, 15) * f(15, 35))