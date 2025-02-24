
def f(x, h):
    if x <= 19 and h == 3:
        return 1
    elif x <= 19 and h < 3:
        return 0
    elif x > 19 and h == 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x - 2, h + 1) or f(x - 5, h + 1) or f(x // 3, h + 1)
        else:
            return f(x - 2, h + 1) and f(x - 5, h + 1) and f(x // 3, h + 1)
        
for i in range(60, 20, -1):
    if f(i, 1):
        print(i)
        break
        