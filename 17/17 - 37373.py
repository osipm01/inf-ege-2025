
data = [int(i) for i in open("17-37373.txt")]

cnt, mx = 0, 0

for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] - data[j]) % 36 == 0:
            if data[i] % 13 == 0 or data[j] % 13 == 0:
                cnt += 1
                mx = max(mx, data[i] - data[j])

print(cnt, mx)


# count = m = 0
# f = open('17-37373.txt')
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] - l[j]) % 36 == 0 and (l[i] % 13 == 0 or l[j] % 13 == 0):
#             count += 1
#             m = max(m, abs(l[i] - l[j]))
# print(count, m)
# 212587 9972