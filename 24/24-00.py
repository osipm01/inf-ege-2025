

data = [i for i in open('demo_2025_24.txt')]

cnt = 0
mx = -10 ** 9

for i in range(0, len(data) - 1):
    if data[i] == 'A' and data[i + 1] == 'A':
        cnt +=1
    else:
        mx = max(mx, cnt)
        cnt = 0

print(mx)