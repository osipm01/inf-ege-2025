
data = open('24-27692.txt').readline()

counter, mx = 1, 0

for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        counter += 1
        mx = max(mx, counter)
    else:
        counter = 1


print(mx)