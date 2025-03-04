
f = open("24-68525.txt", "r")

s = f.readline()

s = s.replace("Q", "A").replace("R", "A").replace("W", "A")
s = s.replace("2", "1").replace("4", "1")

cnt = 0
mx = 0

for i in range(0, len(s) - 1):
    if s[i] != s[i + 1]:
        cnt += 1
    else:
        mx = max(mx, cnt)
        cnt = 1

print(mx)