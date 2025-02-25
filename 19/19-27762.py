from sys import setrecursionlimit

setrecursionlimit(1000000)

def f(x, y, h):
    if h == 3 and x + y >= 47:
        return 1
    elif h < 3 and x + y >= 47:
        return 0
    elif h == 3 and x + y < 47:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y + 2, h + 1) or f(x + 2, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y + 2, h + 1) or f(x + 2, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
        
for i in range(1, 40):
    if f(i, 10, 1) == 1:
        print(i)
        break