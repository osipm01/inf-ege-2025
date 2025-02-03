
for A in range(100):
    flag = True
    for x in range(100):
        if((x&29==0) or (x&12!=0) or (x&A!=0))==0:
            flag = False
    if flag:
        print(A)
        break