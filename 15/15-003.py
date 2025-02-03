
# (y + 2x < A) ∨ (x > 15) ∨ (y > 30)

def f(x, y, A):
    return (y + 2*x < A) or (x > 15) or (y > 30)
for A in range(300):
    cnt = 0
    for x in range(300):
        for y in range(300):
           if f(x, y, A):
               cnt += 1
    if cnt == 90_000:
        print(A)
        break


