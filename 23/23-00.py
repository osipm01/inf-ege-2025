def f(x, y, _str):
    if x == y:
        if '33' not in _str:
            return 1
        return 0
    if x > y:
        return 0

    return f(x + 1, y, _str + '1') + f(x + 2, y, _str + '2') + f(x * 2, y, _str + '3')


print(f(1, 11, ''))