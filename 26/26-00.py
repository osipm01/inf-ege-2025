
dat = [line for line in open('./demo_2025_26.txt').read().splitlines()]

for line in dat:
    data = line.split()

    mid_ball = (int(data[1]) + int(data[2]) + int(data[3]) + int(data[4])) / 4
