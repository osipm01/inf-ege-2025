k = 70

for x in range(k):
    for y in range(k):
        for z in range(k):
            s = '0' + '1'* x + '2'* y + '3'* z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)

            if s.count('1') == 20 and s.count('2') == 10 and s.count('3') == 70:
                print(x)
