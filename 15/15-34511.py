
for A in range(100):
    flag = True
    for x in range(100):
        if ((x & 25 == 0) or (x & 19 != 0) or (x & A != 0)) == 0:
            flag = False
    if flag:
        print(A)
        break