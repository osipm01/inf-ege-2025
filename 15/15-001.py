

def d(x, n):
    return n % x == 0

# print(d(2, 4))

B = [i for i in range(70, 91)]

# print(B)

for A in range(1, 900):
    for x in range(1, 900):
        if d(x, A) or ((x in B) <= d(x, 22)) == 1:
            print(A)