
def f(x, h):
    if x >= 65 and h == 3:
        return 1
    elif x >= 65 and h > 3:
        return 0
    elif x < 65 and h == 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 3, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 2, h + 1)  or f(x * 3, h + 1)
            
for i in range(1, 65):
    if f(i, 1) == 1:
        print(i)
        break