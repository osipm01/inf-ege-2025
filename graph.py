s = "867+878++075+87=9"

nv = "+-/%*"
r = "="
res = 0

buf = ""

for i in range(len(s)):
    if s[i] in nv and s[i+1] not in nv and s[i+1] not in r:
        buf += s[i]
    elif s[i] in r:
        res = eval(buf)
        buf = ""
    else:
        buf = ""

print(res)