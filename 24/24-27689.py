
data = open('24-27689.txt').readline()

data = data.replace('XYZ', 'T')

counter, mx = 0, 0

for i in range(len(data)):
    if data[i] == 'T':
        counter += 1
    else:
        mx = max(mx, counter)
        counter = 0

print(mx)