
data = open('24-27688.txt').readline()

counter, mx = 1, 0

for i in range(len(data) - 1):
    if data[i] == 'Z' and data[i + 1] == 'Z':
        counter += 1
        mx = max(mx, counter)
    else:
        counter = 1

print(mx)
