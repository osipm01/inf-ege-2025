
data = open('24-27699.txt').readline().replace('LDR', 'X')

counter, mx = 0, 0

for i in range(len(data)):
    if data[i] == 'X':
        counter += 1
    else:
        mx = max(mx, counter)
        counter = 1


print(mx * 3)