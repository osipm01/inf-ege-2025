k = 210
n = 600

old_cam = 0
kb = 0

count = 0

data = open('C:/Users/endoc/Documents/ege12/26/26.txt', "r")

bg=[[0]*2 for i in range(0,600)]

for x in data:
    t1, t2 = map(int, x.split())
    bg[count][0]=t1
    bg[count][1]=t2
    # bg[count]=[t1,t2]
    count += 1

bg = sorted(bg)

klist = [0] * 211
klist[0] = 10**10

for i in range(0, 600):
    t1 = bg[i][0]   
    t2 = bg[i][1] 

    for j in range(1, 211):
        if klist[j] > t1:
            klist[j] = 0
    
    _index = klist.index(0)

    if _index > 0:
        klist[_index] = t1

        klist[_index] = t2

        kb += 1
        old_cam = _index

print(kb, old_cam)
