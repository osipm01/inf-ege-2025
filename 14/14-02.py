
alph = '0123456789ABCDE'

for i in alph:
    s = int(f'123{i}515', 15) + int(f'1{i}23315', 15)
    if s % 14 == 0:
        print(s // 14, int(i, 15))
