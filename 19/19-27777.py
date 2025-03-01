
def f(x, y, h):
    if h == 3 and x + y <= 40:
        return 1
    elif h == 3 and x + y > 40:
        return 0
    elif x + y <= 40 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)
        else:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)
        
for i in range(100, 40, -1):
    if f(20, i, 1):
        print(i)
        break
        
    