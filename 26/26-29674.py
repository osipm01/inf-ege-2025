import math
N = 1000

data = [int(i) for i in open("C:/Users/endoc/Documents/GitHub/inf-ege-2025/26/26-29674.txt", "r")]

price = []
price_no_sale = []
max_sale_id = 0

for i in range(0, len(data)):
    if data[i] <= 50:
        price_no_sale.append(data[i])
    price.append(data[i])

price = sorted(price)
max_sale_id = (len(price) - 1) // 2

sum_s = sum(price[0:max_sale_id]) * 0.75  
_sum = sum(price[max_sale_id:])

ss = sum_s + _sum + sum(price_no_sale)

print(math.ceil(ss), price[max_sale_id])