
alph = "0123456789AB"

# x231y12 + 78x98y14.

res = []

for x in alph:
    for y in alph:
        t = int(f"{x}231{y}12", 12) + int(f"78{x}98{y}14", 14)
        if t % 99 == 0:
            res.append(t)

print(min(res) // 99)