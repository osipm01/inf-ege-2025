
def f(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0
    elif h < 3 and x >= 68:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1) 
        
for i in range(1, 70):
    if f(i, 1) == 1:
        print(i)
        break
        