import ipaddress
from ipaddress import IPv4Address

mask = "255.255.248.0"
ip_addr = "172.16.168.0"
cnt = 0

# for ip in ipaddress.ip_network(f'{ip_addr}/{mask}'):
#     bin_ip = str(bin(ip))
#     if bin_ip.count("0") % 5 == 0:
#         cnt+=1

for ip in ipaddress.ip_network(f'{ip_addr}/{mask}'):
    if str(bin(int(ip))).count("0") % 5 != 0:
        cnt+=1

print(cnt)