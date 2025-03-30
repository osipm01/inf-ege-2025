import sys

# 9992 99906 6661

M = 9992
N = 99906
K = 6661

data = [line for line in open("26-20910.txt").readline().split("\n")]

for i in range(M):
    r = data[i].split(" ")
    for j in range(N):
        print(int(r[0]), int(r[1]))