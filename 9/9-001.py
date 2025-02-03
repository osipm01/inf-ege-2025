cnt = 0

lines = open('9-001.txt').readlines()
for line in lines:
    numbers = list(map(int, line.split()))
    mx = max(numbers)
    s_mx = sum(numbers)

    if mx < s_mx:
        if len(set(numbers)) == 4:
            cnt += 1




print(cnt)
