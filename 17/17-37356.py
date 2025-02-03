

data = [int(i) for i in open("17-37356.txt")]

cnt, mx = 0, 0

for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] + data[j]) % 9 == 0:
            cnt += 1
            mx = max(mx, data[i] + data[j])

print(cnt, mx)

# path = "17-37356.txt"
#
# count = m = 0
# f = open(path)
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] + l[j]) % 9 == 0:
#             count += 1
#             m = max(m, l[i] + l[j])
# print(count, m)