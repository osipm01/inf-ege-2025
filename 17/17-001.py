
data = [int(x) for x in open('17-001.txt')]


cnt, mx = 0, 0

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] + data[j]) % 60 == 0:
            if data[i] % 40 == 0 or data[j] % 40 == 0:
                cnt += 1
                mx = max(mx, data[i] + data[j])

print(cnt, mx)