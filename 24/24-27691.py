

data = open("./24-27691.txt").readline()

mx = 0
counter = 1

for i in range(0, len(data) - 1):
    if data[i] == 'A' and data[i + 1] == 'A':
        counter += 1
    else:
        mx = max(mx, counter)
        counter = 1

print(mx
      )