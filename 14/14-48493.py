# y04x5 + 253xy.

alph = "01234567"

for x in alph:
    for y in alph:
        val = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)
        if val % 117 == 0:
            print(val // 117)