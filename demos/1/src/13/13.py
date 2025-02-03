import ipaddress

cnt = 0

for i in ipaddress.ip_network('192.168.32.160/255.255.255.240'):
    if str(i).count('1') % 2 == 0:
        cnt += 1

print(cnt)