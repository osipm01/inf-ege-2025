
with open('27880.txt', 'r') as file:
    S, N = [int(x) for x in file.readline().split()]
    a = sorted([int(x) for x in file])
    file.close()

    M, maxi = 0, 0

    for i in range(N):
        if M + a[i] <= S:
            M += a[i]
            maxi = i

    t = a[maxi]
    for i in range(0, maxi + 1, N):
        if M - t + a[i] <= S:
            M = M - t + a[i]
            t = a[i]


print(maxi + 1, t)