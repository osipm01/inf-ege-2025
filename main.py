
def f(s):
    while not '00' in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)

    return s

for i in range(100):
    for j in range(100):
        for k in range(100):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'
            chars = f(s)
            if chars.count('1') == 61 and chars.count('2') == 50 and chars.count('3') == 18:
                print(len(s))