
# заменить (111, 2)
# заменить (222, 11)


for n in range(61,71):
    s = '1' * n
    while '111' in s:
        s=s.replace('111','2',1)
        s=s.replace('222','11',1)
    if s == '2211':
        break
print(n)