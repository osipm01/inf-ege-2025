
# 210235; 210300

for i in range(210235, 210300 + 1):
    div = set()
    for j in range(2, i // 2):
        if i % j == 0:
            div.add(j)
    if len(div) == 4:
        print(div)


