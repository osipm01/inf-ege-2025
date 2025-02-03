k = 210
n = 600

old_cam = 0
kb = 0

count = 0
len = 0

try:
    data = open('C:/Users/endoc/Documents/ege12/26/26.txt', "r")
except FileNotFoundError:
    print("File not found")
    exit()
    

class Person():
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

bg=[]

for x in data:

    t1, t2 = map(int, x.split())

    person = Person(t1, t2)

    bg[count] = person

    count += 1
    len += 1

    if len == 600:
        break

bg = sorted(bg)

klist = [0] * 211
klist[0] = 10**10

for i in range(0, 600):
    t1 = bg[i].t1   
    t2 = bg[i].t2 

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
