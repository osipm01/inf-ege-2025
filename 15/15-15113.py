# ((x < A) → (x2 < 100)) ∧ ((y2 ≤ 64) → (y ≤ A))

cnt = 0

for a in range(300):
    flag = True
    for y in range(300):
        for x in range(300):
            if not (((x < a) <= (x ** 2 < 100)) and ((y ** 2 <= 64) <= (y <= a))):
                flag = False
                break
    if flag:
         cnt += 1

print(cnt)

