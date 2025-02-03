
def to_sys(base, num):
    if num == 0:
        return '0'
    digits = '0123456789ABCDEF'
    res = ''
    while num:
        res = digits[num % base] + res
        num //= base
    return res
    

print(to_sys(8, 688))
print(oct(688))