# 9992

N = 9992

atr = 0
price = 1
many = 2

mid_price = 0

res = []
db = []
codes = set()

def serch_by_art(art):
    for i in range(0, len(res)):
        if res[i].atr == art:
            return i
    return -1
    

class Prod:
    def __init__(self, atr, price, many, last):
        self.atr = atr
        self.price = price
        # проданных
        self.many = many  
        # не про   
        self.last = last

data = open('C:/Users/endoc/Documents/GitHub/inf-ege-2025/26/26_17643.txt', 'r').readlines()

for i in range(0, 1000):
    dat = list(map(int, data[i].split(" ")))
    p = Prod(dat[0], dat[1], dat[2], 0)
    codes.add(p.atr)
    if p.atr in codes:
        _id  = serch_by_art(p.atr)
        if _id != -1:
            res[_id].last += 1
    mid_price += p.price
    res.append(p)

mid_price = mid_price / 9992

