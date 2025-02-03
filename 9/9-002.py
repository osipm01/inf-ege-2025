cnt = 0

lines = open('9-002.txt').readlines()

for line in lines:
    numbers = list(map(int, line.split()))
    numbers.sort()
    if numbers[0] * numbers[2] + numbers[0] * numbers[1] < numbers[1] * numbers[2]:
        cnt+=1


print(cnt)