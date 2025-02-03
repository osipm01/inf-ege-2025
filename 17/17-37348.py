
data = [int(i) for i in open("17-37348.txt")]

cnt, mx = 0, 0

for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] * data[j] % 34 != 0:
            cnt += 1
            mx = max(mx, data[i] + data[j])

print(cnt, mx)
